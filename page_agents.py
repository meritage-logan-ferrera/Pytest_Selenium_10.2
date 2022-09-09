from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_base import BasePage
import time  

class AgentsPage(BasePage):
  def click_element_play_button(self):
    return self.driver.find_element(By.XPATH, "//*[@id='quick-home-search-hero']/div[1]/div/div/div/a")
  
  def get_text_main_header(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/header/div/div/h1').text
  
  def get_text_main_sub_header(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/header/div/div/p').text
  
  def click_elemenet_main_button_1(self):
    self.driver.find_element(By.XPATH, '/html/body/main/header/div/div/a[1]')
  
  def click_elemenet_main_button_2(self):
    self.driver.find_element(By.XPATH, '/html/body/main/header/div/div/a[2]')
  
  def get_element_aside_1_when_you_sell_with_us(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/aside[1]')
  
  def get_text_aside_1_header(self):
    aside_1 = self.get_element_aside_1_when_you_sell_with_us()
    return self.get_text_section_header(aside_1)
  
  def get_text_aside_1_body(self):
    aside_1 = self.get_element_aside_1_when_you_sell_with_us()
    return self.get_text_section_body(aside_1)
  
  def get_element_aside_1_image(self):
    aside_1 = self.get_element_aside_1_when_you_sell_with_us()
    return self.get_element_section_placeholder_image(aside_1)
  
  def get_element_article_1(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/article[1]')
  
  def get_element_article_1_container(self, number):
    article_1 = self.get_element_article_1()
    return article_1.find_element(By.XPATH, f'/html/body/main/article[1]/div/div/div[2]/div[{number}]')
  
  def get_text_article_1_container_header(self, number):
    container = self.get_element_article_1_container(number)
    return container.find_element(By.TAG_NAME, 'h3').text
  
  def get_text_article_1_container_body(self, number):
    container = self.get_element_article_1_container(number)
    return self.get_text_section_body(container)
  
  def get_element_article_1_container_image(self, number):
    container = self.get_element_article_1_container(number)
    return self.get_element_section_placeholder_image(container)
  
  def get_element_article_2_meritage_agent_terms(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/article[2]')
  
  def get_text_article_2_call_header(self):
    article_2 = self.get_element_article_2_meritage_agent_terms()
    return article_2.find_element(By.TAG_NAME, 'h3').text
  
  def get_text_article_2_header(self):
    article_2 = self.get_element_article_2_meritage_agent_terms()
    return article_2.find_element(By.XPATH, '/html/body/main/article[2]/header/div/p[3]/strong').text
  
  
