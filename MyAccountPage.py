# Import what is needed
import time
from My_account_locators import MyAccountPageLocators


# Class for My Account page
class AccountPage:
    def __init__(self, driver):
        self.driver = driver

    # Click on "WOMEN" button in navigation bar
    # Click on "LIST VIEW" to see the products as list
    def navigate_to_list_view(self):
        self.driver.find_element(*MyAccountPageLocators.WOMEN_NAVBAR).click()
        time.sleep(1)
        self.driver.find_element(*MyAccountPageLocators.LIST_VIEW_BTN).click()
        time.sleep(1)

    # Click on "ORDER HISTORY AND DETAILS"
    # Scroll to the bottom of the page
    # Click on "Back to your account" to go back to account page
    def click_order_history_and_details(self):
        self.driver.find_element(*MyAccountPageLocators.ORDER_HISTORY_AND_DETAILS).click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.find_element(*MyAccountPageLocators.BACK_TO_ACC).click()
        time.sleep(2)

    """ODAVDE PUT DOLE NASTAVAK"""
    def click_credit_slips(self):
        self.driver.find_element(*MyAccountPageLocators.CREDIT_SLIPS).click()
        time.sleep(2)
        self.driver.find_element(*MyAccountPageLocators.BACK_TO_ACC).click()
        time.sleep(2)

    # ODE IMA JOS MASU POSLA
    def click_my_addresses(self):
        self.driver.find_element(*MyAccountPageLocators.MY_ADDRESSES).click()
        time.sleep(2)
        self.driver.find_element(*MyAccountPageLocators.BACK_TO_ACC).click()
        time.sleep(2)

    # I ODE IMA JOS MASU POSLA
    def click_my_personal_information(self):
        self.driver.find_element(*MyAccountPageLocators.MY_PERSONAL_INFORMATION).click()
        time.sleep(2)
        self.driver.find_element(*MyAccountPageLocators.BACK_TO_ACC).click()
        time.sleep(2)

    # IMA I ODE POSLA AL NE MASU TOLIKO
    def click_my_wishlist(self):
        self.driver.find_element(*MyAccountPageLocators.MY_WISHLIST).click()
        time.sleep(2)
        self.driver.find_element(*MyAccountPageLocators.BACK_TO_ACC).click()
        time.sleep(2)



