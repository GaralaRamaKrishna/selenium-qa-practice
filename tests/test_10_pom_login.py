from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page  import LoginPage

# Open Chrome
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)
print("PASS: Chrome opened")

# Create page object
login = LoginPage(driver)

# TEST 1 — Valid Login
print("\n--- TEST 1: Valid Login ---")
login.open()
login.login("tomsmith", "SuperSecretPassword!")

if login.is_login_successful():
    print("PASS: Valid login test passed!")
else:
    print("FAIL: Valid login test failed!")

# Go back to login page
driver.get("https://the-internet.herokuapp.com/login")

# TEST 2 — Invalid Login
print("\n--- TEST 2: Invalid Login ---")
login.login("wronguser", "wrongpass")

message = login.get_flash_message()
if "invalid" in message.lower():
    print("PASS: Invalid login test passed!")
else:
    print("FAIL: Invalid login test failed!")

# Close
driver.quit()
print("\nPASS: All POM tests completed!")
