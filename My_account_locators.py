from selenium.webdriver.common.by import By


# Class for my account page locators
# All My account page locators are here
class MyAccountPageLocators:

    WOMEN_NAVBAR = (By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a')
    LIST_VIEW_BTN = (By.XPATH, '//*[@id="list"]/a')
    ORDER_HISTORY_AND_DETAILS = (By.XPATH, '//*[@id="center_column"]/div/div[1]/ul/li[1]/a')
    BACK_TO_ACC = (By.XPATH, '//*[@id="center_column"]/ul/li[1]/a')
    CREDIT_SLIPS = (By.XPATH, '//*[@id="center_column"]/div/div[1]/ul/li[2]/a')
    MY_ADDRESSES = (By.XPATH, '//*[@id="center_column"]/div/div[1]/ul/li[3]/a')
    MY_PERSONAL_INFORMATION = (By.XPATH, '//*[@id="center_column"]/div/div[1]/ul/li[4]/a')
    MY_WISHLIST = (By.XPATH, '//*[@id="center_column"]/div/div[2]/ul/li/a')
