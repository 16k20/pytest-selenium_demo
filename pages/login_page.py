from .base_page import BasePage
from .dataset import Credentials
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def enter_login(self):
        field = self.find_element(*LoginPageLocators.LOGIN_FIELD)
        field.send_keys(Credentials.LOGIN)
        
    def click_login_button(self):
        button = self.find_element(*LoginPageLocators.LOGIN_BTN)
        button.click()
    
    def enter_password(self):
        field = self.find_element(*LoginPageLocators.PASSWORD_FIELD)
        field.send_keys(Credentials.PASSWORD)

    def switch_to_phone(self):
        button = self.find_element(*LoginPageLocators.PHONE_BTN)
        button.click()
        
    def enter_phone_number(self, phone):
        field = self.find_element(*LoginPageLocators.PHONE_FIELD)
        field.clear()
        field.send_keys(phone)
        
    def get_phone_hint(self):
        hint = self.find_element(*LoginPageLocators.PHONE_HINT)
        return hint.text

    def get_login_hint(self):
        hint = self.find_element(*LoginPageLocators.ENTRY_HINT)
        return hint.text
