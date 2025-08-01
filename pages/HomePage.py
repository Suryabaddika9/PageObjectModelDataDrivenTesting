from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage
from pages.SearchPage import SearchPage


class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    search_box_field_NAME = "search"
    search_button_XPATH =  "//button[contains(@class,'btn-default')]"
    my_account_dropdown_XPATH  = "//a[@title='My Account']"
    login_button_LINK_TEXT = "Login"
    register_option_LINK_TEXT = "Register"


    def enter_text_into_search_box_field(self,product_name):
        self.enter_text_into_element(product_name,"search_box_field_NAME",self.search_box_field_NAME)

    def click_on_search_button(self):
        self.click_on_element("search_button_XPATH",self.search_button_XPATH)
        return SearchPage(self.driver)

    def click_on_my_account_dropdown(self):
        self.click_on_element("my_account_dropdown_XPATH", self.my_account_dropdown_XPATH)
        return self.click_on_login_option()

    def click_on_login_option(self):
        self.click_on_element("login_button_LINK_TEXT", self.login_button_LINK_TEXT)
        return LoginPage(self.driver)

    def click_on_register_option(self):
        self.click_on_element("register_option_LINK_TEXT", self.register_option_LINK_TEXT)
        return RegisterPage(self.driver)


