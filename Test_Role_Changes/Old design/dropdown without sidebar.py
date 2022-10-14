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
import pytest


#NON BROWSER MODE
# options
options = webdriver.ChromeOptions()

#Blink
options.add_argument("--disable-blink-features=AutomationControlled")

#headless mode
driver = webdriver.Chrome('C:/Users/isid/PycharmProjects/aww/chromedriver.exe',
                          options=options  # add "#" before "options" to start test with CHROME
                          )
#
# OPEN GO-REMOTE AND LOGIN AS "OLENA PEDASH"
driver.get("https://a-qa-web.azurewebsites.net/go-remote")
def test_SignIn():
    print("SIGN IN")
    wait = WebDriverWait(driver, 20)
    SignIn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-landing-layout/app-landing-navbar/nav/div/div[2]/div/button/span[1]")))
    SignIn.click()
    time.sleep(2)
    print("Enter the email data")
    email = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-landing-layout/app-sign-in/div/form/div[2]/div[3]/div[1]/div/input")))
    email.click()
    email.send_keys("1olena.pedash@awwcor.com")
    time.sleep(2)
    print('.....................................')
    print("Enter the password")
    print('.....................................')
    password = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-landing-layout/app-sign-in/div/form/div[2]/div[3]/div[2]/div/input")))
    password.click()
    password.send_keys("Password1")
    password.send_keys(Keys.RETURN)
    time.sleep(5)
    LOGGEDIN = driver.find_element(By.XPATH, "/html/body/app-root/app-board/app-main-layout/app-new-navbar/nav/div/div/button/span[1]/span[1]" or "/html/body/app-root/app-main-layout/app-new-navbar/nav/div/div/button/span[1]/span[1]").text
    try:
        assert 'Company' or 'Customer' or 'Admin' or 'Employee' or 'JobSeeker' in LOGGEDIN
        print("User is LOGGED IN")
    except Exception as e:
        print("TEST FAILED")
        print("User is NOT LOGGED IN", format(e))
    print('.....................................')
    time.sleep(8)

    #OPEN MAIN MENU AND CHECKING USER'S ROLE/COMPANY
    mainmenu = driver.find_element(By.XPATH, "/html/body/app-root/app-board/app-main-layout/app-new-navbar/nav/div/div/button/span[1]/span[2]/img" or "/html/body/app-root/app-board/app-main-layout/app-new-navbar/nav/div/div/button/span[1]")
    mainmenu.click()
    time.sleep(2)
    role_title = driver.find_element(By.CLASS_NAME, "manager-role")
    print("Role/Company:")
    print(role_title.text)
    print('.....................................')
    time.sleep(2)
    #
    pass
def test_Adminrole():
    print("SWITCH TO ADMIN ROLE")
    wait = WebDriverWait(driver, 20)
    adminrole = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div/div/div[3]/div[1]/div[1]/span")
    adminrole.click()
    adminrole2 = wait.until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div/div/div/div[3]/div[1]/div[2]")))
    adminrole2.click()
    time.sleep(5)
    ADMINROLEtitle = driver.find_element(By.XPATH,
                                         "/html/body/app-root/app-main-layout/app-new-navbar/nav/div/div/button/span[1]/span[1]").text
    try:
        assert 'Admin' in ADMINROLEtitle
        print("TEST PASSED. SWITCHED TO", ADMINROLEtitle, "ROLE")
    except Exception as e:
        print("TEST FAILED. Curent role:", ADMINROLEtitle, format(e))
    print('.....................................')
    #
    print("Open JobBoard")
    jobboard_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/app-root/app-main-layout/app-new-navbar/nav/div/div/div/a[2]")))
    time.sleep(2)
    jobboard_btn.click()
    try:
        title = driver.title
        assert 'Job Board' in title
        print("JobBoard is opened")
    except Exception as e:
        print("FAILED. JobBoard is not opened", format(e))
    print('.....................................')
    time.sleep(5)
    #
    pass
def test_company():
    print("SWITCH TO COMPANY ROLE")
    wait = WebDriverWait(driver, 20)
    admintocompany1 = driver.find_element(By.XPATH,
                                          "/html/body/app-root/app-landing-layout/app-new-navbar/nav/div/div/button/span[1]/span[1]")
    admintocompany1.click()
    time.sleep(2)
    admintocompany2 = driver.find_element(By.XPATH,
                                          "/html/body/app-root/app-landing-layout/app-new-navbar/nav/div/div/button/span[1]/span[2]/img")
    admintocompany2.click()
    time.sleep(2)
    admintocompany3 = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div[3]/div[2]/div[1]/img")
    admintocompany3.click()
    admintocompany3 = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div[3]/div[2]/div[2]")
    admintocompany3.click()
    time.sleep(5)
    Companyrole = driver.find_element(By.XPATH,
                                      "/html/body/app-root/app-board/app-main-layout/app-new-navbar/nav/div/div/button/span[1]/span[1]").text
    try:
        assert 'Company' in Companyrole
        print("TEST PASSED. SWITCHED TO", Companyrole, "ROLE")
    except Exception as e:
        print("TEST FAILED. Curent role:", Companyrole, format(e))
    print('.....................................')
    #
    print("Open JobBoard")
    driver.find_element(By.XPATH,
                        "/html/body/app-root/app-board/app-main-layout/app-new-navbar/nav/div/div/div/a[2]/span[1]").click()
    time.sleep(4)
    try:
        title = driver.title
        assert 'Job Board' in title
        print("JobBoard is opened")
    except Exception as e:
        print("JobBoard is not opened", format(e))
    print('.....................................')
    #
    pass
def test_customer():
    print("SWITCH TO CUSTOMER ROLE")
    wait = WebDriverWait(driver, 20)
    customerrole1 = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH,
                                                                              "/html/body/app-root/app-landing-layout/app-new-navbar/nav/div/div/button/span[1]")))
    customerrole1.click()
    time.sleep(2)
    customerrole4 = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH,
                                                                              "/html/body/app-root/app-landing-layout/app-new-navbar/nav/div/div/button/span[1]")))
    customerrole4.click()
    time.sleep(2)
    customerrole2 = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div[3]/div[3]/div[1]/img")
    customerrole2.click()
    time.sleep(2)
    customerrole3 = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div[3]/div[3]/div[2]")
    customerrole3.click()
    time.sleep(5)
    Customerrole = driver.find_element(By.XPATH,
                                       "/html/body/app-root/app-main-layout/app-new-navbar/nav/div/div/button/span[1]/span[1]").text
    try:
        assert 'Customer' in Customerrole
        print("TEST PASSED. SWITCHED TO", Customerrole, "ROLE")
    except Exception as e:
        print("TEST FAILED. Curent role:", Customerrole, format(e))
    print('.....................................')
    #
    print("Open JobBoard")
    driver.find_element(By.XPATH,
                        "/html/body/app-root/app-main-layout/app-new-navbar/nav/div/div/div/a[2]/span[1]").click()
    time.sleep(2)
    try:
        title = driver.title
        assert 'Job Board' in title
        print("JobBoard is opened")
    except Exception as e:
        print("JobBoard is not opened", format(e))
    print('.....................................')
    #
    pass
def test_employee():
    print("SWITCH TO EMPLOYEE ROLE")
    wait = WebDriverWait(driver, 20)
    employeerole1 = driver.find_element(By.XPATH,
                                        "/html/body/app-root/app-landing-layout/app-new-navbar/nav/div/div/button/span[1]/span[1]")
    employeerole1.click()
    time.sleep(1)
    employeerole1.click()
    time.sleep(2)
    employeerole2 = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div[3]/div[4]/div[1]/img")
    employeerole2.click()
    time.sleep(2)
    employeerole3 = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div[3]/div[4]/div[2]")
    employeerole3.click()
    time.sleep(5)
    employeerole = driver.find_element(By.XPATH,
                                       "/html/body/app-root/app-main-layout/app-new-navbar/nav/div/div/button/span[1]/span[1]").text
    try:
        assert 'Employee' in employeerole
        print("TEST PASSED. SWITCHED TO", employeerole, "ROLE")
    except Exception as e:
        print("TEST FAILED. Curent role:", employeerole, format(e))
    print('.....................................')
    #
    print("Open JobBoard")
    driver.find_element(By.XPATH,
                        "/html/body/app-root/app-main-layout/app-new-navbar/nav/div/div/div/a[2]/span[1]").click()
    time.sleep(2)
    try:
        title = driver.title
        assert 'Job Board' in title
        print("JobBoard is opened")
    except Exception as e:
        print("JobBoard is not opened", format(e))
    print('.....................................')
    pass
def test_jobseeker():
    print("SWITCH TO JOB SEEKER ROLE")
    wait = WebDriverWait(driver, 20)
    JobSeekerrole1 = driver.find_element(By.XPATH,
                                         "/html/body/app-root/app-landing-layout/app-new-navbar/nav/div/div/button/span[1]/span[1]")
    JobSeekerrole1.click()
    time.sleep(1)
    JobSeekerrole1.click()
    time.sleep(2)
    JobSeekerrole2 = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div[3]/div[5]/div[1]/img")
    JobSeekerrole2.click()
    time.sleep(2)
    JobSeekerrole3 = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div[3]/div[5]/div[2]")
    JobSeekerrole3.click()
    time.sleep(5)
    JobSeekerrole = driver.find_element(By.XPATH,
                                        "/html/body/app-root/app-board/app-main-layout/app-new-navbar/nav/div/div/button/span[1]/span[1]").text
    try:
        assert 'JobSeeker' in JobSeekerrole
        print("TEST PASSED. SWITCHED TO", JobSeekerrole, "ROLE")
    except Exception as e:
        print("TEST FAILED. Curent role:", JobSeekerrole, format(e))

    print('.....................................')
    print('ALL TESTS ARE PASSED')

    print('.....................................')
    time.sleep(15)
    pass

    driver.quit()