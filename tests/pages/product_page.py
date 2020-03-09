from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_busket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def check_alert_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_ALERT_MESSAGE)
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_ALERT_MESSAGE)

    def check_text_inside_alert(self, name, price):
        assert name == self.text_inside_element(*ProductPageLocators.PRODUCT_NAME_INSIDE_MESSAGE)
        assert price == self.text_inside_element(*ProductPageLocators.PRODUCT_PRICE_INSIDE_MESSAGE)

    def should_not_be_success_message(self):
        """Success message is presented, but should not be"""
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_PRICE_ALERT_MESSAGE)

    def should_element_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_PRICE_ALERT_MESSAGE)


