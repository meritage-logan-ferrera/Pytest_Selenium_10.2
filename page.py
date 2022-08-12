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
  MAIN_NAV_ELEMENTS = ('homes', 'why-meritage', 'buyer-resources', 'my-home')
  STATES = ('az', 'ca', 'co', 'fl', 'ga', 'nc', 'sc', 'tn', 'tx')
  WHY_MERITAGE_NAV_ELEMENTS = ('why-meritage', 'testimonials', 'reviews', 'energy-efficiency', 'how-we-design', 'how-we-build', 'awards')
  BUYER_RESOURCES_NAV_ELEMENTS = ('buyer-resources', 'homebuying', 'home-financing', 'energy-efficiency', 'home-design')
  def __init__(self, driver):
    self.driver = driver
  
  def get_html(self): # get the DOM of the current page, use when testing links and navigation
    return self.driver.find_element(By.TAG_NAME, 'html')
  
  def get_title(self):
    return self.driver.title

  def get_element_header_main(self, element):
    return self.driver.find_element(By.XPATH, f"//a[@href='/{element}']")
  
  def get_element_header_level2_homes(self, level2_element):
    if level2_element in self.STATES:
      return self.driver.find_element(By.XPATH, f"//a[@href='/state/{level2_element}']")
    if level2_element in self.WHY_MERITAGE_NAV_ELEMENTS:
      if level2_element == self.WHY_MERITAGE_NAV_ELEMENTS[0]:
        return self.driver.find_element(By.XPATH, f"//a[@href='/why-meritage']")
      else:
        return self.driver.find_element(By.XPATH, f"//a[@href='/why-meritage/{level2_element}']")

  def click_header_main_element(self, element):
    html = self.get_html()
    header_main_element = self.get_element_header_main(element)
    header_main_element.click()
    WebDriverWait(self.driver, timeout=15).until(EC.staleness_of(html)) # wait until the entire old webpage is not present until we assert for the title of the new page
    
  def click_header_level2_homes_element(self, level2_element):
    html = self.get_html()
    header_main_element = None
    if level2_element in self.STATES:
      header_main_element = self.get_element_header_main(self.MAIN_NAV_ELEMENTS[0])
    if level2_element in self.WHY_MERITAGE_NAV_ELEMENTS:
      header_main_element = self.get_element_header_main(self.MAIN_NAV_ELEMENTS[1])
    if level2_element in self.BUYER_RESOURCES_NAV_ELEMENTS:
      header_main_element = self.get_element_header_main(self.MAIN_NAV_ELEMENTS[2])
    header_level2_element = self.get_element_header_level2_homes(level2_element)
    action = ActionChains(self.driver)
    action.move_to_element(header_main_element).move_by_offset(0, 50).move_to_element(header_level2_element).click().perform()
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

