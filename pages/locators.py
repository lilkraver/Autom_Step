from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    product_url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    b_button = (By.CSS_SELECTOR, '#add_to_basket_form [type="submit"]')
    item_name = (By.CSS_SELECTOR, '.row h1')
     
    item_bname = (By.CSS_SELECTOR, '.alertinner>strong')
    item_price = (By.CSS_SELECTOR, 'p.price_color')
    total_price = (By.CLASS_NAME, '.alertinner p strong')
