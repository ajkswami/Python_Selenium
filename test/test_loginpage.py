import time

import requests
from bs4 import BeautifulSoup

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

from test.pages.login_page import LoginPage







@pytest.fixture()



def driver():


    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()



def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_page("https://trytestingthis.netlify.app/")
    time.sleep(2)
    login_page.enter_username("test")
    time.sleep(2)
    login_page.enter_password("test")
    time.sleep(2)
    login_page.click_button()
    time.sleep(2)

    return test_login


def test_sucess(driver):
    url = "https://trytestingthis.netlify.app/login.html?uname=test&pwd=test"


    r = requests.get(url)




    soup = BeautifulSoup(r.text, "html.parser")

    h2_tag = soup.find("h2", text="Login Successful :) ")



    assert h2_tag is not None, "Login not found"

    print("Login Successful message found!")


def test_homepage_heading():


    url = "https://trytestingthis.netlify.app/login.html?uname=test&pwd=test"

    r = requests.get(url)



    soup = BeautifulSoup(r.text, "html.parser")


    h1_tag = soup.find("h1", text="Your Website to practice Automation Testing")



    # Assert that the homepage heading is present in the HTML content
    assert h1_tag is not None, "Homepage heading not found"






