from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# This opens Chrome browser automatically
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

# Go to Google
driver.get("https://www.google.com")

# Print the page title
print("Page Title:", driver.title)

# Wait 3 seconds so you can see it
import time
time.sleep(3)

# Close browser
driver.quit()
print("Test Completed Successfully!")