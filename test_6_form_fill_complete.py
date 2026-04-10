from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Open Chrome
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)
print("PASS: Chrome opened")

# Go to practice form
driver.get("https://demoqa.com/automation-practice-form")
print("PASS: Opened form page")

# Fill First Name
first_name = driver.find_element(By.ID, "firstName")
first_name.send_keys("John")
print("PASS: Entered first name")

# Fill Last Name
last_name = driver.find_element(By.ID, "lastName")
last_name.send_keys("Tester")
print("PASS: Entered last name")

# Fill Email
email = driver.find_element(By.ID, "userEmail")
email.send_keys("john.tester@test.com")
print("PASS: Entered email")

# Select Gender
male_radio = driver.find_element(
    By.XPATH, "//label[@for='gender-radio-1']")
male_radio.click()
print("PASS: Selected gender")

# Fill Phone
phone = driver.find_element(By.ID, "userNumber")
phone.send_keys("9000000001")
print("PASS: Entered phone")

# Fill Subjects
subjects = driver.find_element(By.ID, "subjectsInput")
subjects.send_keys("Computer Science")
time.sleep(1)
subjects.send_keys(Keys.RETURN)
print("PASS: Entered subject")

# Select Hobbies (Sports checkbox)
hobby_sports = driver.find_element(
    By.XPATH, "//label[@for='hobbies-checkbox-1']")
hobby_sports.click()
print("PASS: Selected Sports hobby")

# Select Reading checkbox
hobby_reading = driver.find_element(
    By.XPATH, "//label[@for='hobbies-checkbox-2']")
hobby_reading.click()
print("PASS: Selected Reading hobby")

# Fill Address
address = driver.find_element(
    By.ID, "currentAddress")
address.send_keys("123 Test Street, Hyderabad")
print("PASS: Entered address")

# Scroll down to see dropdowns
driver.execute_script(
    "window.scrollTo(0, 500)")
time.sleep(1)

# Select State dropdown
state = driver.find_element(
    By.ID, "react-select-3-input")
state.send_keys("NCR")
time.sleep(1)
state.send_keys(Keys.RETURN)
print("PASS: Selected state")

# Select City dropdown
city = driver.find_element(
    By.ID, "react-select-4-input")
city.send_keys("Delhi")
time.sleep(1)
city.send_keys(Keys.RETURN)
print("PASS: Selected city")

# Wait to see everything filled
time.sleep(3)

# Take screenshot
driver.save_screenshot("form_filled_complete.png")
print("PASS: Screenshot saved!")

# Close
driver.quit()
print("PASS: Complete form test done!")

