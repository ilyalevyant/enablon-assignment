from selenium.webdriver.chrome import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from dataclasses import dataclass

from test_helpers.config import Config


@dataclass
class DriverFactory():
    config: object = Config()

    def get_driver(self):
        conf = self.config
        driver = webdriver.WebDriver(ChromeDriverManager().install())
        driver.set_window_size(conf.desktop_screen_width, conf.desktop_screen_height)
        driver.implicitly_wait(conf.implicitly_wait)
        return driver
