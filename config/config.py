import SignInPage
import MainPage
import MyAccountPage
from MainPage import *
from MyAccountPage import *
from WomenPage import *
from OrderPage import *
from ProductPage import *
from ContactUsPage import *
from selenium import webdriver


class Config:

    CHROME_DRIVER = '/Users/nikolarancnik/chromedriver'
    PROJECT_ROOT = "http://automationpractice.com/index.php"

    # THIS IS THE WAY
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER)

    main_page = MainPage(driver)

    account_page = AccountPage(driver)
    women_page = WomenPage(driver)
    orders_page = OrdersPage(driver)
    product_page = ProductPage(driver)
    contact_page = ContactUsPage(driver)
