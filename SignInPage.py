# Import what is needed
import time
from Sing_in_page_locators import SignInPageLocators


# Class for Sign in page
class SingInPage:
    def __init__(self, driver):
        self.driver = driver

    # Under "ALREADY REGISTERED?" title in the "Email address" input field type in
    # email address that you have register with
    # In the "Password" input field write in your password you used to register with email address
    # Click "Sign in" button to login
    def login(self):
        self.driver.find_element(*SignInPageLocators.USER_EMAIL_LOCATOR).send_keys(*SignInPageLocators.USER_EMAIL)
        time.sleep(1)
        self.driver.find_element(*SignInPageLocators.USER_PASSWD_LOCATOR).send_keys(*SignInPageLocators.USER_PASSWD)
        time.sleep(3)
        self.driver.find_element(*SignInPageLocators.SING_IN_LOCATOR).click()

    # Under "CREATE AN ACCOUNT" title in the "Email address" input field type in
    # email address that you want to register with
    # Click "Create an account" button to go to register page
    def enter_email_for_registration(self):
        self.driver.find_element(*SignInPageLocators.EMAIL_REGISTER_INPUT).send_keys(*SignInPageLocators.MAIL_FOR_REGISTRATION)
        time.sleep(2)
        self.driver.find_element(*SignInPageLocators.CREATE_AN_ACCOUNT).click()
        time.sleep(1)

    # In the navbar, on the right side of the website, click "Contact us"
    def click_on_contact_us(self):
        self.driver.find_element(*SignInPageLocators.CONTACT_US_BTN).click()
        time.sleep(1)








