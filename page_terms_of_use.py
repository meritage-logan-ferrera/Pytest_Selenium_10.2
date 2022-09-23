from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_base import BasePage
import time  

class TermsOfUsePage(BasePage):
  def get_text_main_header(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/header/div/div/h1').text
  
  def get_element_main_article(self):
    return self.get_section_by_aria_label('article', '')
  
  def get_elements_headers(self):
    article = self.get_element_main_article()
    header_elements = article.find_elements(By.TAG_NAME, 'strong')
    header_text = []
    for i in range(len(header_elements)):
      header_text.append(header_elements[i].text)
    return header_text
  
  def get_element_aside_still_have_questions(self):
    return self.get_section_by_aria_label('aside', 'Still have questions?')
  
  def get_text_still_have_questions_header(self):
    questions_section = self.get_element_aside_still_have_questions()
    return self.get_text_section_header(questions_section)
  
  def get_text_still_have_questions_body(self):
    questions_section = self.get_element_aside_still_have_questions()
    return questions_section.find_element(By.XPATH, './/div/div/div[1]').text
  
  def click_element_still_have_questions_button_1(self):
    html = self.get_html()
    questions_section = self.get_element_aside_still_have_questions()
    self.click_element_section_button(questions_section)
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def click_element_still_have_questions_button_2(self):
    html = self.get_html()
    questions_section = self.get_element_aside_still_have_questions()
    questions_section.find_element(By.XPATH, './/div/div/div[2]/a[2]').click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  