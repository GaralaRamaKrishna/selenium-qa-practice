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

driver.get("https://the-internet.herokuapp.com/login")
print("PASS: Opened login page")

wait = WebDriverWait(driver, 10)

# XPath 1 — Find by attribute
username = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//input[@id='username']")))
username.send_keys("tomsmith")
print("PASS: XPath by attribute — username found!")

# XPath 2 — Find by type attribute
password = driver.find_element(
    By.XPATH, "//input[@type='password']")
password.send_keys("SuperSecretPassword!")
print("PASS: XPath by type — password found!")

# XPath 3 — Find button by text
login_btn = driver.find_element(
    By.XPATH,
    "//button[normalize-space()='Login']")
login_btn.click()
print("PASS: XPath contains text — button found!")

# Wait for login
wait.until(EC.url_contains("secure"))
print("PASS: Login successful!")

# XPath 4 — Find heading by tag
heading = driver.find_element(
    By.XPATH, "//h2")
print("PASS: Page heading:", heading.text)

# XPath 5 — Find by partial class
flash_msg = driver.find_element(
    By.XPATH, "//div[contains(@class,'flash')]")
print("PASS: Flash message:", flash_msg.text[:50])

driver.quit()
print("PASS: XPath test completed!")