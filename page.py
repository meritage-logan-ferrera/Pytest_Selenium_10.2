import time
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
  def __init__(self, driver):
    self.driver = driver

class MainPage(BasePage):
  def click_state(self, state):
    state_selected = self.driver.find_element(By.XPATH, f"//a[@href='/state/{state}']")
    state_selected.click()
    WebDriverWait(self.driver, timeout=3).until(EC.invisibility_of_element(state_selected)) # Wait until the page is changed (this way is dumb I will try to find a better one) before we end this function to make sure the driver has time to be aware of the new page
#     return TexasPage(self.driver)

class MainPageAndroid(BasePage):
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
# class TexasPage(BasePage):
#   def something(self):
#     print("temp")

