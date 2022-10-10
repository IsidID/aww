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
actions = ActionChains(driver)
# OPEN GO-REMOTE AND LOGIN AS "OLENA PEDASH"
driver.get("https://a-qa-web.azurewebsites.net/go-remote")
print("LogIn")
wait = WebDriverWait(driver, 10)
SignIn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-landing-layout/app-landing-navbar/nav/div/div[2]/div/button/span[1]")))
SignIn.click()
time.sleep(2)
email = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-landing-layout/app-sign-in/div/form/div[2]/div[3]/div[1]/div/input")))
email.click()
email.send_keys("1olena.pedash@awwcor.com")
time.sleep(2)
password = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-landing-layout/app-sign-in/div/form/div[2]/div[3]/div[2]/div/input")))
password.click()
password.send_keys("Password1")
password.send_keys(Keys.RETURN)
time.sleep(5)
LOGGEDIN = driver.find_element(By.XPATH, "/html/body/app-root/app-board/app-main-layout/app-new-navbar/nav/div/div/button/span[1]/span[1]" and "/html/body/app-root/app-main-layout/app-new-navbar/nav/div/div/button/span[1]/span[1]").text
try:
    assert 'Company' or 'Customer' or 'Admin' or 'Employee' or 'JobSeeker' in LOGGEDIN
    print("User is Logged In")
except Exception as e:
    print("TEST FAILED")
    print("User is NOT LOGGED IN", format(e))
time.sleep(8)

#OPEN MAIN MENU AND CHECKING USER'S ROLE/COMPANY
mainmenu = driver.find_element(By.XPATH, "/html/body/app-root/app-board/app-main-layout/app-new-navbar/nav/div/div/button/span[1]/span[1]" and "/html/body/app-root/app-main-layout/app-new-navbar/nav/div/div/button/span[1]/span[1]")
mainmenu.click()
time.sleep(2)
driver.switch_to.active_element
role_title = driver.find_element(By.CLASS_NAME, "manager-role")
print("Role/Company:")
print(role_title.text)
print("Current url:", driver.current_url)

time.sleep(2)
#


print("Switch to JobSeeker role")
JobSeekerrole = driver.find_element(By.XPATH, "//*[@id='mat-menu-panel-0']/div/div[3]/div[5]/div[1]/span")
JobSeekerrole.click()
JobSeekerrole2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mat-menu-panel-0']/div/div[3]/div[5]/div[2]")))
JobSeekerrole2.click()
time.sleep(5)
JobSeekerroletitle = driver.find_element(By.XPATH, "/html/body/app-root/app-main-layout/app-new-navbar/nav/div/div/button/span[1]/span[1]" and "/html/body/app-root/app-board/app-main-layout/app-new-navbar/nav/div/div/button/span[1]/span[1]").text
try:
    assert 'JobSeeker' in JobSeekerroletitle
    print("Test passed. Current role:", JobSeekerroletitle)
    print("Current url:", driver.current_url)
except Exception as e:
    print("TEST FAILED. Curent role:", JobSeekerroletitle, format(e))
    print("Current url:", driver.current_url)

time.sleep(3)
#
print("Create a new profile")
createbutton = driver.find_element(By.XPATH, "/html/body/app-root/app-board/app-main-layout/app-dashboard-page/div/div/app-profiles-dashboard/div[2]/app-search-block/div[1]/a/span[1]/span")
createbutton.click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/app-root/app-board/app-main-layout/app-profile-form-page-update/div/form/div[1]/div[1]/input").send_keys("AutoTestPosition")
driver.find_element(By.XPATH, "//*[@id='mat-select-value-7']/span/span").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/mat-option[2]/span").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/app-root/app-board/app-main-layout/app-profile-form-page-update/div/form/div[1]/div[2]/div[2]/input").send_keys("45")
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/app-root/app-board/app-main-layout/app-profile-form-page-update/div/form/div[2]/div[3]/mat-select/div/div[2]/div").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/mat-option[3]/span").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/app-root/app-board/app-main-layout/app-profile-form-page-update/div/form/div[3]/div[2]/mat-chip-list/div/input").send_keys("Angular")
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/mat-option[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='mat-select-value-11']/span").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='mat-option-36']/span").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/app-root/app-board/app-main-layout/app-profile-form-page-update/div/form/div[4]/div[2]/input").send_keys("https://google.com", Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB)
time.sleep(2)
driver.switch_to.active_element.find_element(By.XPATH, "/html/body/app-root/app-board/app-main-layout/app-profile-form-page-update/div/form/div[5]/button").click()
time.sleep(5)
newprofile = driver.find_element(By.XPATH, "/html/body/app-root/app-board/app-main-layout/app-dashboard-page/div/div/app-profiles-dashboard/div[2]/ul").text
newprofile1 = driver.find_element(By.XPATH, "/html/body/app-root/app-board/app-main-layout/app-dashboard-page/div/div/app-profiles-dashboard/div[2]/ul/li[1]/div/div[1]/h5").text
try:
    assert 'AutoTestPosition' in newprofile
    print("Test passed.", newprofile1, "profile is created")
    print("Current url:", driver.current_url)
    print("Please wait while the profile is being deleted")
except Exception as e:
    print("TEST FAILED. Available profiles:", newprofile, format(e))
    print("Current url:", driver.current_url)



##################DELETE PROFILE#################

time.sleep(10)
Delete = driver.find_element(By.XPATH, "/html/body/app-root/app-board/app-main-layout/app-dashboard-page/div/div/app-profiles-dashboard/div[2]/ul/li[1]/div/div[2]/div/button")
Delete.click()
time.sleep(2)
Delete1 = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/button[2]")
Delete1.click()
time.sleep(2)
Delete2 = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/app-confirm-dialog/div[2]/button[1]/span[1]")
Delete2.click()
time.sleep(2)
Delete3 = driver.find_element(By.XPATH, "/html/body/app-root/app-board/app-main-layout/app-dashboard-page/div/div/app-profiles-dashboard/div[2]/app-search-block/div[2]/mat-form-field/div/div[1]/div/mat-select/div/div[1]/span")
Delete3.click()
time.sleep(2)
Delete4 = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/mat-option[2]/span")
Delete4.click()
time.sleep(2)
Delete5 = driver.find_element(By.XPATH, "/html/body/app-root/app-board/app-main-layout/app-dashboard-page/div/div/app-profiles-dashboard/div[2]/ul/li/div/div[2]/div/button")
Delete5.click()
time.sleep(2)
Delete6 = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/button[3]")
Delete6.click()
time.sleep(2)
Delete7 = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/app-confirm-dialog/div[2]/button[1]/span[1]")
Delete7.click()
print("Profile deleted. Quit browser")
time.sleep(3)
#time.sleep(15)
driver.quit()