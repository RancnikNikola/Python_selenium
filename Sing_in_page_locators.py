from selenium.webdriver.common.by import By


# Class for orders page locators
# All Orders page locators are here
class SignInPageLocators:

    SING_IN_TO_PAGE_LOCATOR = (By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')

    USER_EMAIL = "brucewayne@mailinator.com"
    USER_PASSWD = "waynebruce94"

    USER_EMAIL_LOCATOR = (By.NAME, "email")
    USER_PASSWD_LOCATOR = (By.NAME, "passwd")

    SING_IN_LOCATOR = (By.NAME, "SubmitLogin")

    MAIL_FOR_REGISTRATION = 'bane1@mailinator.com'
    EMAIL_REGISTER_INPUT = 'email_create'
    CREATE_AN_ACCOUNT = 'SubmitCreate'

    """CONTACT US"""
    CONTACT_US_BTN = (By.ID, 'contact-link')
