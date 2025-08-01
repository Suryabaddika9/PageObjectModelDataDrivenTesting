from datetime import datetime
import pytest
from openpyxl.reader.excel import ExcelReader

from Tests.BaseTest import BaseTest
from pages.HomePage import HomePage
from utilities import ExcelReaderUtils


class TestRegister(BaseTest):
    driver = None
    def test_register_with_mandate_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_dropdown()
        register_page = home_page.click_on_register_option()
        account_success_page = register_page.enter_all_fields_to_register(ExcelReaderUtils.get_cell_data("ExcelFiles/Tutorial.xlsx","TestRegister",2,1),
                                                                          ExcelReaderUtils.get_cell_data("ExcelFiles/Tutorial.xlsx","TestRegister",2,2),
                                                                          self.timestamp_email_generator(), "1234567890", "123456", "123456")
        assert account_success_page.verify_account_success_message_is_present("Your Account Has Been Created!")

    def test_register_without_mandate_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_dropdown()
        register_page = home_page.click_on_register_option()
        register_page.enter_all_fields_to_register("", "", "", "", "", "")
        assert register_page.verify_warning_message_for_first_name_field("First Name must be between 1 and 32 characters!")


