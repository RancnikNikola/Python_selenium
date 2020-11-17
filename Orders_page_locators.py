from selenium.webdriver.common.by import By


# Class for orders page locators
# All Orders page locators are here
class OrdersPageLocators:

    PROCEED_TO_CHECKOUT_BTN_2 = (By.XPATH, '//*[@id="center_column"]/p[2]/a[1]')
    PROCEED_TO_CHECKOUT_BTN_3 = (By.XPATH, '//*[@id="center_column"]/form/p/button')
    PROCEED_TO_CHECKOUT_BTN_4 = (By.XPATH, '//*[@id="form"]/p/button')

    TEXTAREA_MSG = (By.NAME, 'message')
    COMMENT_MSG = "This is my comment about this order"

    TERMS_OF_SERVICE_OPEN = (By.XPATH, '//*[@id="form"]/div/p[2]/a')
    TERMS_OF_SERVICE_CLOSE = (By.XPATH, '//*[@id="order"]/div[2]/div/div/a')
    TERMS_CHECKBOX = (By.XPATH, '//*[@id="uniform-cgv"]/span')

    BANK_WIRE_BTN = (By.XPATH, '//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a')
    CONFIRM_ORDER_BTN = (By.XPATH, '//*[@id="cart_navigation"]/button')