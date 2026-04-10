from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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

# Select Gender Radio Button (Male)
male_radio = driver.find_element(
    By.XPATH, "//label[@for='gender-radio-1']")
male_radio.click()
print("PASS: Selected Male gender")

# Fill Phone Number
phone = driver.find_element(By.ID, "userNumber")
phone.send_keys("9000000001")
print("PASS: Entered phone number")

# Wait to see form filled
time.sleep(3)

# Take screenshot as proof
driver.save_screenshot("form_filled.png")
print("PASS: Screenshot saved!")

# Close browser
driver.quit()
print("PASS: Form test completed!")
