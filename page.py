from argparse import Action
from email import header
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

  def get_element_meritage_image_translucent(self):
    return self.driver.find_element(By.CSS_SELECTOR, "img[src='//mthcdn.azureedge.net/-/media/corporate/navigation/logo-meritage-green-svg.ashx?h=74&la=en&w=335&rev=0ab3a3e8ac2c4762b58841066960c970&hash=7D5E7C8753CE3B810CC16D0F3EA6B093CCD10493']")

  def get_element_search_button(self):
    return self.driver.find_element(By.CSS_SELECTOR, "#button--search")
    
  def get_element_header_main(self, element):
    return self.driver.find_element(By.XPATH, f"//a[@href='/{element}']")
  
  def click_header_main_element(self, element):
    html = self.get_html()
    header_main_element = self.get_element_header_main(element)
    header_main_element.click()
    WebDriverWait(self.driver, timeout=15).until(EC.staleness_of(html)) # wait until the entire old webpage is not present until we assert for the title of the new page

  def get_element_header_level2(self, level1_element, level2_element):
    level1 = self.get_element_header_main(level1_element)
    if level1_element != level2_element:
      return level1.find_element(By.XPATH, f"//a[@href='/{level1_element}/{level2_element}']")
    else:
      return level1.find_element(By.XPATH, f"//a[@href='/{level1_element}']")

  def click_header_level2_element(self, level1_element, level2_element):
    html = self.get_html()
    header_main_element = self.get_element_header_main(level1_element)
    header_level2_element = self.get_element_header_level2(level1_element, level2_element)
    
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

