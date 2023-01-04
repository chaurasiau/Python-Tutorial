import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
###########################
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
###########################

options = Options()
# this parameter tells Chrome that
# it should be run without UI (Headless)
options.headless = True
# options.add_argument('--allow-running-insecure-content')
# options.add_argument('ignore-certificate-errors')
# options.add_argument('--disable-features=VizDisplayCompositor')
# initializing webdriver for Chrome
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()), options=options)
# driver = webdriver.Chrome()

# getting GeekForGeeks webpage
driver.get('https://www.geeksforgeeks.org')

# sleep for 5 seconds just to see that
# the browser was opened indeed
time.sleep(5)

# closing browser
driver.close()
