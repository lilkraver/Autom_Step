import pytest
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
from pages.base_page import BasePage


initial_url = ProductPageLocators.product_url
urls = [f"{initial_url}/?promo=offer{no}" for no in range(10)]


@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    link = ProductPageLocators.product_url
    page = ProductPage(browser, link)
    page.open()
    page.add_item()