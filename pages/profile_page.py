from .base_page import BasePage
from .locators import ProfilePageLocators

class ProfilePage(BasePage):
    def get_username(self):
        avatar = self.find_element(*ProfilePageLocators.AVATAR)
        avatar.click()
        self.change_frame(*ProfilePageLocators.IFRAME)
        username = self.find_element(*ProfilePageLocators.USERNAME)
        return username.text
