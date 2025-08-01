
from pages.AccountSuccessPage import AccountSuccessPage
from pages.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    first_name_field_input_ID = "input-firstname"
    last_name_field_input_ID = "input-lastname"
    email_field_input_ID = "input-email"
    telephone_field_input_ID = "input-telephone"
    password_field_input_ID = "input-password"
    confirm_password_field_input_ID = "input-confirm"
    check_box_field_XPATH = "//input[@type='checkbox']"
    submit_button_XPATH = "//input[@type='submit']"
    warning_message_text_for_first_name_field_XPATH = "//div[@class='text-danger'][text()='First Name must be between 1 and 32 characters!']"

    def enter_text_into_first_name_field(self,first_name):
        self.enter_text_into_element(first_name,"first_name_field_input_ID",self.first_name_field_input_ID)

    def enter_text_into_last_name_field(self,last_name):
        self.enter_text_into_element(last_name, "last_name_field_input_ID", self.last_name_field_input_ID)

    def enter_text_into_email_field(self,email):
        self.enter_text_into_element(email, "email_field_input_ID", self.email_field_input_ID)

    def enter_text_into_telephone_number_field(self,telephone_number):
        self.enter_text_into_element(telephone_number, "telephone_field_input_ID", self.telephone_field_input_ID)

    def enter_text_into_password_field(self,password):
        self.enter_text_into_element(password, "password_field_input_ID", self.password_field_input_ID)

    def enter_text_into_confirm_password_field(self,confirm_password):
        self.enter_text_into_element(confirm_password, "confirm_password_field_input_ID", self.confirm_password_field_input_ID)

    def click_on_the_check_box_field(self):
        self.click_on_element("check_box_field_XPATH",self.check_box_field_XPATH)
        #self.driver.find_element(By.XPATH,self.check_box_field_XPATH).click()

    def click_on_submit_button(self):
        self.click_on_element("submit_button_XPATH", self.submit_button_XPATH)
        #self.driver.find_element(By.XPATH,self.submit_button_XPATH).click()
        return AccountSuccessPage(self.driver)

    def enter_all_fields_to_register(self,first_name,last_name,email,telephone_number,password,confirm_password):
        self.enter_text_into_first_name_field(first_name)
        self.enter_text_into_last_name_field(last_name)
        self.enter_text_into_email_field(email)
        self.enter_text_into_telephone_number_field(telephone_number)
        self.enter_text_into_password_field(password)
        self.enter_text_into_confirm_password_field(confirm_password)
        self.click_on_the_check_box_field()
        return self.click_on_submit_button()

    def warning_message_for_first_name_field(self):
        return self.retrieve_element_text("warning_message_text_for_first_name_field_XPATH",self.warning_message_text_for_first_name_field_XPATH)
        #return self.driver.find_element(By.XPATH,self.warning_message_text_for_first_name_field_XPATH).text

    def verify_warning_message_for_first_name_field(self,expected_warning_message):
        displayed_warning_message = self.warning_message_for_first_name_field()
        return expected_warning_message == displayed_warning_message
