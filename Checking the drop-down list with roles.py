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
import unittest

# options
options = webdriver.ChromeOptions()

#Blink
options.add_argument("--disable-blink-features=AutomationControlled")

#headless mode
options.headless = True
driver = webdriver.Chrome(
options = options
)

driver.get("https://a-qa-web.azurewebsites.net/go-remote")
print("SignIn button click")
wait = WebDriverWait(driver, 10)
SignIn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-landing-layout/app-landing-navbar/nav/div/div[3]/button")))
SignIn.click()
print("Done")
time.sleep(1)
print('====================================================================================')
print("Enter the email data")
email = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-landing-layout/app-sign-in/div/form/div[2]/div[1]/input")))
email.click
email.send_keys("1olena.pedash@awwcor.com")
print("Done")
print('====================================================================================')
print("Enter the password")
password = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-landing-layout/app-sign-in/div/form/div[2]/div[2]/input")))
password.click()
password.send_keys("Password1")
password.send_keys(Keys.RETURN)
print("Done")
print('====================================================================================')
print("LogIn")
#wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-landing-layout/app-sign-in/div/form/div[4]/button"))).click()
print("LogIn Done")
print('====================================================================================')
time.sleep(8)
print("Open Main Menu")
mainmenu = driver.find_element(By.XPATH, "/html/body/app-root/app-board/app-main-layout/app-new-navbar/nav/div/div/button/span[1]/span[1]")
mainmenu.click()
time.sleep(2)
driver.switch_to.active_element
role_title = driver.find_element(By.CLASS_NAME, "manager-role")
print("Role/Company:")
print(role_title.text)
print("Done")
print('====================================================================================')
time.sleep(2)
print("Choosing Admin Role")
#focus = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div[3]/div[2]/div[1]/img")
#focus.driver.switch_to.active_element
#focus.click()
adminrole = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[3]/div[1]")
adminrole.click()
adminrole2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#mat-menu-panel-0 > div > div.level-select__wrap.btn-shadow.ng-tns-c218-2 > div:nth-child(1) > div.level-select__title.ng-star-inserted.show-more")))
adminrole2.click()
print("Role/Company:")
print(role_title.text)
print("Admin Role Choosed")
print('====================================================================================')




time.sleep(5)
driver.quit()
