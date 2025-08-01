import time
from datetime import datetime

import pytest
from openpyxl.reader.excel import ExcelReader
from selenium.webdriver.common.by import By

from Tests.BaseTest import BaseTest
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from utilities import ExcelReaderUtils


class TestLogin(BaseTest):
    driver = None
    @pytest.mark.parametrize("email_address,password",ExcelReaderUtils.get_data_from_excel("ExcelFiles/Tutorial.xlsx","TestLogin"))
    def test_login_with_valid_credentials(self,email_address,password):
        home_page = HomePage(self.driver)
        login_page = home_page.click_on_my_account_dropdown()
        login_page.enter_login_details(email_address,password)
        time.sleep(2)
        assert login_page.verify_login_message_is_displayed()

    def test_login_with_invalid_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.click_on_my_account_dropdown()
        login_page.enter_login_details(self.timestamp_email_generator(), "Surya690@")
        assert login_page.verify_invalid_credentials_warning_message("Warning: No match for E-Mail Address and/or Password.....")




