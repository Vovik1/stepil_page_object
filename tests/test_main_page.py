import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


@pytest.mark.dont_check
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)


@pytest.mark.check_now
def test_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/uk/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
