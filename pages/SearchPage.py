from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    valid_hp_product_LINK_TEXT = "HP LP3065"
    no_product_warning_msg_XPATH = "//input[@id='button-search']/following-sibling::p"

    def display_status_of_product(self):
        self.verify_element_is_displayed("valid_hp_product_LINK_TEXT",self.valid_hp_product_LINK_TEXT)

    def retrieve_no_product_msg(self):
        return self.retrieve_element_text("no_product_warning_msg_XPATH",self.no_product_warning_msg_XPATH)