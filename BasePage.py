from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import MainPageLocators

# PATH to chromium driver
C_PATH = '/Users/nikolarancnik/chromedriver'
# Set Chrome as driver
# driver = webdriver.Chrome(executable_path=C_PATH)
# Define wait
# wait = WebDriverWait(driver, 10)
# Define URL
PROJECT_URL = "http://automationpractice.com/index.php"
# Define user email
# user_email = "brucewayne@mailinator.com"
# # Define user password
# user_password = "waynebruce94"
# Go to
# driver.get(PROJECT_URL)


class BasePage:
    """Base class to initialize the base page that will be called from all pages"""

    driver = webdriver.Chrome(executable_path=C_PATH)

    def __init__(self, driver):
        self.driver = driver

    def click_on_sign_in_button(self, by_locator):
        """Clicks the sign in button"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()



