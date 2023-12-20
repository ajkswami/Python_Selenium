import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))



# driver.find_element(By.XPATH, "//legend[@text contains ='title']")
# driver.find_element(By.XPATH, "//label[text()='First name:']")
# driver.find_element(By.XPATH,"//input[@name='fname']")

driver.get("https://www.google.co.in/")
time.sleep(2)

print("yes")

driver.current_window_handle
print("no")

driver.back()
time.sleep(2)
driver.switch_to.new_window()
time.sleep(2)

driver.get("https://www.facebook.com/")
time.sleep(2)

driver.current_window_handle
print("aboo")


driver.forward()
time.sleep(2)

driver.get("https://www.google.co.in/")


driver.back()
time.sleep(2)


driver.refresh()
time.sleep(2)


driver.maximize_window()
time.sleep(2)

driver.minimize_window()
time.sleep(2)

driver.switch_to.new_window()
time.sleep(2)

driver.get("https://www.facebook.com/")
time.sleep(2)

driver.minimize_window()
time.sleep(2)

driver.close()



