from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_base import BasePage
import time  

class PrivacyPolicyPage(BasePage):
  def get_text_main_header(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/article/header/div/h2').text
  
  def get_element_main_article(self):
    return self.get_section_by_aria_label('article', 'Privacy Policy')
  
  def get_elements_headers(self):
    article = self.get_element_main_article()
    header_elements = article.find_elements(By.TAG_NAME, 'strong')
    header_text = []
    for i in range(len(header_elements)):
      header_text.append(header_elements[i].text)
    return header_text
  
  def get_element_image_1(self):
    article = self.get_element_main_article()
    return article.find_element(By.XPATH, ".//img[@alt='Privacy Policy 1']")
  
  def get_element_image_2(self):
    article = self.get_element_main_article()
    return article.find_element(By.XPATH, ".//img[@alt='Privacy Policy 2']")
  
  def get_element_plain_button_terms(self):
    article = self.get_element_main_article()
    return article.find_element(By.XPATH, ".//div/div/p[4]/span/a")

  def get_element_plain_button_clicking_here(self):
    article = self.get_element_main_article()
    return article.find_element(By.XPATH, ".//div/div/div/p[6]/span[2]/a")

  def get_element_plain_button_visiting_request(self):
    article = self.get_element_main_article()
    return article.find_element(By.XPATH, ".//div/div/ul[6]/li[2]/a")
  
  def click_element_plain_button_terms(self):
    html = self.get_html()
    button = self.get_element_plain_button_terms()
    button.click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))

  def click_element_plain_button_clicking_here(self):
    original_window = self.driver.current_window_handle
    button = self.get_element_plain_button_clicking_here()
    button.click()
    self.new_tab(original_window)

  def click_element_plain_button_visiting_request(self):
    original_window = self.driver.current_window_handle
    button = self.get_element_plain_button_visiting_request()
    button.click()
    self.new_tab(original_window)

  def get_element_aside_still_have_questions(self):
    return self.get_section_by_aria_label('aside', 'Still have questions?')
  
  def get_text_still_have_questions_header(self):
    questions_section = self.get_element_aside_still_have_questions()
    return self.get_text_section_header(questions_section)
  
  def get_text_still_have_questions_body(self):
    questions_section = self.get_element_aside_still_have_questions()
    return self.get_text_section_body(questions_section)
  
  def click_element_still_have_questions_button(self):
    html = self.get_html()
    questions_section = self.get_element_aside_still_have_questions()
    self.click_element_section_button(questions_section)
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))