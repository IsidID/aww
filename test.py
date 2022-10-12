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
import _pytest
import pytest

#NON BROWSER MODE
# options
options = webdriver.ChromeOptions()

#Blink
options.add_argument("--disable-blink-features=AutomationControlled")

#headless mode
options.headless = True
driver = webdriver.Chrome(
#options = options #add "#" before "options" to start test with CHROME
)
# OPEN GO-REMOTE AND LOGIN AS "OLENA PEDASH"
driver.get("https://a-qa-web.azurewebsites.net/go-remote")

#def SignIn():

    print("SIGN IN")
    wait = WebDriverWait(driver, 20)
    SignIn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-landing-layout/app-landing-navbar/nav/div/div[2]/div/button/span[3]")))
    SignIn.click()
    time.sleep(2)
    #SignIn.click()
    #pass
#def mail():
    print("Enter the email data")
    wait = WebDriverWait(driver, 20)
    email = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-landing-layout/app-sign-in/div/form/div[2]/div[3]/div[1]/div/input")))
    email.click()
    email.send_keys("1olena.pedash@awwcor.com")
    time.sleep(2)
    print('.....................................')
    #pass
#def passw():
    print("Enter the password")
    print('.....................................')
    wait = WebDriverWait(driver, 20)
    password = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-landing-layout/app-sign-in/div/form/div[2]/div[3]/div[2]/div/input")))
    password.click()
    password.send_keys("Password1")
    password.send_keys(Keys.RETURN)
    time.sleep(5)
   # pass
#def inf():
    LOGGEDIN = driver.find_element(By.XPATH, "/html/body/app-root/app-board/app-main-layout/app-new-navbar/nav/div/div/button/span[1]/span[1]" or "/html/body/app-root/app-main-layout/app-new-navbar/nav/div/div/button/span[1]/span[1]").text
    try:
        assert 'Company' or 'Customer' or 'Admin' or 'Employee' or 'JobSeeker' in LOGGEDIN
        print("User is LOGGED IN")
    except Exception as e:
        print("TEST FAILED")
        print("User is NOT LOGGED IN", format(e))
    print('.....................................')
    time.sleep(8)
#    pass
#def menucl(): #OPEN MAIN MENU AND CHECKING USER'S ROLE/COMPANY
    mainmenu = driver.find_element(By.XPATH, "/html/body/app-root/app-board/app-main-layout/app-new-navbar/nav/div/div/button/span[1]/span[1]" or "/html/body/app-root/app-main-layout/app-new-navbar/nav/div/div/button/span[1]/span[1]")
    mainmenu.click()
    time.sleep(2)
    driver.switch_to.active_element
    role_title = driver.find_element(By.CLASS_NAME, "manager-role")
    print("Role/Company:")
    print(role_title.text)
    print('.....................................')
    time.sleep(2)
    #
#    pass