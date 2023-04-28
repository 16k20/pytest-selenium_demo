from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_FIELD = (
        By.ID,
        'passp-field-login')
    LOGIN_BTN = (
        By.ID,
        'passp:sign-in')
    PASSWORD_FIELD = (
        By.ID,
        'passp-field-passwd')
    PHONE_BTN = (
        By.XPATH,
        "//button[@data-type='phone']")
    PHONE_FIELD = (
        By.ID,
        "passp-field-phone")
    PHONE_HINT = (
        By.ID,
        "field:input-phone:hint")
    ENTRY_HINT = (
        By.ID,
        'field:input-login:hint')
        
class ProfilePageLocators():
    AVATAR = (
        By.CLASS_NAME,
        "UserID-Avatar")
    IFRAME = (
        By.CLASS_NAME,
        "UserWidget-Iframe")
    USERNAME = (
        By.CLASS_NAME,
        "Subname")
