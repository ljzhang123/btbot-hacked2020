from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import os
import util

# TODO: function to be refactored into util.py
def driverUpdate():
    browserVersion = browser.capabilities['browserVersion'].rsplit('.', 1)[0] # newer webdrivers use 'browserVersion' as key instead of 'version'
    driverVersion = browser.capabilities['chrome']['chromedriverVersion'].rsplit('.', 1)[0]
    print("Current browser version is: " + browserVersion + "\nCurrent driver version is: " + driverVersion)

    if browserVersion != driverVersion:
        # TODO: write function in util.py to download appropriate driver
        os.remove('chromedriver.exe')
        util.getDriver(browserVersion)

util.getPath()
# TODO: add exception handling no pre-exisiting web driver
browser = webdriver.Chrome()
driverUpdate()
browser.get("https://www.beartracks.ualberta.ca/psp/uahebprd/EMPLOYEE/HRMS/c/ZSS_STUDENT_CENTER.ZSS_WATCH_LIST.GBL?FolderPath=PORTAL_ROOT_OBJECT.ZSS_ACADEMICS.ZSS_AC_PLAN.ZSS_WATCH_LIST_GBL_1&amp;IsFolder=false&amp;IgnoreParamTempl=FolderPath%2cIsFolder")

username = browser.find_element_by_id('username')
username.send_keys('') # enter username here

password = browser.find_element_by_id('user_pass')
password.send_keys('') # enter password here

password.submit()

# TODO: find and output all semesters displayed
# seats = browser.find_element_by_id('SSR_DUMMY_RECV1$sels$0$$0')
# seats.submit()
