# Import what is needed
import time
from Main_page_locators import MainPageLocators


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    # In the navbar, on the right side of website, click "Sign in" button
    def navigate_to_login_page(self):
        self.driver.find_element(*MainPageLocators.SING_IN_TO_PAGE_LOCATOR).click()
        time.sleep(1)

    # Find search input field, and write in the term you want to search, I've searched for "T shirt"
    # After typing the term you want to search, click on "magnifier" icon button
    def search_for_term(self):
        self.driver.find_element(*MainPageLocators.SEARCH_INPUT).send_keys(*MainPageLocators.SEARCH_TERM)
        time.sleep(2)
        self.driver.find_element(*MainPageLocators.SEARCH_BTN).click()
        time.sleep(1)

