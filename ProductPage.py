# Import what is needed
import time
from Product_page_locators import ProductPageLocators


# Class for Contact us page
class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    # Click link text "Write a review"
    # After clicking "Write a review", popup with form will appear
    # Under the "Write a review" title, in "Quality" field, click on the fifth (5) star
    # In the "Title" input field, write the title of your review, I chose "This is the way"
    # In the "Comment" input field, write the comment of your review, I chose "This is the review comment"
    # Click the "Send" button, to send your review of the product
    # After clicking "Send" button, the popup will appear
    # Click "OK" button to close the popup
    def write_a_product_review_as_logged_user(self):
        self.driver.find_element(*ProductPageLocators.WRITE_REVIEW_LINK).click()
        time.sleep(1)
        self.driver.find_element(*ProductPageLocators.STAR_QUALITY_5).click()
        time.sleep(2)
        self.driver.find_element(*ProductPageLocators.REVIEW_TITLE_INPUT).send_keys(*ProductPageLocators.REVIEW_TITLE)
        time.sleep(2)
        self.driver.find_element(*ProductPageLocators.REVIEW_COMMENT_INPUT).send_keys(*ProductPageLocators.REVIEW_COMMENT)
        time.sleep(2)
        self.driver.find_element(*ProductPageLocators.SEND_REVIEW_BTN).click()
        time.sleep(2)
        self.driver.find_element(*ProductPageLocators.OK_REVIEW_BTN).click()
        time.sleep(2)

    # Click link text "Send to a friend"
    # After clicking "Send to a friend", popup form will appear
    # In the "Name of your friend" input field, type the name of your friend, mine is "Jane Doe"
    # In the "E-mail address of your friend" input field,
    # type the email address of your friend, I chose "Janedoe@unknown.com"
    # Click "Send" button to send the product to your friend
    # After clicking "Send" button, the popup will appear
    # Click "OK" button to close the popup
    def send_to_friend(self):
        self.driver.find_element(*ProductPageLocators.SEND_TO_FRIEND).click()
        time.sleep(2)
        self.driver.find_element(*ProductPageLocators.FRIEND_NAME_INPUT).send_keys(*ProductPageLocators.FRIEND_NAME)
        time.sleep(2)
        self.driver.find_element(*ProductPageLocators.FRIEND_EMAIL_INPUT).send_keys(*ProductPageLocators.FRIEND_EMAIL)
        time.sleep(2)
        self.driver.find_element(*ProductPageLocators.FRIEND_SEND_BTN).click()
        time.sleep(2)
        # Find OK button
        self.driver.find_element(*ProductPageLocators.OK_BUTTON).click()

    # Click "Add to cart" button, after accessing product over the "MORE" button
    def click_add_to_cart_after(self):
        self.driver.find_element(*ProductPageLocators.ADD_TO_CART_AFTER).click()
        time.sleep(2)

    # Click "Add to cart" button, after accessing product over the "MORE" button
    # Click "PROCEED TO CHECKOUT" button that will lead you to orders page
    def click_add_to_cart_after_and_proceed(self):
        self.driver.find_element(*ProductPageLocators.ADD_TO_CART_AFTER).click()
        time.sleep(2)
        self.driver.find_element(*ProductPageLocators.PROCEED_TO_CHECKOUT_BTN_1).click()
        time.sleep(2)

    # Click "Add to wishlist" button, after accessing product over the "MORE" button
    # After clicking "Add to wishlist" button, the popup will appear with text "Added to your wishlist"
    # Close the popup by clicking the "X" button of popup window
    def click_add_to_wishlist_after_more(self):
        self.driver.find_element(*ProductPageLocators.ADD_TO_WISHLIST_MORE).click()
        time.sleep(2)
        self.driver.find_element(*ProductPageLocators.ADD_TO_WISHLIST_MORE_CLOSE).click()
        time.sleep(1)
        # self.driver.find_element(*ProductPageLocators.USERS_PROFILE_BTN).click()
        # time.sleep(2)
        # # Click on "My Wishlist" button
        # self.driver.find_element(*ProductPageLocators.MY_WISHLIST_BTN).click()
        # time.sleep(1)

    # After accessing product over the "MORE" button,
    # click on the product image to view it in full size
    def click_to_view_large_image(self):
        self.driver.find_element(*ProductPageLocators.LARGE_IMAGE).click()
        time.sleep(2)

    # After clicking on the product image to view it in full size,
    # hover with a mouse, and click the "arrow" button on the right side of the product image four (4) times
    # to scroll images to the right
    # Close the product image by clicking the "X" button of popup window
    def scroll_images_right(self):
        self.driver.find_element(*ProductPageLocators.NEXT_BTN_1).click()
        time.sleep(2)
        self.driver.find_element(*ProductPageLocators.NEXT_BTN_2).click()
        time.sleep(2)
        self.driver.find_element(*ProductPageLocators.NEXT_BTN_3).click()
        time.sleep(2)
        self.driver.find_element(*ProductPageLocators.NEXT_BTN_4).click()
        time.sleep(2)
        self.driver.find_element(*ProductPageLocators.CLOSE_PIC_BTN_N).click()
        time.sleep(2)

    # After clicking on the product image to view it in full size,
    # hover with a mouse, and click the "arrow" button on the left side of the product image four (4) times
    # to scroll images to the left
    # Close the product image by clicking the "X" button of popup window
    def scroll_images_left(self):
        self.driver.find_element(*ProductPageLocators.PREV_BTN_1).click()
        time.sleep(2)
        self.driver.find_element(*ProductPageLocators.PREV_BTN_2).click()
        time.sleep(2)
        self.driver.find_element(*ProductPageLocators.PREV_BTN_3).click()
        time.sleep(2)
        self.driver.find_element(*ProductPageLocators.PREV_BTN_4).click()
        time.sleep(2)
        self.driver.find_element(*ProductPageLocators.CLOSE_PIC_BTN).click()
        time.sleep(2)

    # After accessing product over the "MORE" button, under the Quantity field,
    # click on the plus (+) sign to increase the quantity of chosen product
    def click_plus_to_increase_quantity(self):
        self.driver.find_element(*ProductPageLocators.INCREASE_QUANTITY).click()
        time.sleep(2)

    # After accessing product over the "MORE" button, under the Quantity text,
    # click on the minus (-) sign to decrease the quantity of chosen product
    def click_minus_to_decrease_quantity(self):
        self.driver.find_element(*ProductPageLocators.DECREASE_QUANTITY).click()
        time.sleep(2)

    # After accessing product over the "MORE" button, under the Size text,
    # click on the dropdown menu to choose small (S) size of the chosen product
    def size_small(self):
        self.driver.find_element(*ProductPageLocators.SIZE_SMALL).click()
        time.sleep(2)

    # After accessing product over the "MORE" button, under the Size text,
    # click on the dropdown menu to choose medium (M) size of the chosen product
    def size_medium(self):
        self.driver.find_element(*ProductPageLocators.SIZE_MEDIUM).click()
        time.sleep(2)

    # After accessing product over the "MORE" button, under the Size text,
    # click on the dropdown menu to choose large (L) size of the chosen product
    def size_large(self):
        self.driver.find_element(*ProductPageLocators.SIZE_LARGE).click()
        time.sleep(2)

    # After accessing product over the "MORE" button, under the Color text,
    # click on the blue color box (right box) to blue color for the chosen product
    def click_blue_color_more(self):
        self.driver.find_element(*ProductPageLocators.BLUE_COLOR_MORE).click()
        time.sleep(2)

    # After accessing product over the "MORE" button, under the Color text,
    # click on the orange color box (left box) to orange color for the chosen product
    def click_orange_color_more(self):
        self.driver.find_element(*ProductPageLocators.ORANGE_COLOR_MORE).click()
        time.sleep(2)

    # After accessing product over the "MORE" button,
    # click "Tweet" button to share your chosen product on Twitter and store it
    # in "window_before" variable
    # After clicking "Tweet" button, the new window will open asking you to
    # login to twitter if you are not logged in
    # Now, we tell driver to switch to that new "tweeter" window and close it
    def share_on_twitter(self):
        window_before = self.driver.window_handles[0]
        self.driver.find_element(*ProductPageLocators.TWITTER_SHARE).click()
        time.sleep(2)
        window_after = self.driver.window_handles[1]
        time.sleep(2)
        self.driver.switch_to_window(window_after)
        time.sleep(1)
        self.driver.close()

    # After accessing product over the "MORE" button,
    # click "Share" button to share your chosen product on Facebook and store it
    # in "window_before" variable
    # After clicking "Share" button, the new window will open asking you to
    # login to facebook if you are not logged in
    # Now, we tell driver to switch to that new "facebook" window and close it
    def share_on_facebook(self):
        window_before = self.driver.window_handles[0]
        self.driver.find_element(*ProductPageLocators.FACEBOOK_SHARE).click()
        time.sleep(2)
        window_after = self.driver.window_handles[1]
        time.sleep(2)
        self.driver.switch_to_window(window_after)
        time.sleep(1)
        self.driver.close()

    # After accessing product over the "MORE" button,
    # click "Google+" button to share your chosen product on Google+ and store it
    # in "window_before" variable
    # After clicking "Google+" button, the new window will open asking you to
    # login to Google+ if you are not logged in
    # Now, we tell driver to switch to that new "Google+" window and close it
    def share_on_google_plus(self):
        window_before = self.driver.window_handles[0]
        self.driver.find_element(*ProductPageLocators.GOOGLE_PLUS_SHARE).click()
        time.sleep(2)
        window_after = self.driver.window_handles[1]
        time.sleep(2)
        self.driver.switch_to_window(window_after)
        time.sleep(1)
        self.driver.close()

    # After accessing product over the "MORE" button,
    # click "Pinterest" button to share your chosen product on Pinterest and store it
    # in "window_before" variable
    # After clicking "Pinterest" button, the new window will open asking you to
    # login to Pinterest if you are not logged in
    # Now, we tell driver to switch to that new "Pinterest" window and close it
    def share_on_pinterest(self):
        window_before = self.driver.window_handles[0]
        self.driver.find_element(*ProductPageLocators.PINTEREST_SHARE).click()
        time.sleep(2)
        window_after = self.driver.window_handles[1]
        time.sleep(2)
        self.driver.switch_to_window(window_after)
        time.sleep(1)
        self.driver.close()

    def click_print_product(self):  ## TRIBA SREDIT
        # Find Print button and wait for it to be clickable
        # window_before = self.driver.window_handles[0]
        self.driver.find_element(*ProductPageLocators.PRINT_PRODUCT).click()
        time.sleep(2)
        # window_after = self.driver.window_handles[1]
        # time.sleep(2)
        # self.driver.switch_to_window(window_after)
        time.sleep(1)
        self.driver.find_element(*ProductPageLocators.ClOSE_PRINT).click()
        time.sleep(1)










