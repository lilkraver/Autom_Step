import pytest
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
from pages.base_page import BasePage


#initial_url = ProductPageLocators.product_url
#urls = [f"{initial_url}/?promo=offer{no}" for no in range(10)]

#@pytest.mark.parametrize('link', urls)
#def test_guest_can_add_product_to_basket(browser, link):
    #link = ProductPageLocators.product_url
    
@pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_item()
    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_for_tree_tests)
    page.open()
    #page.should_be_product_page()
    page.add_item()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link_for_tree_tests)
    page.open()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_for_tree_tests)
    page.open()
    #page.should_be_product_page()
    page.add_item()
    page.should_disappeared_success_message()
    
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_see_empty_basket()
    basket_page.should_be_text_about_empty()
