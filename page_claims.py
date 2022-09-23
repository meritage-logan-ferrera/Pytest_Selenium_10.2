from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_base import BasePage
import time  

class ClaimsPage(BasePage):
  def get_text_main_header(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/div/div[1]/div/h2').text
  
  def get_element_main_header(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/div')
  
  def get_element_header_link_1(self):
    header_section = self.get_element_main_header()
    return header_section.find_element(By.XPATH, './/div[2]/div/div/div/a[1]')
  
  def get_element_header_link_2(self):
    header_section = self.get_element_main_header()
    return header_section.find_element(By.XPATH, './/div[2]/div/div/div/a[2]')

  def click_element_header_link_1(self):
    button = self.get_element_header_link_1()
    button.click()
  
  def click_element_header_link_2(self):
    button = self.get_element_header_link_1()
    button.click()

  def get_element_article_1(self):
    return self.driver.find_element(By.ID, 'energy-efficient-features-claims')

  def get_element_article_2(self):
    return self.driver.find_element(By.ID, 'general-energy-claims')
  
  def get_text_article_1_header(self):
    article_1 = self.get_element_article_1()
    return article_1.find_element(By.TAG_NAME, 'h4').text

  def get_text_article_2_header(self):
    article_2 = self.get_element_article_2()
    return article_2.find_element(By.TAG_NAME, 'h4').text
  
  def get_elements_article_1_links(self):
    article_1 = self.get_element_article_1()
    return article_1.find_elements(By.TAG_NAME, 'a')
  
  def get_elements_article_1_headers(self):
    article_1 = self.get_element_article_1()
    header_elements = article_1.find_elements(By.TAG_NAME, 'strong')
    header_text = []
    for i in range(len(header_elements)):
      header_text.append(header_elements[i].text)
    return header_text

  def get_elements_article_2_links(self):
    article_2 = self.get_element_article_2()
    return article_2.find_elements(By.TAG_NAME, 'a')
  
  def get_elements_article_2_headers(self):
    article_2 = self.get_element_article_2()
    header_elements = article_2.find_elements(By.TAG_NAME, 'strong')
    header_text = []
    for i in range(len(header_elements)):
      header_text.append(header_elements[i].text)
    return header_text

  def get_element_aside_looking_for_help(self):
    return self.get_section_by_aria_label('aside', 'Looking for help narrowing your search?')
  
  def get_text_looking_for_help_header(self):
    questions_section = self.get_element_aside_looking_for_help()
    return self.get_text_section_header(questions_section)
  
  def get_text_looking_for_help_body(self):
    questions_section = self.get_element_aside_looking_for_help()
    return questions_section.find_element(By.TAG_NAME, 'span').text
  
  def click_element_looking_for_help_button_1(self):
    html = self.get_html()
    questions_section = self.get_element_aside_looking_for_help()
    self.click_element_section_button(questions_section)
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def click_element_looking_for_help_button_2(self):
    html = self.get_html()
    questions_section = self.get_element_aside_looking_for_help()
    questions_section.find_element(By.XPATH, './/div/div/div[2]/a[2]').click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))

  def get_element_article_disclaimer(self):
    return self.get_section_by_aria_label('article', '')
  
  def get_text_disclaimer(self):
    disclaimer_section = self.get_element_article_disclaimer()
    return disclaimer_section.find_element(By.TAG_NAME, 'p').text