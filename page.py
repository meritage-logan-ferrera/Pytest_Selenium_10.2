from argparse import Action
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class BasePage(object):
  def __init__(self, driver):
    self.driver = driver
  
  def get_html(self): # get the DOM of the current page, use when testing links and navigation
    return self.driver.find_element(By.TAG_NAME, 'html')
  
  def get_title(self):
    return self.driver.title

  def get_element_header_main(self, item):
    return self.driver.find_element(By.XPATH, f"//a[@href='/{item}']")
  
  def get_element_header_level2_homes(self, level2_item):
    return self.driver.find_element(By.XPATH, f"//a[@href='/state/{level2_item}']")
    
  def click_header_main_item(self, item):
    html = self.get_html()
    header_main_item = self.get_element_header_main(item)
    header_main_item.click()
    WebDriverWait(self.driver, timeout=15).until(EC.staleness_of(html)) # wait until the entire old webpage is not present until we assert for the title of the new page
    
  def click_header_level2_homes_item(self, level2_item):
    html = self.get_html()
    header_main_item = self.get_element_header_main('homes')
    header_level2_item = self.get_element_header_level2_homes(level2_item)
    action = ActionChains(self.driver)
    action.move_to_element(header_main_item).move_by_offset(0, 50).move_to_element(header_level2_item).click().perform()
    WebDriverWait(self.driver, timeout=15).until(EC.staleness_of(html))
    if self.driver.title == '':
      time.sleep(5) # Firefox takes longer to load the title for some reason


class MetroPage(BasePage): 
  def placeholder(self):
    return 'placeholder'
  

class MainPage(BasePage):
  def click_state(self, state):
    html = self.get_html()
    state_selected = self.driver.find_element(By.XPATH, f"//a[@href='/state/{state}']")
    state_selected.click()
    WebDriverWait(self.driver, timeout=15).until(EC.staleness_of(html)) 
#     return TexasPage(self.driver)

# class TexasPage(BasePage):
#   def something(self):
#     print("temp")

