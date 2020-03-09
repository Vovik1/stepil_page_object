from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "You are not on login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "There is no login form on page"
        # реализуйте проверку, что есть форма логина

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "There is no register form on page"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_input.send_keys(email)
        password1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password1.send_keys(password)
        password2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM)
        password2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()

