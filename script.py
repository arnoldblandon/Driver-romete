import sys
from time import sleep
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from scrapers.scraper import get_driver, connect_to_base, parse_html

#profile = webdriver.FirefoxProfile()
#profile.set_preference("dom.max_script_run_time", 2600)
#profile.set_preference("dom.max_chrome_script_run_time", 2600)

driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX)


driver.get("https://sandbox.secure.payulatam.com/login.zul")
# login
driver.find_element_by_xpath(
    "//*[@name='j_username']").send_keys("")
driver.find_element_by_xpath(
    "//*[@name='j_password']").send_keys("")
driver.find_element_by_xpath(
    "//input[@id='btnenviar']").click()

print("click en Transfers")
# click text Transfers
try:
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((
            By.XPATH, "//*[contains(text(),'Transfers')]")))
except:
    pass
driver.save_screenshot("test.png")