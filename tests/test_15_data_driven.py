import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


# Test data — list of tuples
login_data = [
    # (username, password, expected_result)
    ("tomsmith", "SuperSecretPassword!", "success"),
    ("wronguser", "wrongpassword", "failure"),
    ("tomsmith", "wrongpassword", "failure"),
    ("", "", "failure"),
]


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
    yield driver
    driver.quit()


@pytest.mark.parametrize(
    "username, password, expected",
    login_data
)
def test_login_data_driven(
        driver, username, password, expected):

    driver.get(
        "https://the-internet.herokuapp.com/login")
    wait = WebDriverWait(driver, 10)

    # Enter credentials
    username_field = wait.until(
        EC.presence_of_element_located(
            (By.ID, "username")))
    username_field.clear()
    username_field.send_keys(username)

    password_field = driver.find_element(
        By.ID, "password")
    password_field.clear()
    password_field.send_keys(password)

    login_btn = driver.find_element(
        By.CLASS_NAME, "radius")
    login_btn.click()

    # Check result
    if expected == "success":
        wait.until(EC.url_contains("secure"))
        assert "secure" in driver.current_url
        print(f"PASS: Login with {username} succeeded!")

    else:
        flash = wait.until(
            EC.presence_of_element_located(
                (By.ID, "flash")))
        assert "invalid" in flash.text.lower() \
            or "password" in flash.text.lower() \
            or len(flash.text) > 0
        print(f"PASS: Login with '{username}' "
              f"correctly failed!")