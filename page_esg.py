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
    html = self.get_html()
    no_title_aside = self.get_element_aside_no_title()
    no_title_aside.find_element(By.CLASS_NAME, 'button.button--blue--solid.view').click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
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
    environmental_section.find_element(By.CLASS_NAME, 'button.button--blue').click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_element_article_social_corporate(self):
    return self.get_section_by_aria_label('article', 'Social: Corporate Social Responsibility')
  
  def get_element_social_corporate_image(self):
    social_corporate_section = self.get_element_article_social_corporate()
    return self.get_element_section_placeholder_image(social_corporate_section)
  
  def get_elements_social_corporate_body(self):
    social_corporate_section = self.get_element_article_social_corporate()
    return social_corporate_section.find_elements(By.TAG_NAME, 'p')
  
  def get_text_social_corporate_header(self):
    social_corporate_section = self.get_element_article_social_corporate()
    return self.get_text_section_header(social_corporate_section)
  
  def click_element_social_corporate_button(self):
    html = self.get_html()
    social_corporate_section = self.get_element_article_social_corporate()
    social_corporate_section.find_element(By.CLASS_NAME, 'button.button--blue').click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_element_article_social_philanthropy(self):
    return self.get_section_by_aria_label('article', 'Social: Service & Philanthropy')
  
  def get_element_social_philanthropy_image(self):
    social_philanthropy_section = self.get_element_article_social_philanthropy()
    return self.get_element_section_placeholder_image(social_philanthropy_section)
  
  def get_elements_social_philanthropy_body(self):
    social_philanthropy_section = self.get_element_article_social_philanthropy()
    return social_philanthropy_section.find_elements(By.TAG_NAME, 'p')
  
  def get_text_social_philanthropy_header(self):
    social_philanthropy_section = self.get_element_article_social_philanthropy()
    return self.get_text_section_header(social_philanthropy_section)
  
  def click_element_social_philanthropy_button(self):
    html = self.get_html()
    social_philanthropy_section = self.get_element_article_social_philanthropy()
    self.click_element_section_button(social_philanthropy_section)
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_element_article_corporate_governance(self):
    return self.get_section_by_aria_label('article', 'Corporate Governance')
  
  def get_element_corporate_governance_image(self):
    corporate_governance_section = self.get_element_article_corporate_governance()
    return self.get_element_section_placeholder_image(corporate_governance_section)
  
  def get_elements_corporate_governance_body(self):
    corporate_governance_section = self.get_element_article_corporate_governance()
    return corporate_governance_section.find_elements(By.TAG_NAME, 'p')
  
  def get_text_corporate_governance_header(self):
    corporate_governance_section = self.get_element_article_corporate_governance()
    return self.get_text_section_header(corporate_governance_section)
  
  def click_element_corporate_governance_button(self):
    html = self.get_html()
    corporate_governance_section = self.get_element_article_corporate_governance()
    corporate_governance_section.find_element(By.CLASS_NAME, 'button.button--blue').click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_element_article_quote(self):
    return self.get_section_by_aria_label('article', 'ESG')
  
  def get_text_quote(self):
    quote_section = self.get_element_article_quote()
    return self.get_text_section_header(quote_section)
  
  def get_text_quote_body(self):
    quote_section = self.get_element_article_quote()
    return self.get_text_section_body(quote_section)
  
