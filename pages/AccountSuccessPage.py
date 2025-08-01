from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class AccountSuccessPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    account_success_message_XPATH = "//div[@id='content']/h1"

    def verify_account_success_message(self):
        return self.retrieve_element_text("account_success_message_XPATH",self.account_success_message_XPATH)

    def verify_account_success_message_is_present(self,expected_text):
        retrieved_text = self.verify_account_success_message()
        return retrieved_text == expected_text
