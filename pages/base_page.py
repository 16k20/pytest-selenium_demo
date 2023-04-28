from selenium.common.exceptions import NoSuchElementException

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        
    def open(self):
        self.browser.get(self.url)
        
    def find_element(self, how, what):
        try:
            return self.browser.find_element(how, what)
        except NoSuchElementException:
            return None
    def change_frame(self, how, what):
        return self.browser.switch_to.frame(self.find_element(how, what))
