import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# Initialize Chrome WebDriver

class Launch:

    def __init__(self):
        self.driver = None


    def launch_browser(self):
        Chrome_driver_path = ChromeDriverManager().install()

        service = ChromeService(Chrome_driver_path)

        self.driver = webdriver.Chrome(service=service)

        # Open Google and wait for 3 seconds
        self.driver.get("https://www.google.com")
        time.sleep(3)

        googleSearch = self.driver.find_element(By.ID, "APjFqb")
        time.sleep(2)
        googleSearch.send_keys("https://trytestingthis.netlify.app/")
        main_url = "https://trytestingthis.netlify.app/"
        time.sleep(2)
        googleSearch.send_keys(Keys.RETURN)
        time.sleep(3)

        target_url = self.driver.find_element(By.XPATH, "//*[@class='GTRloc']")
        time.sleep(2)

        target_url.click()
        time.sleep(2)

        print("Test Done")

        return target_url

launch_instance =Launch()

target_url = launch_instance.launch_browser()


launch_instance.driver.quit()



