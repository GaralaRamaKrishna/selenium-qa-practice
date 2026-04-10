import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


# FIXTURE — runs before and after tests
@pytest.fixture(scope="session")
def driver():
    # SETUP — runs before each test
    print("\nSETUP: Opening Chrome...")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
    driver.get(
        "https://the-internet.herokuapp.com/login")
    print("SETUP: Opened login page")

    # Pass driver to test
    yield driver

    # TEARDOWN — runs after each test
    print("\nTEARDOWN: Closing Chrome...")
    driver.quit()
    print("TEARDOWN: Chrome closed!")


# TEST 1 — uses fixture
def test_page_title(driver):
    assert "The Internet" in driver.title
    print("PASS: Title correct!")


# TEST 2 — uses same fixture
def test_username_field_visible(driver):
    username = driver.find_element(
        By.ID, "username")
    assert username.is_displayed()
    print("PASS: Username field visible!")


# TEST 3 — uses same fixture
def test_valid_login(driver):
    wait = WebDriverWait(driver, 10)

    username = wait.until(
        EC.presence_of_element_located(
            (By.ID, "username")))
    username.send_keys("tomsmith")

    password = driver.find_element(
        By.ID, "password")
    password.send_keys("SuperSecretPassword!")

    login_btn = driver.find_element(
        By.CLASS_NAME, "radius")
    login_btn.click()

    wait.until(EC.url_contains("secure"))
    assert "secure" in driver.current_url
    print("PASS: Login successful!")