import pytest

from pages.main_page import MainPage
from test_helpers.config import Config
from test_helpers.constants import TASK_NAME
from test_helpers.driver_factory import DriverFactory


@pytest.fixture
def browser(conf):
    driver_factory = DriverFactory(conf)
    driver = driver_factory.get_driver()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(browser, conf):
    browser.get(conf.service_endpoint)
    return MainPage(browser)


@pytest.fixture
def conf():
    config = Config()
    return config


@pytest.fixture
def add_task(main_page):
    main_page.add_task(TASK_NAME)