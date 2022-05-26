from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
  def should_see_empty_basket(self):
		assert self.get_count_books_of_basket() == 0, "There is an item in the basket"
	
	def should_be_not_text_about_empty(self):
		assert self.is_not_element_present(*BasketPageLocators.EMPTY_TEXT), "Text of empty basket is presented"
	
	def should_be_text_about_empty(self):
		assert self.is_element_present(*BasketPageLocators.EMPTY_TEXT), "Text of empty basket is not presented"
