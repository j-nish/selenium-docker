# Program which will simply connect to a remote selenium webdriver, then open a web page.

# Basic libraries
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# For sleeps
import time

# Assume that the container is running on the same machine
# In this case, selenium docker is running on port 4444
driver = webdriver.Remote(
  command_executor='http://127.0.0.1:4444/wd/hub',
  desired_capabilities=DesiredCapabilities.CHROME)

url = 'http://www.google.com'

driver.get(url)

time.sleep(3)

elem = driver.find_element_by_name("username")
elem.send_keys("your_username")

elem2 = driver.find_element_by_name("password")
elem2.send_keys('your_password')
elem2.send_keys(Keys.RETURN)

print('done!')
driver.close()
