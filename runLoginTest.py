from selenium import webdriver
from SignInPage import *
from MainPage import *
from MyAccountPage import *
from WomenPage import *
from OrderPage import *
from ProductPage import *
from ContactUsPage import *

PATH = '/Users/nikolarancnik/chromedriver'
PROJECT_URL = "http://automationpractice.com/index.php"

# THIS IS THE WAY
driver = webdriver.Chrome(executable_path=PATH)

main_page = MainPage(driver)
login_form = Login(driver)
account_page = AccountPage(driver)
women_page = WomenPage(driver)
orders_page = OrdersPage(driver)
product_page = ProductPage(driver)
contact_page = ContactUsPage(driver)


def login_test():   # DONE!!!!
    """Tests the login steps using given information"""
    driver.get(PROJECT_URL)  # Go to this website
    time.sleep(1)
    main_page.navigate_to_login_page()  # Call navigate_to_login_page method of main_page class
    time.sleep(1)
    login_form.login()  # Calling class method login() from Login class
    time.sleep(2)   # Pause for 3 seconds
    # driver.quit()   # Close the driver(Chrome)


def login_list_view():  # DONE!!!!
    """Logs in to page, and navigate to women page to click list view button"""
    login_test()
    account_page.navigate_to_list_view()    # Call navigate_to_list_view method of AccountPage class
    time.sleep(2)


def buy_faded_short_sleeve_t_shirt():   # DONE !!!
    """Logs in to page, navigates to women page, clicks list view,
        than it clicks first add to cart button and does the purchase of the chosen product"""
    login_list_view()   # Class method that leads to list view Main page
    women_page.add_to_cart_and_proceed()
    orders_page.proceed_to_checkout()


def add_to_wishlist():  # DONE !!!
    """Logs in to page, navigates to women page, adds the first product to wishlist,
    than navigates to your profile page to your wishlist"""
    login_list_view()
    women_page.add_to_wishlist_and_close_popup()


def write_a_review():   # DONE !!!!
    """Logs in to page, navigates to women page, clicks more button on women page,
    then clicks on write a review, then it populates input fields and sets the product quality to 5"""
    login_list_view()
    women_page.click_on_more_btn()
    product_page.write_a_product_review()


def send_product_to_a_friend():  # DONE !!!!
    """Logs in to page, navigates to women page, clicks more button on women page,
        than clicks on link send to a friend, and populates input fields and clicks send button"""
    login_list_view()
    women_page.click_on_more_btn()
    product_page.send_to_friend()


def pick_blue_color_and_buy():   # DONE !!!!
    """Logs in to page, navigates to women page,click on list view button,
        click or pick blue color of product (tshirt)
            adds product to cart and proceeds to checkout"""
    login_list_view()
    women_page.click_blue_color_before()
    product_page.click_add_to_cart_after_and_proceed()
    orders_page.proceed_to_checkout()


def pick_orange_color_and_buy():   # DONE !!!!
    """Logs in to page, navigates to women page, click list view button,
        click or pick orange color of product (tshirt)
            adds product to cart and proceeds to checkout"""
    login_list_view()
    women_page.click_orange_color_before()
    product_page.click_add_to_cart_after_and_proceed()
    orders_page.proceed_to_checkout()


def click_more_button_and_add_to_wishlist():    # DONE !!!!
    """Logs in to page, navigates to women page, clicks list view button,
        clicks more button of product, than it adds it to wishlist,
            than navigates to your profile to my wishlist"""
    login_list_view()
    women_page.click_on_more_btn()
    product_page.click_add_to_wishlist_after_more()


def scroll_product_image_to_right():    # DONE !!!!
    """Logs in to page, navigates to women page, clicks list view button,
        clicks more button of product, click on the product image,
            swipes it to right and close the picture"""
    login_list_view()
    women_page.click_on_more_btn()
    product_page.click_to_view_large_image()
    product_page.scroll_images_right()


def scroll_product_image_to_left():    # DONE !!!!
    """Logs in to page, navigates to women page, clicks list view button,
        clicks more button of product, click on the product image,
            swipes it to left and close the picture"""
    login_list_view()
    women_page.click_on_more_btn()
    product_page.click_to_view_large_image()
    product_page.scroll_images_left()


def increase_quantity_t_shirt():
    """Logs in to page, navigates to women page, clicks list view button,
        clicks more button of product, than clicks plus (+) sign to
            increase quantity of product"""
    login_list_view()
    women_page.click_on_more_btn()
    product_page.click_plus_to_increase_quantity()


def decrease_quantity_t_shirt():
    """Logs in to page, navigates to women page, clicks list view button,
        clicks more button of product, than clicks minus (-) sign to
            decrease quantity of product"""
    login_list_view()
    women_page.click_on_more_btn()
    product_page.click_minus_to_decrease_quantity()


def small_size_t_shirt():
    """Logs in to page, navigates to women page, clicks list view button,
            clicks more button of product, than chooses size S (small)
                of the product"""
    login_list_view()
    women_page.click_on_more_btn()
    product_page.size_small()


def medium_size_t_shirt():
    """Logs in to page, navigates to women page, clicks list view button,
            clicks more button of product, than chooses size M (medium)
                of the product"""
    login_list_view()
    women_page.click_on_more_btn()
    product_page.size_medium()


def large_size_t_shirt():
    """Logs in to page, navigates to women page, clicks list view button,
            clicks more button of product, than chooses size L (large)
                of the product"""
    login_list_view()
    women_page.click_on_more_btn()
    product_page.size_large()


def pick_orange_color_after_more():
    login_list_view()
    women_page.click_on_more_btn()
    product_page.click_orange_color_more()
    product_page.click_add_to_cart_after_and_proceed()
    orders_page.proceed_to_checkout()


def pick_blue_color_after_more():
    login_list_view()
    women_page.click_on_more_btn()
    product_page.click_blue_color_more()
    product_page.click_add_to_cart_after_and_proceed()
    orders_page.proceed_to_checkout()


def social_media_share_twitter():
    login_list_view()
    women_page.click_on_more_btn()
    product_page.share_on_twitter()


def social_media_share_facebook():
    login_list_view()
    women_page.click_on_more_btn()
    product_page.share_on_facebook()


def social_media_share_google_plus():
    login_list_view()
    women_page.click_on_more_btn()
    product_page.share_on_google_plus()


def social_media_share_pinterest():
    login_list_view()
    women_page.click_on_more_btn()
    product_page.share_on_pinterest()


def print_product():
    login_list_view()
    women_page.click_on_more_btn()
    product_page.click_print_product()


def register_user():
    """Tests the login steps using given information"""
    driver.get(PROJECT_URL)  # Go to this website
    time.sleep(1)
    main_page.navigate_to_login_page()  # Call navigate_to_login_page method of main_page class
    time.sleep(1)
    login_form.enter_email_for_registration()
    time.sleep(2)
    login_form.populate_registration_fields()


def contact_us_send_a_message():
    """"""
    login_test()
    login_form.click_on_contact_us()
    contact_page.populate_a_contact_message_fields()


def search_for_given_term():
    """"""
    driver.get(PROJECT_URL)
    time.sleep(2)
    main_page.search_for_term()

"""OVO JE BIA TEST PROVJERA"""
def login_and_click_order_history():
    """"""
    login_test()
    time.sleep(2)
    account_page.click_order_history_and_details()


if __name__ == "__main__":
    contact_us_send_a_message()

# za zavrist test napravi add_finalizer (tako nekako)
