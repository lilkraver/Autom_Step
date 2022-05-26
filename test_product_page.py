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
