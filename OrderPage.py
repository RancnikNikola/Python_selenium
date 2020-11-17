# Import what is needed
import time
from Orders_page_locators import OrdersPageLocators


# Class for Orders page
class OrdersPage:
    def __init__(self, driver):
        self.driver = driver

    # Click on "PROCEED TO CHECKOUT" button in orders page
    # In textarea with a heading
    # "If you would like to add a comment about your order, please write in the field below.",
    # type in comment about your order
    # Click on "PROCEED TO CHECKOUT" button again
    # Click on link text "Read the Terms of Service" to read the terms of service
    # After reading Terms of Service, close the popup window clicking on "X" button of the window
    # Click on checkbox to agree to the terms of service
    # Click on "PROCEED TO CHECKOUT" button last time
    # Click on "Pay by bank wire(order processing will be longer)" to pay with bank wire
    # Click on "I confirm my order" button to finish your order
    def proceed_to_checkout(self):
        self.driver.find_element(*OrdersPageLocators.PROCEED_TO_CHECKOUT_BTN_2).click()
        time.sleep(2)
        self.driver.find_element(*OrdersPageLocators.TEXTAREA_MSG).send_keys(*OrdersPageLocators.COMMENT_MSG)
        time.sleep(1)
        self.driver.find_element(*OrdersPageLocators.PROCEED_TO_CHECKOUT_BTN_3).click()
        time.sleep(1)
        self.driver.find_element(*OrdersPageLocators.TERMS_OF_SERVICE_OPEN).click()
        time.sleep(2)
        self.driver.find_element(*OrdersPageLocators.TERMS_OF_SERVICE_CLOSE).click()
        time.sleep(1)
        self.driver.find_element(*OrdersPageLocators.TERMS_CHECKBOX).click()
        time.sleep(1)
        self.driver.find_element(*OrdersPageLocators.PROCEED_TO_CHECKOUT_BTN_4).click()
        time.sleep(1)
        self.driver.find_element(*OrdersPageLocators.BANK_WIRE_BTN).click()
        time.sleep(1)
        self.driver.find_element(*OrdersPageLocators.CONFIRM_ORDER_BTN).click()
        time.sleep(1)





