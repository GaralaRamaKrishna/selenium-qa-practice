from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Step 1: Open Chrome browser
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)
print(" Chrome opened")

# Step 2: Go to Google
driver.get("https://duckduckgo.com")
print("Opened Google")

# Step 3: Find search box and type
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium WebDriver Python")
print(" Typed in search box")

# Step 4: Press Enter
search_box.send_keys(Keys.RETURN)
print("Pressed Enter")

# Step 5: Wait 3 seconds to see results
time.sleep(3)

# Step 6: Print page title
print("Page Title:", driver.title)

# Step 7: Close browser
driver.quit()
print(" Test Completed Successfully!")