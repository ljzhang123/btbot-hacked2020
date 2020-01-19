from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome(executable_path=r'C:\Users\John Doe\PycharmProjects\chromedriver.exe')
browser.get("https://www.beartracks.ualberta.ca/psp/uahebprd/EMPLOYEE/HRMS/c/ZSS_STUDENT_CENTER.ZSS_WATCH_LIST.GBL?FolderPath=PORTAL_ROOT_OBJECT.ZSS_ACADEMICS.ZSS_AC_PLAN.ZSS_WATCH_LIST_GBL_1&amp;IsFolder=false&amp;IgnoreParamTempl=FolderPath%2cIsFolder")

username = browser.find_element_by_id('username')
username.send_keys('') # enter username here

password = browser.find_element_by_id('user_pass')
password.send_keys('') # enter password here

password.submit()

seats = browser.find_element_by_id('SSR_DUMMY_RECV1$sels$0$$0')
seats.submit()
