from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_page_title():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
    driver.get("https://the-internet.herokuapp.com/login")

    # Assert page title
    assert "The Internet" in driver.title
    print("PASS: Title correct!")

    driver.quit()


def test_valid_login():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
    driver.get("https://the-internet.herokuapp.com/login")
    wait = WebDriverWait(driver, 10)

    # Login
    username = wait.until(
        EC.presence_of_element_located(
            (By.ID, "username")))
    username.send_keys("tomsmith")

    password = driver.find_element(By.ID, "password")
    password.send_keys("SuperSecretPassword!")

    login_btn = driver.find_element(
        By.CLASS_NAME, "radius")
    login_btn.click()

    # Assert login worked
    wait.until(EC.url_contains("secure"))
    assert "secure" in driver.current_url
    print("PASS: Login successful!")

    driver.quit()


def test_invalid_login():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
    driver.get("https://the-internet.herokuapp.com/login")
    wait = WebDriverWait(driver, 10)

    # Wrong credentials
    username = wait.until(
        EC.presence_of_element_located(
            (By.ID, "username")))
    username.send_keys("wronguser")

    password = driver.find_element(By.ID, "password")
    password.send_keys("wrongpassword")

    login_btn = driver.find_element(
        By.CLASS_NAME, "radius")
    login_btn.click()

    # Assert error shown
    error = wait.until(
        EC.presence_of_element_located(
            (By.ID, "flash")))
    assert "invalid" in error.text.lower()
    print("PASS: Error message correct!")

    driver.quit()
