from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME_ALERT_MESSAGE = (By.CSS_SELECTOR, '#messages :nth-child(1) .alertinner')
    PRODUCT_NAME_INSIDE_MESSAGE = (By.CSS_SELECTOR, '#messages :nth-child(1) .alertinner strong')
    PRODUCT_PRICE_ALERT_MESSAGE = (By.CSS_SELECTOR, '#messages :nth-child(3) .alertinner')
    PRODUCT_PRICE_INSIDE_MESSAGE = (By.CSS_SELECTOR, '#messages :nth-child(3) .alertinner strong')