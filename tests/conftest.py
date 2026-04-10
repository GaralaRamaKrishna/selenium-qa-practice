import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def driver():
    print("\nSETUP: Starting Chrome for test suite...")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
    driver.maximize_window()
    print("SETUP: Chrome ready!")

    yield driver

    print("\nTEARDOWN: Closing Chrome...")
    driver.quit()
    print("TEARDOWN: Done!")