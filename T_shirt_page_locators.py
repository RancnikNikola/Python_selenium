from selenium.webdriver.common.by import By


# Class for Main page locators
# All Main page locators are here
class TshirtsPageLocators:

    QUICK_VIEW_BTN = (By.XPATH, '//*[@id="center_column"]/ul/li/div/div/div[1]/div/a[2]')
    ADD_TO_COMPARE_BTN = (By.XPATH, '//*[@id="center_column"]/ul/li/div/div/div[3]/div/div[3]/div[2]/a')

    ADD_TO_CART = (By.XPATH, '//*[@id="add_to_cart"]/button')

    ADD_TO_WISHLIST_MORE = (By.XPATH, '//*[@id="wishlist_button"]')
    ADD_TO_WISHLIST_MORE_CLOSE = (By.XPATH, '//*[@id="product"]/div[2]/div/div/a')

    BLUE_COLOR_MORE = (By.NAME, 'Blue')
    ORANGE_COLOR_MORE = (By.NAME, 'Orange')

    PRODUCT_MORE_BTN = (By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div/div[3]/div/div[2]/a[2]')

    SORT_BY_DROPDOWN = (By.ID, 'selectProductSort')
    COMPARE_BTN = (By.XPATH, '//*[@id="center_column"]/div[3]/div/form/button')

    LIST_VIEW_BTN = ''
    GRID_VIEW_BTN = ''
