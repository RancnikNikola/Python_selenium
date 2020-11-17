# Import what is needed
import time
from Contact_us_locators import ContactUsPageLocators


# Class for Contact us page
class ContactUsPage:
    def __init__(self, driver):
        self.driver = driver

    # From Subject Heading dropdown click on Customer Service
    # Email address field is already populated (If logged in)
    # From Order reference dropdown click on first product, the product code is "CIPYAIZJH"
    # From Product dropdown click "Faded Short Sleeve T-shirts - Color : Blue, size M"
    # In Attach File input field, send a PDF file "IN027828.pdf"
    # In Message textbox field, type the message you want
    # Click on SEND button
    def populate_a_contact_message_fields(self):
        self.driver.find_element(*ContactUsPageLocators.SUBJECT_HEADING_CUSTOMER_SERVICE).click()
        time.sleep(1)
        self.driver.find_element(*ContactUsPageLocators.ORDER_REFERENCE).click()
        time.sleep(2)
        self.driver.find_element(*ContactUsPageLocators.CHOOSE_PRODUCT).click()
        time.sleep(2)
        self.driver.find_element(*ContactUsPageLocators.ATTACH_FILE).send_keys(*ContactUsPageLocators.PDF_PATH)
        time.sleep(1)
        self.driver.find_element(*ContactUsPageLocators.CONTACT_TEXTAREA).send_keys(*ContactUsPageLocators.CONTACT_TEXTAREA_MESSAGE)
        time.sleep(1)
        self.driver.find_element(*ContactUsPageLocators.SEND_CONTACT_US_MESSAGE_BTN).click()
        time.sleep(1)


