from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_base import BasePage
import time  

class ESGPage(BasePage):
  def get_text_main_header(self):
    return self.driver.find_element(By.XPATH, '/html/body/header/div/div/h1').text
  
  def get_element_aside_no_title(self):
    return self.get_section_by_aria_label('aside', '')
  
  def get_elements_aside_body(self):
    no_title_aside = self.get_element_aside_no_title()
    return no_title_aside.find_elements(By.TAG_NAME, 'p')
  
  def click_element_aside_button(self):
    no_title_aside = self.get_element_aside_no_title()
    no_title_aside.find_element(By.TAG_NAME, 'a')
  
  def get_element_article_environmental(self):
    return self.get_section_by_aria_label('article', 'Environmental')
  
  def get_element_environmental_image(self):
    environmental_section = self.get_element_article_environmental()
    return self.get_element_section_placeholder_image(environmental_section)
  
  def get_elements_environmental_body(self):
    environmental_section = self.get_element_article_environmental()
    return environmental_section.find_elements(By.TAG_NAME, 'p')
  
  def get_text_environmental_header(self):
    environmental_section = self.get_element_article_environmental()
    return self.get_text_section_header(environmental_section)
  
  def click_element_environmental_button(self):
    html = self.get_html()
    environmental_section = self.get_element_article_environmental()
    self.click_element_section_button(environmental_section)
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  
  
