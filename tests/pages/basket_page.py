from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def check_if_empty(self):
        empty_basket_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text
        assert empty_basket_text == "Your basket is empty. Continue shopping", "Basket is not empty"

    def should_not_be_checkout_button(self):
        assert self.is_not_element_present(*BasketPageLocators.CHECKOUT_BUTTON, timeout=0.5)

