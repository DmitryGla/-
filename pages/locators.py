from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    #для входа
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    #для регистрации
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")