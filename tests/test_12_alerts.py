from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)
print("PASS: Chrome opened")

wait = WebDriverWait(driver, 10)

# Go to alerts practice page
driver.get(
    "https://the-internet.herokuapp.com/javascript_alerts")
print("PASS: Opened alerts page")

# TEST 1 — Simple Alert (OK only)
print("\n--- TEST 1: Simple Alert ---")
alert_btn = driver.find_element(
    By.XPATH, "//button[normalize-space()='Click for JS Alert']")
alert_btn.click()

# Switch to alert
alert = wait.until(EC.alert_is_present())
print("PASS: Alert appeared!")
print("Alert text:", alert.text)

# Accept (click OK)
alert.accept()
print("PASS: Clicked OK on alert!")

# TEST 2 — Confirm Alert (OK + Cancel)
print("\n--- TEST 2: Confirm Alert ---")
confirm_btn = driver.find_element(
    By.XPATH, "//button[normalize-space()='Click for JS Confirm']")
confirm_btn.click()

confirm = wait.until(EC.alert_is_present())
print("PASS: Confirm appeared!")
print("Confirm text:", confirm.text)

# Dismiss (click Cancel)
confirm.dismiss()
print("PASS: Clicked Cancel!")

# TEST 3 — Prompt Alert (with text input)
print("\n--- TEST 3: Prompt Alert ---")
prompt_btn = driver.find_element(
    By.XPATH, "//button[normalize-space()='Click for JS Prompt']")
prompt_btn.click()

prompt = wait.until(EC.alert_is_present())
print("PASS: Prompt appeared!")

# Type text in prompt
prompt.send_keys("Rama QA Testing")
print("PASS: Typed in prompt!")

# Accept
prompt.accept()
print("PASS: Submitted prompt!")

# Check result
result = driver.find_element(By.ID, "result")
print("Result shown:", result.text)

driver.quit()
print("\nPASS: Alert tests completed!")