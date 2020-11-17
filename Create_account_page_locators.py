from selenium.webdriver.common.by import By


# Class for orders page locators
# All Orders page locators are here
class CreateAccountPageLocators:

    GENDER_MR = (By.XPATH, '//*[@id="uniform-id_gender1"]/span')
    FIRST_NAME_REGISTER_INPUT = (By.ID, 'customer_firstname')
    FIRST_NAME_REG = 'Bane'
    LAST_NAME_REGISTER_INPUT = (By.ID, 'customer_lastname')
    LAST_NAME_REG = 'Villain'
    PASSWD_REGISTER_INPUT = (By.ID, 'passwd')
    PASSWD_REG = 'darkknight1'
    DAY_BIRTH_DROPDOWN = 'days'
    DAY_BIRTH = (By.XPATH, '//*[@id="days"]/option[11]')
    MONTH_BIRTH = (By.XPATH, '//*[@id="months"]/option[11]')
    YEAR_BIRTH = (By.XPATH, '//*[@id="years"]/option[22]')
    NEWSLETTER_CHECKBOX = 'newsletter'
    SPECIAL_OFFERS_CHECKBOX = 'optin'

    COMPANY_REG_INPUT = (By.ID, 'company')
    COMPANY_REG_INPUT_TXT = 'DC'

    ADDRESS_1_REG_INPUT = (By.ID, 'address1')
    ADDRESS_1_REG_INPUT_TXT = 'Gotham street 10'

    ADDRESS_2_REG_INPUT = (By.ID, 'address2')
    ADDRESS_2_REG_INPUT_TXT = 'Unknown'

    CITY_REG_INPUT = (By.ID, 'city')
    CITY_REG_INPUT_TXT = 'Gotham'

    STATE_REG = (By.XPATH, '//*[@id="id_state"]/option[34]')

    ZIP_CODE_REG_INPUT = (By.ID, 'postcode')
    ZIP_CODE_REG_INPUT_TXT = '53540'

    COUNTRY_REG = (By.XPATH, '//*[@id="id_country"]/option[2]')

    ADDITIONAL_INFO_TEXTAREA_REG = (By.ID, 'other')
    ADDITIONAL_INFO_TEXTAREA_REG_TXT = 'Best villain ever'
    HOME_PHONE_REG_INPUT = (By.ID, 'phone')
    HOME_PHONE_REG_INPUT_NUM = '1234567890'
    MOBILE_PHONE_REG_INPUT = (By.ID, 'phone_mobile')
    MOBILE_PHONE_REG_INPUT_NUM = '0987654321'
    ALIAS_ADDRESS_REG_INPUT = (By.ID, 'alias')
    ALIAS_ADDRESS_REG_INPUT_TXT = 'Additional address'

    REGISTER_BTN = (By.ID, 'submitAccount')