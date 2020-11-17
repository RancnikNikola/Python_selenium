# Import what is needed
import time
from Women_page_locators import WomenPageLocators


# Class for Women page
class WomenPage:
    def __init__(self, driver):
        self.driver = driver

    # Click on "Add to cart" button on WOMEN page
    # After clicking the "Add to cart" button, the popup window will appear
    # In the popup window, click "PROCEED TO CHECKOUT" button
    def add_to_cart_and_proceed(self):
        self.driver.find_element(*WomenPageLocators.ADD_TO_CART_BEFORE).click()
        time.sleep(1)
        self.driver.find_element(*WomenPageLocators.PROCEED_TO_CHECKOUT_BTN_1).click()
        time.sleep(1)

    # Click on "Add to wishlist" button on WOMEN page
    # After clicking on "Add to wishlist" button, the popup will appear with text "Added to your wishlist"
    # Close the popup by clicking the "X" button of popup window
    def add_to_wishlist_and_close_popup(self):
        self.driver.find_element(*WomenPageLocators.ADD_TO_WISHLIST).click()
        time.sleep(2)
        self.driver.find_element(*WomenPageLocators.CLOSE_WISHLIST_POPUP).click()
        time.sleep(2)
        # Click on "Your profile" button
        # self.driver.find_element(*WomenPageLocators.USERS_PROFILE_BTN).click()
        # time.sleep(2)
        # # Click on "My Wishlist" button
        # self.driver.find_element(*WomenPageLocators.MY_WISHLIST_BTN).click()
        # time.sleep(1)

    # Click "MORE" button of the product on WOMEN page
    def click_on_more_btn(self):
        self.driver.find_element(*WomenPageLocators.PRODUCT_MORE_BTN).click()
        time.sleep(2)

    # Click on "BLUE" color box of the product on WOMEN page
    def click_blue_color_before(self):
        self.driver.find_element(*WomenPageLocators.BLUE_COLOR).click()
        time.sleep(2)

    # Click on "ORANGE" color box of the product on WOMEN page
    def click_orange_color_before(self):
        self.driver.find_element(*WomenPageLocators.ORANGE_COLOR).click()
        time.sleep(2)


