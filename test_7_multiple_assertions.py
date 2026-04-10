from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Open Chrome
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)
print("PASS: Chrome opened")

# Go to login page
driver.get("https://the-internet.herokuapp.com/login")
print("PASS: Opened login page")

# ASSERTION 1: Check page title
if "The Internet" in driver.title:
    print("PASS: Page title is correct!")
else:
    print("FAIL: Page title is wrong!")

# ASSERTION 2: Check username field exists
username_field = driver.find_element(By.ID, "username")
if username_field.is_displayed():
    print("PASS: Username field is visible!")
else:
    print("FAIL: Username field not visible!")

# ASSERTION 3: Check password field exists
password_field = driver.find_element(By.ID, "password")
if password_field.is_displayed():
    print("PASS: Password field is visible!")
else:
    print("FAIL: Password field not visible!")

# ASSERTION 4: Check login button exists
login_button = driver.find_element(
    By.CLASS_NAME, "radius")
if login_button.is_displayed():
    print("PASS: Login button is visible!")
else:
    print("FAIL: Login button not visible!")

# Now actually login
username_field.send_keys("tomsmith")
password_field.send_keys("SuperSecretPassword!")
login_button.click()
print("PASS: Clicked login")

time.sleep(3)

# ASSERTION 5: Check login succeeded
if "secure" in driver.current_url:
    print("PASS: Login successful!")
else:
    print("FAIL: Login failed!")

# Take screenshot as proof
driver.save_screenshot("multiple_assertions.png")
print("PASS: Screenshot saved!")

# Close
driver.quit()
print("PASS: All assertions completed!")