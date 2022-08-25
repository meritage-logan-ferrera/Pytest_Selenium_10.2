from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class BasePageAndroid(object):
  def __init__(self, driver):
    self.driver = driver

class MainPageAndroid(BasePageAndroid):
  def exit_cookies(self):
    # wait = WebDriverWait(self.driver, 1)
    # close_cookie_button = self.driver.find_element(MobileBy.XPATH, "//a[@aria-label='Close Banner Button']")
    # wait.until(EC.visibility_of(close_cookie_button)) *****until is having toruble with appium, perhaps appium elements are not of type WebElement *****
    elements = self.driver.find_elements(MobileBy.XPATH, "//a[@aria-label='Close Banner Button']") # remove cookie prompt since it covers other elements on the page so we cannot click them
    if len(elements) != 0:
      elements[0].click()
      #WebDriverWait(self.driver, timeout=3).until(EC.invisibility_of_element(elements[0]))
  
  def click_state(self):
    self.exit_cookies()
    arizona = self.driver.find_element(MobileBy.XPATH, "//a[@href='/state/az']")
    arizona.click()
    #WebDriverWait(self.driver, timeout=3).until(EC.invisibility_of_element(arizona))