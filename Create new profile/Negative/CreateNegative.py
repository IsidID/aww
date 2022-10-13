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


def test_SignIn():
    print("LogIn")
    wait = WebDriverWait(driver, 30)
    SignIn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/app-root/app-landing-layout/app-landing-navbar/nav/div/div[2]/div/button/span[1]")))
    SignIn.click()
    time.sleep(2)
    email = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/app-root/app-landing-layout/app-sign-in/div/form/div[2]/div[3]/div[1]/div/input")))
    email.click()
    email.send_keys("1olena.pedash@awwcor.com")
    time.sleep(2)
    password = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/app-root/app-landing-layout/app-sign-in/div/form/div[2]/div[3]/div[2]/div/input")))
    password.click()
    password.send_keys("Password1")
    password.send_keys(Keys.RETURN)
    time.sleep(5)
    LOGGEDIN = driver.find_element(By.XPATH,
                                   "/html/body/app-root/app-board/app-main-layout/app-new-navbar/nav/div/div/button/span[1]/span[1]" or "/html/body/app-root/app-main-layout/app-new-navbar/nav/div/div/button/span[1]/span[1]").text
    try:
        assert 'Company' or 'Customer' or 'Admin' or 'Employee' or 'JobSeeker' in LOGGEDIN
        print("User is Logged In")
    except Exception as e:
        print("TEST FAILED")
        print("User is NOT LOGGED IN", format(e))
    time.sleep(5)

    # OPEN MAIN MENU AND CHECKING USER'S ROLE/COMPANY
    mainmenu = driver.find_element(By.XPATH,
                                   "/html/body/app-root/app-board/app-main-layout/app-new-navbar/nav/div/div/button/span[1]/span[1]" or "/html/body/app-root/app-main-layout/app-new-navbar/nav/div/div/button/span[1]/span[1]")
    # mainmenu.click()
    time.sleep(2)
    mainmenu.click()
    time.sleep(2)
    driver.switch_to.active_element
    role_title = driver.find_element(By.CLASS_NAME, "manager-role")
    print("Role/Company:")
    print(role_title.text)
    print("Current url:", driver.current_url)
    time.sleep(2)
    #
    pass


def test_jobseeker():
    print("Switch to JobSeeker role")
    wait = WebDriverWait(driver, 10)
    JobSeekerrole = driver.find_element(By.XPATH, "//*[@id='mat-menu-panel-0']/div/div[3]/div[5]/div[1]/span")
    JobSeekerrole.click()
    JobSeekerrole2 = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='mat-menu-panel-0']/div/div[3]/div[5]/div[2]")))
    JobSeekerrole2.click()
    time.sleep(5)
    JobSeekerroletitle = driver.find_element(By.XPATH,
                                             "/html/body/app-root/app-board/app-main-layout/app-new-navbar/nav/div/div/button/span[1]/span[1]").text
    try:
        assert 'JobSeeker' in JobSeekerroletitle
        print("Test passed. Current role:", JobSeekerroletitle)
        print("Current url:", driver.current_url)
    except Exception as e:
        print("TEST FAILED. Curent role:", JobSeekerroletitle, format(e))
        print("Current url:", driver.current_url)
    pass


def test_position_and_rates():
    time.sleep(2)
    createbutton = driver.find_element(By.XPATH,
                                       "/html/body/app-root/app-board/app-main-layout/app-dashboard-page/div/div/app-profiles-dashboard/div[2]/app-search-block/div[1]/a/span[1]/span")
    createbutton.click()
    time.sleep(5)
    pos = driver.find_element(By.XPATH,
                              "/html/body/app-root/app-board/app-main-layout/app-profile-form-page-update/div/form/div[1]/div[1]/input")
    pos.send_keys("AutoTest")
    time.sleep(2)
    pos.send_keys(Keys.CONTROL + "a")
    pos.send_keys(Keys.DELETE, Keys.TAB)
    time.sleep(2)
    posreq = driver.find_element(By.XPATH,
                                 "/html/body/app-root/app-board/app-main-layout/app-profile-form-page-update/div/form/div[1]/div[1]/mat-error").text
    try:
        assert 'This field is required' in posreq
        print("Your Position is clear")
    except Exception as e:
        print("Your position data not deleted")

    time.sleep(2)
    rate = driver.find_element(By.XPATH,
                               "/html/body/app-root/app-board/app-main-layout/app-profile-form-page-update/div/form/div[1]/div[2]/div[2]/input")
    rate.send_keys("45")
    typereq = driver.find_element(By.XPATH,
                                  "/html/body/app-root/app-board/app-main-layout/app-profile-form-page-update/div/form/div[1]/div[2]/div[1]/mat-error").text
    try:
        assert 'This field is required' in typereq
        print("Rate type is not choosed")
    except Exception as e:
        print("Your rate type data is choosed")
    time.sleep(2)
    time.sleep(2)
    rate.send_keys(Keys.CONTROL + "a")
    rate.send_keys(Keys.DELETE, Keys.TAB)
    time.sleep(2)
    ratereq = driver.find_element(By.XPATH,
                                  "/html/body/app-root/app-board/app-main-layout/app-profile-form-page-update/div/form/div[1]/div[2]/div[2]/mat-error").text
    try:
        assert 'This field is required' in ratereq
        print("Your Rate data is clear")
    except Exception as e:
        print("Your rate data not deleted")
    time.sleep(2)
    rate.send_keys("asddsaas")
    try:
        assert 'Use only numbers with up to 2 points precision!' in ratereq
        print("Rate text data is not available")
    except Exception as e:
        print("Your rate data can be text")
    time.sleep(2)
    rate.send_keys(Keys.CONTROL + "a")
    rate.send_keys(Keys.DELETE)
    time.sleep(2)
    rate.send_keys("21.1212")
    sleep(1)
    driver.switch_to.parent_frame()
    sleep(2)
    rate2poin = driver.find_element(By.XPATH,
                                    "/html/body/app-root/app-board/app-main-layout/app-profile-form-page-update/div/form/div[1]/div[2]/div[2]/mat-error").text
    # time.sleep(4)
    try:
        assert 'Use only numbers with up to 2 points precision!' in rate2poin
        print("Rate data with up 2 points is not available")
    except Exception as e:
        print("Your rate data can be with more than 2 points precision")
    time.sleep(2)
    rate.send_keys(Keys.CONTROL + "a")
    rate.send_keys(Keys.DELETE)
    time.sleep(2)
    rate.send_keys("!@#$%")
    sleep(1)
    driver.switch_to.parent_frame()
    sleep(2)
    ratesymb = driver.find_element(By.XPATH,
                                   "/html/body/app-root/app-board/app-main-layout/app-profile-form-page-update/div/form/div[1]/div[2]/div[2]/mat-error").text
    try:
        assert 'Use only numbers with up to 2 points precision!' in ratesymb
        print("Rate symbol data is not available")
    except Exception as e:
        print("Your rate data can be symbols")
    time.sleep(2)
    rate.send_keys(Keys.CONTROL + "a")
    rate.send_keys(Keys.DELETE)
    time.sleep(2)
    rate.send_keys("-45")
    sleep(1)
    driver.switch_to.parent_frame()
    sleep(2)
    rateminus = driver.find_element(By.XPATH,
                                   "/html/body/app-root/app-board/app-main-layout/app-profile-form-page-update/div/form/div[1]/div[2]/div[2]/mat-error").text
    try:
        assert 'Use only numbers with up to 2 points precision!' in rateminus
        print("Rate negative numbers data is not available")
    except Exception as e:
        print("Your rate data can be negative numbers")
    time.sleep(2)
    rate.send_keys(Keys.CONTROL + "a")
    rate.send_keys(Keys.DELETE)
    time.sleep(2)
    rate.send_keys("3232323232")
    sleep(1)
    driver.switch_to.parent_frame()
    sleep(2)
    ratenum = driver.find_element(By.XPATH,
                                  "/html/body/app-root/app-board/app-main-layout/app-profile-form-page-update/div/form/div[1]/div[2]/div[2]/mat-error").text
    try:
        assert 'Please enter a value between 0 and 999999.99!' in ratenum
        print("Rate overmore data is not available")
    except Exception as e:
        print("Your rate data can be not between 0 and 999999.99!")
    time.sleep(6)
    pass


def test_foreign_lang():
    driver.refresh()
    time.sleep(5)
    wait = WebDriverWait(driver, timeout=30)
    rate = driver.find_element(By.XPATH,
                               "/html/body/app-root/app-board/app-main-layout/app-profile-form-page-update/div/form/div[1]/div[2]/div[2]/input")
    rate.send_keys(Keys.TAB, Keys.SPACE)
    time.sleep(5)
    mat = driver.find_element(By.XPATH, "//div[@id='mat-select-2-panel']")
    mat.send_keys(Keys.ESCAPE, Keys.ESCAPE)
    mat.send_keys(Keys.ESCAPE)
    langreq = driver.find_element(By.XPATH,
                                  "/html/body/app-root/app-board/app-main-layout/app-profile-form-page-update/div/form/div[2]/div[3]/mat-error").text
    try:
        assert 'This field is required' in langreq
        print("Foreign language field is empty")
    except Exception as e:
        print("Dont choosed language lvl")
    time.sleep(2)
    pass


def test_skills():
    driver.refresh()
    time.sleep(8)
    wait = WebDriverWait(driver, timeout=30)
    skills = driver.find_element(By.XPATH,
                                 "/html/body/app-root/app-board/app-main-layout/app-profile-form-page-update/div/form/div[3]/div[2]/mat-chip-list/div/input")
    skills.click()
    time.sleep(3)
    driver.switch_to.parent_frame()
    skills.send_keys(Keys.ESCAPE)
    sleep(2)
    sleep(2)
    Skillsqeq = driver.find_element(By.XPATH,
                                    "/html/body/app-root/app-board/app-main-layout/app-profile-form-page-update/div/form/div[3]/div[2]/mat-error").text
    try:
        assert 'This field is required' in Skillsqeq
        print("Skills fields is empty")
    except Exception as e:
        print("Dont choosed skills")
    time.sleep(2)
    pass


def test_resume():
    driver.refresh()
    time.sleep(5)
    wait = WebDriverWait(driver, timeout=30)
    resume = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH,
                                                                       "/html/body/app-root/app-board/app-main-layout/app-profile-form-page-update/div/form/div[4]/div[2]/input")))
    resume.send_keys("sad")
    resume.send_keys(Keys.TAB)
    time.sleep(4)
    resumereq = driver.find_element(By.XPATH,
                                    "/html/body/app-root/app-board/app-main-layout/app-profile-form-page-update/div/form/div[4]/div[2]/mat-error" or "//*[@id='mat-error-0']").text
    try:
        assert 'Please enter correct URL address' in resumereq
        print("Resume link checked")
        resume.send_keys(Keys.CONTROL + "a")
        resume.send_keys(Keys.DELETE)
    except Exception as e:
        print("no resume link")

    time.sleep(2)

    resumelinkedin = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH,
                                                                               "/html/body/app-root/app-board/app-main-layout/app-profile-form-page-update/div/form/div[4]/div[3]/input")))
    resumelinkedin.send_keys("https://www.linkedin.com/in/sadasd/")
    time.sleep(2)
    resumelinkedin.send_keys(Keys.CONTROL + "a")
    resumelinkedin.send_keys(Keys.DELETE)
    resumelinkedin.send_keys("linkedin.com", Keys.TAB)
    sleep(2)
    resumelinkedinreq = driver.find_element(By.XPATH,
                                            "/html/body/app-root/app-board/app-main-layout/app-profile-form-page-update/div/form/div[4]/div[3]/mat-error").text
    try:
        assert 'LinkedIn invalid' in resumelinkedinreq
        resumelinkedin.send_keys(Keys.CONTROL + "a")
        resumelinkedin.send_keys(Keys.DELETE)
        print("LinkedIn link checked")
    except Exception as e:
        print("no linkedin link")

    time.sleep(2)

    # resumeattach = driver.find_element(By.XPATH,
    #                                   "/html/body/app-root/app-board/app-main-layout/app-profile-form-page-update/div/form/div[4]/div[4]/app-upload-file/label[1]")
    # resumeattach.click()
    # time.sleep(5)
    # pyautogui.write('https://drive.google.com/file/d/1bgoFfpHYwfEw0YsiMm8c1cgye88pgzfJ/view?usp=sharing')
    # sleep(2)
    # pyautogui.press('return')
    # time.sleep(8)
    # try:
    #    assert driver.find_element(By.XPATH, "/html/body/div[4]/div").is_enabled()
    # except Exception as e:
    #    print("no attached files")
    # time.sleep(8)
    port = driver.find_element(By.XPATH,
                               "/html/body/app-root/app-board/app-main-layout/app-profile-form-page-update/div/form/div[4]/div[5]/input")
    port.send_keys("asdfs", Keys.TAB)
    sleep(2)
    portlink = driver.find_element(By.XPATH,
                                   "/html/body/app-root/app-board/app-main-layout/app-profile-form-page-update/div/form/div[4]/div[5]/mat-error").text
    try:
        assert 'It must be link' in portlink
        print("Portfolio link checked")
    except Exception as e:
        print("data in portfolio is not link")
    pass
    sleep(4)
    driver.quit()