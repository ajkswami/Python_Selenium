import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pages_1.launch_driver import Launch


import time

class Test:

    def test_launch(self):
        launch_page = Launch()


        assert "trytestingthis.netlify.app" in launch_page.get_attribute("href")

        time.sleep(2)

        print("Test Passed")








