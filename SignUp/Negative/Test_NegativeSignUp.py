import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
import pyautogui
import keyboard
from selenium.webdriver.support import select
from selenium.webdriver.support import wait
from selenium.webdriver.common import alert

# NON BROWSER MODE
# options
options = webdriver.ChromeOptions()

# Blink
options.add_argument("--disable-blink-features=AutomationControlled")

# headless mode
options.headless = True
driver = webdriver.Chrome('C:/Users/isid/PycharmProjects/aww/chromedriver.exe',
                          options=options  # add "#" before "options" to start test with CHROME
                          )
actions = ActionChains(driver)
driver.maximize_window()
driver.implicitly_wait(30)
# OPEN GO-REMOTE AND LOGIN AS "OLENA PEDASH"
driver.get("https://a-qa-web.azurewebsites.net/go-remote")
