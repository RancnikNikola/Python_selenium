from selenium.webdriver.common.by import By


# Class for contact us page locators
# All Contact us page locators are here
class ContactUsPageLocators:

    SUBJECT_HEADING_CUSTOMER_SERVICE = (By.XPATH, '//*[@id="id_contact"]/option[2]')
    ORDER_REFERENCE = (By.XPATH, '//*[@id="center_column"]/form/fieldset/div[1]/div[1]/div[2]/div/select/option[2]')
    CHOOSE_PRODUCT = (By.XPATH, '//*[@id="253601_order_products"]/option[2]')
    ATTACH_FILE = (By.ID, 'fileUpload')
    CONTACT_TEXTAREA = (By.ID, 'message')
    CONTACT_TEXTAREA_MESSAGE = 'This is the message from the contact us page bla bla bla'
    SEND_CONTACT_US_MESSAGE_BTN = (By.ID, 'submitMessage')
    DOC_NAME = 'IN027828.pdf'
    PDF_PATH = '/Users/nikolarancnik/Desktop/IN027828.pdf'



