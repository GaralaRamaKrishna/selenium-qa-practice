from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Open Chrome
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)
print("PASS: Chrome opened")

# Go to login page
driver.get("https://the-internet.herokuapp.com/login")
print("PASS: Opened login page")

# Explicit Wait — wait for username field
wait = WebDriverWait(driver, 10)

username = wait.until(
    EC.presence_of_element_located(
        (By.ID, "username")))
print("PASS: Username field found!")

# Wait for password field
password = wait.until(
    EC.presence_of_element_located(
        (By.ID, "password")))
print("PASS: Password field found!")

# Wait for login button to be clickable
login_btn = wait.until(
    EC.element_to_be_clickable(
        (By.CLASS_NAME, "radius")))
print("PASS: Login button ready!")

# Fill and submit
username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")
login_btn.click()
print("PASS: Clicked login")

# Wait for secure page to load
wait.until(EC.url_contains("secure"))
print("PASS: Login successful!")

# Close
driver.quit()
print("PASS: Test completed!")