from base_page import BasePage
from selenium.webdriver.common.by import By

class StatePage(BasePage):
  def get_element_breadcrumbs_house(self):
    return self.driver.find_element(By.CLASS_NAME, "fa.fa-home")

  def get_text_breadcrumbs_header(self):
    header = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/nav/ul/li[2]/span")
    return header.text
  
  def get_text_state_header(self):
    header = self.driver.find_element(By.XPATH, "/html/body/header/div[1]/div/div[1]/div/h1")
    return header.text
  
  def get_text_state_sub_header(self):
    sub_header = self.driver.find_element(By.XPATH, "/html/body/header/div[1]/div/div[1]/div/p")
    return sub_header.text
  
  def get_text_scroll_down_arrow(self):
    arrow_text = self.driver.find_element(By.XPATH, "/html/body/header/div[2]/p")
    return arrow_text.text
  
  def get_element_scroll_down_arrow(self):
    return self.driver.find_element(By.XPATH, "/html/body/header/div[2]/a")
    
  def click_element_scroll_down_arrow(self):
    scroll_down_arrow = self.get_element_scroll_down_arrow()
    scroll_down_arrow.click()
  
  def get_element_aside(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/aside[1]")
  
  def get_text_aside_header(self):
    aside = self.get_element_aside()
    header = aside.find_element(By.TAG_NAME, "h2")
    return header.text

  def get_text_aside_sub_header(self):
    aside = self.get_element_aside()
    sub_header = aside.find_element(By.CSS_SELECTOR, "p:nth-child(3)")
    return sub_header.text

  