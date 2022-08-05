import time
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
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

# class TexasPage(BasePage):
#   def something(self):
#     print("temp")

