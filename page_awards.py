from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_base import BasePage
import time  

class AwardsPage(BasePage):
  def get_text_main_header(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/header/div/div/h1').text
  
  def get_text_main_sub_header(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/header/div/div/p').text
  
  def get_element_article_real(self):
    return self.get_section_by_aria_label('article', 'A real confidence builder.')
  
  def get_text_real_header(self):
    real_section = self.get_element_article_real()
    return self.get_text_section_header(real_section)
  
  def get_text_real_body(self):
    real_section = self.get_element_article_real()
    body_elements = real_section.find_elements(By.TAG_NAME, 'p')
    body_text = []
    for i in range(len(body_elements)):
      body_text.append(body_elements[i].text)
    return body_text

  def get_element_article_national(self):
    return self.get_section_by_aria_label('article', 'National Awards')
  
  def get_text_national_header(self):
    national_section = self.get_element_article_national()
    return self.get_text_section_header(national_section)
  
  def get_text_national_body(self):
    national_section = self.get_element_article_national()
    return self.get_text_section_body(national_section)
  
  def get_elements_national_images(self):
    national_section = self.get_element_article_national()
    return national_section.find_elements(By.TAG_NAME, 'img')
  
  def get_element_section_first_list(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/div[1]')
  
  def get_text_first_list(self):
    first_section = self.get_element_section_first_list()
    list_elements = first_section.find_elements(By.TAG_NAME, 'li')
    list_text = []
    for i in range(len(list_elements)):
      list_text.append(list_elements[i].text)
    return list_text
  
  def get_element_article_regional(self):
    return self.get_section_by_aria_label('article', 'Regional Awards')
  
  def get_text_regional_header(self):
    regional_section = self.get_element_article_regional()
    return self.get_text_section_header(regional_section)
  
  def get_text_regional_body(self):
    regional_section = self.get_element_article_regional()
    return self.get_text_section_body(regional_section)
  
  def get_elements_regional_images(self):
    regional_section = self.get_element_article_regional()
    return regional_section.find_elements(By.TAG_NAME, 'img')
  
  def get_element_section_second_list(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/div[2]')
  
  def get_text_second_list(self):
    second_section = self.get_element_section_second_list()
    list_elements = second_section.find_elements(By.TAG_NAME, 'li')
    list_text = []
    for i in range(len(list_elements)):
      list_text.append(list_elements[i].text)
    return list_text
  
  def get_element_article_setting(self):
    return self.get_section_by_aria_label('article', 'Setting the standard for energy-efficient homes.')
  
  def get_text_setting_header(self):
    setting_section = self.get_element_article_setting()
    return self.get_text_section_header(setting_section)
  
  def get_text_setting_body(self):
    setting_section = self.get_element_article_setting()
    return self.get_text_section_body(setting_section)
  
  def get_elements_setting_images(self):
    setting_section = self.get_element_article_setting()
    return setting_section.find_elements(By.TAG_NAME, 'img')
  
  def get_element_aside(self):
    return self.get_section_by_aria_label('aside', '')
  
  def get_text_aside_body(self):
    aside = self.get_element_aside()
    body_elements = aside.find_elements(By.TAG_NAME, 'p')
    body_text = []
    for i in range(len(body_elements)):
      body_text.append(body_elements[i].text)
    return body_text
  
  def click_element_aside_button_1(self):
    html = self.get_html()
    aside = self.get_element_aside()
    self.click_element_section_button(aside)
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
    
  def click_element_aside_button_2(self):
    html = self.get_html()
    aside = self.get_element_aside()
    aside.find_element(By.XPATH, './/div/div/div[2]/a').click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
    #Best Home Builders for Energy Efficient Homes | Meritage Homes

  def get_element_article_disclaimer(self):
    return self.get_section_by_aria_label('article', '')
  
  def get_text_disclaimer_body(self):
    disclaimer_section = self.get_element_article_disclaimer()
    return self.get_text_section_body(disclaimer_section)
  
  def get_element_aside_ready_to_find(self):
    return self.get_section_by_aria_label('aside', 'Ready to find your home?')
  
  def get_text_aside_ready_to_find_header(self):
    aside_ready_to_find = self.get_element_aside_ready_to_find()
    return self.get_text_section_header(aside_ready_to_find)

  def get_text_aside_ready_to_find_body(self):
    aside_ready_to_find = self.get_element_aside_ready_to_find()
    return self.get_text_section_body(aside_ready_to_find)
  
  def click_element_aside_ready_to_find_button_1(self):
    html = self.get_html()
    aside_ready_to_find = self.get_element_aside_ready_to_find()
    aside_ready_to_find.find_element(By.XPATH, './/div/div/div[2]/a[1]').click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))

  def click_element_aside_ready_to_find_button_2(self):
    html = self.get_html()
    aside_ready_to_find = self.get_element_aside_ready_to_find()
    aside_ready_to_find.find_element(By.XPATH, './/div/div/div[2]/a[2]').click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))