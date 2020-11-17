from selenium.webdriver.common.by import By


# Class for Main page locators
# All Main page locators are here
class MainPageLocators:

    SING_IN_TO_PAGE_LOCATOR = (By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
    SEARCH_INPUT = (By.ID, 'search_query_top')
    SEARCH_TERM = 'T shirt'
    SEARCH_BTN = (By.NAME, 'submit_search')

    NAVBAR_WOMEN_BTN = (By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a')
    NAVBAR_DRESSES_BTN = (By.XPATH, '//*[@id="block_top_menu"]/ul/li[2]/a')
    NAVBAR_T_SHIRT_BTN = (By.XPATH, '//*[@id="block_top_menu"]/ul/li[3]/a')

    CONTACT_US_BTN = (By.ID, 'contact-link')
    SIGN_OUT_BTN = (By.ID, 'header_user_info')
    SIGN_IN_BTN = (By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
    MY_PROFILE_BTN = (By.ID, 'header_user_info')

    

