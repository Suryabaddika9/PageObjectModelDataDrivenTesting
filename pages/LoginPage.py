from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    input_email_field_ID = "input-email"
    input_password_field_ID = "input-password"
    login_button_XPATH = "//input[@value='Login']"
    login_verify_message_XPATH = "//div[@id='content']/ul/li/a[text()='Edit your account information']"
    invalid_email_warning_XPATH = "//div[@class='alert alert-danger alert-dismissible']"


    def enter_text_into_email_field(self,email):
        self.enter_text_into_element(email,"input_email_field_ID",self.input_email_field_ID)

    def enter_text_into_password_field(self,password):
        self.enter_text_into_element(password, "input_password_field_ID", self.input_password_field_ID)

    def verify_invalid_email_warning_message(self):
        return self.retrieve_element_text("invalid_email_warning_XPATH",self.invalid_email_warning_XPATH)

    def click_on_login_button(self):
        self.click_on_element("login_button_XPATH",self.login_button_XPATH)

    def verify_login_message_is_displayed(self):
        return self.verify_element_is_displayed("login_verify_message_XPATH",self.login_verify_message_XPATH)

    def enter_login_details(self,email_address,password):
        self.enter_text_into_email_field(email_address)
        self.enter_text_into_password_field(password)
        self.click_on_login_button()

    def verify_invalid_credentials_warning_message(self,expected_warning):
        retrieved_warning = self.verify_invalid_email_warning_message()
        return retrieved_warning.__contains__(expected_warning)






