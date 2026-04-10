from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)
print("PASS: Chrome opened")

# Create screenshots folder if not exists
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")
    print("PASS: Screenshots folder created")

driver.get("https://the-internet.herokuapp.com/login")
print("PASS: Opened login page")

wait = WebDriverWait(driver, 10)

# TEST 1 — This will PASS
print("\n--- TEST 1: Valid Login ---")
try:
    username = wait.until(
        EC.presence_of_element_located(
            (By.ID, "username")))
    username.send_keys("tomsmith")

    password = driver.find_element(
        By.ID, "password")
    password.send_keys("SuperSecretPassword!")

    login_btn = driver.find_element(
        By.CLASS_NAME, "radius")
    login_btn.click()

    wait.until(EC.url_contains("secure"))
    print("PASS: Valid login passed!")
    driver.save_screenshot(
        "screenshots/test1_pass.png")
    print("PASS: Screenshot saved!")

except Exception as e:
    driver.save_screenshot(
        "screenshots/test1_FAIL.png")
    print("FAIL: Test 1 failed!")
    print("Error:", str(e))

# Go back for TEST 2
driver.get("https://the-internet.herokuapp.com/login")

# TEST 2 — Deliberately FAILING test
print("\n--- TEST 2: Wrong Element (will fail) ---")
try:
    # This will fail — wrong ID on purpose!
    wrong_element = wait.until(
        EC.presence_of_element_located(
            (By.ID, "this_does_not_exist")))
    print("PASS: Element found!")

except Exception as e:
    driver.save_screenshot(
        "screenshots/test2_FAIL.png")
    print("FAIL: Element not found!")
    print("Error:", str(e)[:80])
    print("PASS: Screenshot saved as evidence!")

driver.quit()
print("\nPASS: Screenshot test completed!")
print("Check screenshots/ folder for images!")