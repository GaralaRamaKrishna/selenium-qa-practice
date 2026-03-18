from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
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

# Find username field and type
username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")
print("PASS: Entered username")

# Find password field and type
password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")
print("PASS: Entered password")

# Click login button
login_button = driver.find_element(By.CLASS_NAME,
    "radius")
login_button.click()
print("PASS: Clicked login button")

# Wait and check result
time.sleep(3)

# Check if login was successful
if "secure" in driver.current_url:
    print("PASS: Login successful!")
else:
    print("FAIL: Login failed!")

# Close browser
driver.quit()
print("PASS: Test completed!")
