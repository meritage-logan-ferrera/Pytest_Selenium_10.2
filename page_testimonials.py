from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_base import BasePage  

class TestimonialsPage(BasePage):
  def get_text_main_header(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/header/div[1]/div/div/div/h1").text
  
  def get_text_main_sub_header(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/header/div[1]/div/div/div/p").text
  
  def click_element_play_button(self):
    self.driver.find_element(By.XPATH, "/html/body/main/header/div[1]/div/div/div/a").click()

  # One overlay is used for every video. How to distinguish?
  def get_element_youtube_overlay(self):
    return self.driver.find_element(By.XPATH, "/html/body/div[4]")
    #display block

  def get_text_section_header(self, section):
    header = section.find_element(By.TAG_NAME, 'h2')
    return header.text
  
  def get_text_section_body(self, section):
    body = section.find_element(By.TAG_NAME, 'p')
    return body.text
  
  def click_element_section_button(self, section):
    section.find_element(By.TAG_NAME, 'a').click()
  
  def get_element_section_placeholder_image(self, section):
    return section.find_element(By.TAG_NAME, "img")
    
  def click_element_section_play_button(self, section):
    section.find_element(By.CLASS_NAME, "video-trigger").click()

  def get_element_aside_1(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/aside[1]")

  def get_text_aside_1_header(self):
    aside_1 = self.get_element_aside_1()
    return self.get_text_section_header(aside_1)
  
  def get_text_aside_1_body(self):
    aside_1 = self.get_element_aside_1()
    return self.get_text_section_body(aside_1)
  
  def click_element_aside_1_button(self):
    aside_1 = self.get_element_aside_1()
    self.click_element_section_button(aside_1)
  
  def get_element_section_1_row(self, number):
    return self.driver.find_element(By.XPATH, f"/html/body/main/article[1]/div/div/div[{number}]")

  def get_text_row_header(self, number):
    row = self.get_element_section_1_row(number)
    return self.get_text_section_header(row)
  
  def get_text_row_body(self, number):
    row = self.get_element_section_1_row(number)
    return self.get_text_section_body(row)
  
  def click_element_row_button(self, number):
    row = self.get_element_section_1_row(number)
    self.click_element_section_button(row)
  
  def get_element_row_image(self, number):
    row = self.get_element_section_1_row(number)
    return self.get_element_section_placeholder_image(row)
  
  def click_element_row_play_button(self, number):
    row = self.get_element_section_1_row(number)
    return self.click_element_section_play_button(row)