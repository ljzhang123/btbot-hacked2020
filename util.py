import os
import requests
from selenium.common import exceptions
from zipfile import ZipFile

def getPath():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    if os.path.exists('chromedriver.exe') == False:
        raise exceptions.WebDriverException('driver not in directory')
        
    # TODO: call getDriver() to download a driver after an exception has been raised

def getDriver(browserVersion):
    website = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE_' + browserVersion
    r = requests.get(website, allow_redirects = True)
    latestURL = r.text
    # downloadURL = 'https://chromedriver.storage.googleapis.com/index.html?path=' + latestURL + '/'
    downloadURL = 'https://chromedriver.storage.googleapis.com/' + latestURL + '/chromedriver_win32.zip'
    download = requests.get(downloadURL, allow_redirects = True)
    open('chromedriver_win32.zip', 'wb').write(download.content)

    ZipFile('chromedriver_win32.zip', 'r').extractall()
    os.remove('chromedriver_win32.zip')

# if __name__ == "__main__":
#     version = "83.0.4103"
#     os.chdir(os.path.dirname(os.path.abspath(__file__)))
#     getDriver(version)
