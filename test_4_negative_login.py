from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://the-internet.herokuapp.com/login")
print("PASS: Opened login page")

# Enter WRONG credentials
username = driver.find_element(By.ID, "username")
username.send_keys("wronguser")
print("PASS: Entered wrong username")

password = driver.find_element(By.ID, "password")
password.send_keys("wrongpassword")
print("PASS: Entered wrong password")

# Click login
login_button = driver.find_element(By.CLASS_NAME,
    "radius")
login_button.click()
print("PASS: Clicked login button")

time.sleep(3)

# Check error message appeared
error = driver.find_element(By.ID, "flash")
if "Your username is invalid" in error.text:
    print("PASS: Error message shown correctly!")
else:
    print("FAIL: Error message not shown!")

driver.quit()
print("PASS: Test completed!")