from selenium.webdriver.common.by import By


# Class for Product page locators
# All Product page locators are here
class ProductPageLocators:
    WRITE_REVIEW_LINK = (By.XPATH, '//*[@id="product_comments_block_extra"]/ul/li/a')
    STAR_QUALITY_5 = (By.XPATH, '//*[@id="criterions_list"]/li/div[1]/div[6]')

    REVIEW_TITLE_INPUT = (By.NAME, "title")
    REVIEW_TITLE = "This is the way"

    REVIEW_COMMENT_INPUT = (By.NAME, 'content')
    REVIEW_COMMENT = 'This is the review comment'

    SEND_REVIEW_BTN = (By.ID, "submitNewMessage")
    OK_REVIEW_BTN = (By.XPATH, '//*[@id="product"]/div[2]/div/div/div/p[2]/button')

    SEND_TO_FRIEND = (By.XPATH, '//*[@id="send_friend_button"]')
    FRIEND_NAME_INPUT = (By.NAME, 'friend_name')
    FRIEND_NAME = "Jane Doe"

    FRIEND_EMAIL_INPUT = (By.NAME, 'friend_email')
    FRIEND_EMAIL = "Janedoe@unknown.com"

    FRIEND_SEND_BTN = (By.NAME, 'sendEmail')
    OK_BUTTON = (By.XPATH, '//*[@id="product"]/div[2]/div/div/div/p[2]/input')

    ADD_TO_CART_AFTER = (By.XPATH, '//*[@id="add_to_cart"]/button')

    PROCEED_TO_CHECKOUT_BTN_1 = (By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a')

    ADD_TO_WISHLIST_MORE = (By.XPATH, '//*[@id="wishlist_button"]')
    ADD_TO_WISHLIST_MORE_CLOSE = (By.XPATH, '//*[@id="product"]/div[2]/div/div/a')

    USERS_PROFILE_BTN = (By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
    MY_WISHLIST_BTN = (By.XPATH, '//*[@id="center_column"]/div/div[2]/ul/li/a')

    NEXT_BTN_1 = (By.XPATH, '//*[@id="product"]/div[2]/div/div[1]/a[2]')
    NEXT_BTN_2 = (By.XPATH, '//*[@id="product"]/div[2]/div/div/div[1]/a[2]')
    NEXT_BTN_3 = (By.XPATH, '//*[@id="product"]/div[2]/div/div/div[1]/a[2]')
    NEXT_BTN_4 = (By.XPATH, '//*[@id="product"]/div[2]/div/div/div[1]/a[2]')
    CLOSE_PIC_BTN_N = (By.XPATH, '//*[@id="product"]/div[2]/div/div/a')

    LARGE_IMAGE = (By.XPATH, '//*[@id="view_full_size"]')

    PREV_BTN_1 = (By.XPATH, '//*[@id="product"]/div[2]/div/div[1]/a[1]')
    PREV_BTN_2 = (By.XPATH, '//*[@id="product"]/div[2]/div/div/div[1]/a[1]')
    PREV_BTN_3 = (By.XPATH, '//*[@id="product"]/div[2]/div/div/div[1]/a[1]')
    PREV_BTN_4 = (By.XPATH, '//*[@id="product"]/div[2]/div/div/div[1]/a[1]')
    CLOSE_PIC_BTN = (By.XPATH, '//*[@id="product"]/div[2]/div/div/a')

    INCREASE_QUANTITY = (By.XPATH, '//*[@id="quantity_wanted_p"]/a[2]')
    DECREASE_QUANTITY = (By.XPATH, '//*[@id="quantity_wanted_p"]/a[1]/span')

    SIZE_SMALL = (By.XPATH, '//*[@id="group_1"]/option[1]')
    SIZE_MEDIUM = (By.XPATH, '//*[@id="group_1"]/option[2]')
    SIZE_LARGE = (By.XPATH, '//*[@id="group_1"]/option[3]')

    BLUE_COLOR_MORE = (By.NAME, 'Blue')
    ORANGE_COLOR_MORE = (By.NAME, 'Orange')

    TWITTER_SHARE = (By.XPATH, '//*[@id="center_column"]/div/div/div[3]/p[7]/button[1]')
    FACEBOOK_SHARE = (By.XPATH, '//*[@id="center_column"]/div/div/div[3]/p[7]/button[2]')
    GOOGLE_PLUS_SHARE = (By.XPATH, '//*[@id="center_column"]/div/div/div[3]/p[7]/button[3]')
    PINTEREST_SHARE = (By.XPATH, '//*[@id="center_column"]/div/div/div[3]/p[7]/button[4]')

    PRINT_PRODUCT = (By.XPATH, '//*[@id="usefull_link_block"]/li[2]/a')
    ClOSE_PRINT = (By.XPATH, '//*[@id="sidebar"]//print-preview-button-strip//div/cr-button[1]')