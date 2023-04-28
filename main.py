from .pages.login_page import LoginPage
from .pages.profile_page import ProfilePage
from .pages.dataset import TestLinks, Credentials, TestData
import pytest

#пример позитивного кейса на обычный логин
def test_login_by_login(browser):
    page = LoginPage(browser, TestLinks.LOGIN_LINK)
    page.open()
    page.enter_login()
    page.click_login_button()
    page.enter_password()
    page.click_login_button()
    accpage = ProfilePage(browser, browser.current_url)
    assert accpage.get_username() == Credentials.LOGIN

#пример негативного кейса с параметризацией
@pytest.mark.parametrize("phone_number", TestData.INVALID_PHONES)
def test_incorrect_phone(browser, phone_number):
    page = LoginPage(browser, TestLinks.LOGIN_LINK)
    page.open()
    page.switch_to_phone()
    page.enter_phone_number(phone_number)
    page.click_login_button()
    assert page.get_phone_hint() == 'Недопустимый формат номера'

#еще один типовый негативный кейс
def test_empty_login(browser):
    page = LoginPage(browser, TestLinks.LOGIN_LINK)
    page.open()
    page.click_login_button()
    assert page.get_login_hint() == 'Логин не указан'
    
