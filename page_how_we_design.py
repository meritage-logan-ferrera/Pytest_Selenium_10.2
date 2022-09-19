from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_base import BasePage
import time  

class HowWeDesignPage(BasePage):
  def get_text_main_header(self):
    return self.driver.find_element(By.XPATH, '/html/body/header/div/div/h1').text
  
  def get_text_main_sub_header(self):
    return self.driver.find_element(By.XPATH, '/html/body/header/div/div/p').text
  
  def get_text_article_no_header_body(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/article[1]/header/div").text
  
  def click_element_article_no_header_button(self):
    html = self.get_html()
    self.driver.find_element(By.XPATH, '/html/body/main/article[1]/header/div/a').click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))

  def get_element_section_design_collections(self):
    return self.get_section_by_aria_label('article', 'Design Collections')
  
  def get_text_design_header(self):
    design_section = self.get_element_section_design_collections()
    return self.get_text_section_header(design_section)
  
  def get_elements_design_body(self):
    design_section = self.get_element_section_design_collections()
    return design_section.find_elements(By.TAG_NAME, 'p')
  
  def get_element_design_image(self):
    design_section = self.get_element_section_design_collections()
    return self.get_element_section_placeholder_image(design_section)
  
  def click_element_design_button(self):
    html = self.get_html()
    design_section = self.get_element_section_design_collections()
    self.click_element_section_button(design_section)
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_element_section_live_now(self):
    return self.get_section_by_aria_label('article', 'LiVE.NOW.')
  
  def get_text_live_header(self):
    live_section = self.get_element_section_live_now()
    return self.get_text_section_header(live_section)
  
  def get_elements_live_body(self):
    live_section = self.get_element_section_live_now()
    return live_section.find_elements(By.TAG_NAME, 'p')
  
  def get_element_live_image(self):
    live_section = self.get_element_section_live_now()
    return self.get_element_section_placeholder_image(live_section)
  
  def click_element_live_button(self):
    html = self.get_html()
    live_section = self.get_element_section_live_now()
    self.click_element_section_button(live_section)
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))

  def get_element_article_columns(self, number):
    return self.driver.find_element(By.XPATH, f'/html/body/main/div[3]/div[2]/article[{number}]')
  
  def get_text_column_header(self, number):
    column_article = self.get_element_article_columns(number)
    return column_article.find_element(By.TAG_NAME, 'h3').text
  
  def get_text_column_body(self, number):
    column_article = self.get_element_article_columns(number)
    return column_article.find_element(By.TAG_NAME, 'p').text
  
  def click_element_column_button(self, number):
    html = self.get_html()
    column_article = self.get_element_article_columns(number)
    self.click_element_section_button(column_article)
    if number != 3:
      WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_text_bottom_asterisk(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/article[4]/header/div/p/span').text
