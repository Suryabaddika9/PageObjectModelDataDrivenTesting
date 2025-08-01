from datetime import datetime

import pytest


@pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
class BaseTest:

    def timestamp_email_generator(self):
        timestamp = datetime.now()
        timestamp = timestamp.strftime("%Y%m%d_%H%M%S")
        return "Surya" + timestamp + "@gmail.com"