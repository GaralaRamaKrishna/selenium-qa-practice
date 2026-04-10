from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    # URL
    URL = "https://the-internet.herokuapp.com/login"

    # Locators — all in one place!
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "radius")
    FLASH_MESSAGE = (By.ID, "flash")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)
        print("PASS: Opened login page")

    def enter_username(self, username):
        field = self.wait.until(
            EC.presence_of_element_located(
                self.USERNAME_FIELD))
        field.send_keys(username)
        print("PASS: Entered username")

    def enter_password(self, password):
        field = self.wait.until(
            EC.presence_of_element_located(
                self.PASSWORD_FIELD))
        field.send_keys(password)
        print("PASS: Entered password")

    def click_login(self):
        btn = self.wait.until(
            EC.element_to_be_clickable(
                self.LOGIN_BUTTON))
        btn.click()
        print("PASS: Clicked login")

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_flash_message(self):
        msg = self.wait.until(
            EC.presence_of_element_located(
                self.FLASH_MESSAGE))
        return msg.text

    def is_login_successful(self):
        return "secure" in self.driver.current_url