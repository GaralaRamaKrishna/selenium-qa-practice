import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN_URL = "https://the-internet.herokuapp.com/login"


class TestLoginSuite:

    # TEST 1
    def test_page_loads(self, driver):
        driver.get(LOGIN_URL)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.title_contains("The Internet"))
        assert "The Internet" in driver.title
        print("PASS: Page loaded!")

    # TEST 2
    def test_username_visible(self, driver):
        driver.get(LOGIN_URL)
        username = driver.find_element(
            By.ID, "username")
        assert username.is_displayed()
        print("PASS: Username visible!")

    # TEST 3
    def test_password_visible(self, driver):
        driver.get(LOGIN_URL)
        password = driver.find_element(
            By.ID, "password")
        assert password.is_displayed()
        print("PASS: Password visible!")

    # TEST 4
    def test_login_button_visible(self, driver):
        driver.get(LOGIN_URL)
        btn = driver.find_element(
            By.CLASS_NAME, "radius")
        assert btn.is_displayed()
        print("PASS: Login button visible!")

    # TEST 5
    def test_valid_login(self, driver):
        driver.get(LOGIN_URL)
        wait = WebDriverWait(driver, 10)

        username = wait.until(
            EC.presence_of_element_located(
                (By.ID, "username")))
        username.send_keys("tomsmith")

        password = driver.find_element(
            By.ID, "password")
        password.send_keys("SuperSecretPassword!")

        driver.find_element(
            By.CLASS_NAME, "radius").click()

        wait.until(EC.url_contains("secure"))
        assert "secure" in driver.current_url
        print("PASS: Valid login works!")

    # TEST 6
    def test_invalid_login(self, driver):
        driver.get(LOGIN_URL)
        wait = WebDriverWait(driver, 15)

        username = wait.until(
            EC.presence_of_element_located(
                (By.ID, "username")))
        username.send_keys("wronguser")

        password = driver.find_element(
            By.ID, "password")
        password.send_keys("wrongpass")

        driver.find_element(
            By.CLASS_NAME, "radius").click()

        import time
        time.sleep(2)

        error = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "flash")))
        assert "invalid" in error.text.lower()
        print("PASS: Invalid login blocked!")

    # TEST 7
    def test_empty_login(self, driver):
        driver.get(LOGIN_URL)
        wait = WebDriverWait(driver, 10)

        driver.find_element(
            By.CLASS_NAME, "radius").click()

        import time
        time.sleep(2)

        # Website stays on login page
        # when empty credentials submitted
        assert "login" in driver.current_url
        print("PASS: Empty login stays on login page!")



