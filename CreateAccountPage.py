# Import what is needed
import time
from Create_account_page_locators import CreateAccountPageLocators


# Class for Sign in page
class CreateAccountPage:
    def __init__(self, driver):
        self.driver = driver

    # MOGLO BI SE ODVOJIT PERSONAL INFO I YOUR ADDRESS INFO
    """FIELDS FOR "YOUR PERSONAL INFORMATION"""
    # In title radio buttons, click on Mr. radio button
    # In "First name" input field, type in your First name
    # In "Last name" input field, type in your Last name
    # Email field is already populated with the email address that you used to create an account
    # In the "Password" input field, type in your password you want to register with
    # There are three (3) dropdowns under the Date of Birth (Day, Month, Year)
    # For the first dropdown (Day) choose any day, I chose ten (10)
    # For the second dropdown (Month) choose any month, I chose (10)
    # And for the third dropdown (Year) choose any year, I chose (2000)
    # Click "Sign up for our newsletter!" checkbox
    # Click "Receive special offers from our partners!" checkbox

    """FIELDS FOR "YOUR ADDRESS"""
    # "First name" and "Last name" input fields are already populated with your first and last name
    # In the "Company" input field, type in your company name, I chose "DC"
    # In the "Address" input field, type in your address, I chose "Gotham street 10"
    # In the "Address (Line 2)" input field, type in your second address, I chose "unknown"
    # In the "City" input field, type in your city, I chose "Gotham"
    # In the "State" dropdown menu, choose you state, I chose "North Dakota", its value is 34
    # In the "Zip/Postal Code" input field, enter you postal code, I chose "53540"
    # In the "Country" dropdown menu, choose your country, I chose "United States"
    # In the "Additional information" textarea field, type any in additional information, I chose "Best villain ever"
    # In the "Home phone" input field, enter your Home phone number, I chose "1234567890"
    # In the "Mobile phone" input field, enter your Mobile phone number, I chose "0987654321"
    # In the "Assign an address alias for future reference" input field, there is already some text
    # which is "My address",
    # Clear "Assign an address alias for future reference" input field and write in your alias address,
    # I chose "Additional address"
    # Now to finish registration click on "Register" button
    def populate_registration_fields(self):
        self.driver.find_element(*CreateAccountPageLocators.GENDER_MR).click()
        time.sleep(1)
        self.driver.find_element(*CreateAccountPageLocators.FIRST_NAME_REGISTER_INPUT).send_keys \
            (*CreateAccountPageLocators.FIRST_NAME_REG)
        time.sleep(2)
        self.driver.find_element(*CreateAccountPageLocators.LAST_NAME_REGISTER_INPUT).send_keys(*CreateAccountPageLocators.LAST_NAME_REG)
        time.sleep(2)
        self.driver.find_element(*CreateAccountPageLocators.PASSWD_REGISTER_INPUT).send_keys(*CreateAccountPageLocators.PASSWD_REG)
        time.sleep(2)
        self.driver.find_element(*CreateAccountPageLocators.DAY_BIRTH).click()
        time.sleep(1)
        self.driver.find_element(*CreateAccountPageLocators.MONTH_BIRTH).click()
        time.sleep(1)
        self.driver.find_element(*CreateAccountPageLocators.YEAR_BIRTH).click()
        time.sleep(1)
        self.driver.find_element(*CreateAccountPageLocators.NEWSLETTER_CHECKBOX).click()
        time.sleep(1)
        self.driver.find_element(*CreateAccountPageLocators.SPECIAL_OFFERS_CHECKBOX).click()
        time.sleep(1)

        self.driver.find_element(*CreateAccountPageLocators.COMPANY_REG_INPUT).send_keys(*CreateAccountPageLocators.COMPANY_REG_INPUT_TXT)
        time.sleep(2)
        self.driver.find_element(*CreateAccountPageLocators.ADDRESS_1_REG_INPUT).send_keys \
            (*CreateAccountPageLocators.ADDRESS_1_REG_INPUT_TXT)
        time.sleep(2)
        self.driver.find_element(*CreateAccountPageLocators.ADDRESS_2_REG_INPUT).send_keys \
            (*CreateAccountPageLocators.ADDRESS_2_REG_INPUT_TXT)
        time.sleep(2)
        self.driver.find_element(*CreateAccountPageLocators.CITY_REG_INPUT).send_keys(*CreateAccountPageLocators.CITY_REG_INPUT_TXT)
        time.sleep(2)
        self.driver.find_element(*CreateAccountPageLocators.STATE_REG).click()
        time.sleep(2)
        self.driver.find_element(*CreateAccountPageLocators.ZIP_CODE_REG_INPUT).send_keys \
            (*CreateAccountPageLocators.ZIP_CODE_REG_INPUT_TXT)
        time.sleep(2)
        self.driver.find_element(*CreateAccountPageLocators.COUNTRY_REG).click()
        time.sleep(2)
        self.driver.find_element(*CreateAccountPageLocators.ADDITIONAL_INFO_TEXTAREA_REG).send_keys \
            (*CreateAccountPageLocators.ADDITIONAL_INFO_TEXTAREA_REG_TXT)
        time.sleep(2)
        self.driver.find_element(*CreateAccountPageLocators.HOME_PHONE_REG_INPUT).send_keys \
            (*CreateAccountPageLocators.HOME_PHONE_REG_INPUT_NUM)
        time.sleep(2)
        self.driver.find_element(*CreateAccountPageLocators.MOBILE_PHONE_REG_INPUT).send_keys \
            (*CreateAccountPageLocators.MOBILE_PHONE_REG_INPUT_NUM)
        time.sleep(2)
        self.driver.find_element(*CreateAccountPageLocators.ALIAS_ADDRESS_REG_INPUT).clear()
        time.sleep(2)
        self.driver.find_element(*CreateAccountPageLocators.ALIAS_ADDRESS_REG_INPUT).send_keys \
            (*CreateAccountPageLocators.ALIAS_ADDRESS_REG_INPUT_TXT)
        time.sleep(2)
        self.driver.find_element(*CreateAccountPageLocators.REGISTER_BTN).click()
        time.sleep(2)