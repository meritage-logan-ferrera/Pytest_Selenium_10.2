from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_base import BasePage
import time  

class BuyerResourcesPage(BasePage):
  def get_text_main_header(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/header/div/div/h1').text

  def get_text_main_sub_header(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/header/div/div/div').text
  
  def get_element_article_affiliates(self):
    return self.get_section_by_aria_label('article', 'Meet our preferred affiliates.')
  
  def get_text_affiliates_header(self):
    affiliates_section = self.get_element_article_affiliates()
    return self.get_text_section_header(affiliates_section)
  
  def get_text_affiliates_body(self):
    affiliates_section = self.get_element_article_affiliates()
    return affiliates_section.find_element(By.CLASS_NAME, 'small-12.column').text
  
  def get_elements_affiliates_columns(self):
    affiliates_section = self.get_element_article_affiliates()
    return affiliates_section.find_elements(By.CLASS_NAME, 'column')
  
  def get_element_affiliates_image(self, number):
    columns = self.get_elements_affiliates_columns()
    return columns[number].find_element(By.TAG_NAME, 'img')
  
  def click_element_affiliates_image(self, number):
    html = self.get_html()
    columns = self.get_elements_affiliates_columns()
    columns[number].click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_element_article_homebuying(self):
    return self.get_section_by_aria_label('article', 'Homebuying process')
  
  def get_text_homebuying_header(self):
    homebuying_section = self.get_element_article_homebuying()
    return self.get_text_section_header(homebuying_section)
  
  def get_text_homebuying_body(self):
    homebuying_section = self.get_element_article_homebuying()
    return self.get_text_section_body(homebuying_section)
  
  def click_element_homebuying_button(self):
    html = self.get_html()
    homebuying_section = self.get_element_article_homebuying()
    self.click_element_section_button(homebuying_section)
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_element_homebuying_image_1(self):
    homebuying_section = self.get_element_article_homebuying()
    return homebuying_section.find_element(By.XPATH, './/div/div[2]/div/div[1]/a/img')
  
  def get_element_homebuying_image_2(self):
    homebuying_section = self.get_element_article_homebuying()
    return homebuying_section.find_element(By.XPATH, './/div/div[2]/div/div[2]/a/img')
  
  def click_element_homebuying_image_1(self):
    html = self.get_html()
    homebuying_section = self.get_element_article_homebuying()
    homebuying_section.find_element(By.XPATH, './/div/div[2]/div/div[1]/a').click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def click_element_homebuying_image_2(self):
    html = self.get_html()
    homebuying_section = self.get_element_article_homebuying()
    homebuying_section.find_element(By.XPATH, './/div/div[2]/div/div[2]/a').click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_text_homebuying_container_1_header(self):
    homebuying_section = self.get_element_article_homebuying()
    return homebuying_section.find_element(By.XPATH, './/div/div[2]/div/div[1]/a/div/div/h4').text

  def get_text_homebuying_container_2_header(self):
    homebuying_section = self.get_element_article_homebuying()
    return homebuying_section.find_element(By.XPATH, './/div/div[2]/div/div[2]/a/div/div/h4').text
  
  def get_text_homebuying_container_1_body(self):
    homebuying_section = self.get_element_article_homebuying()
    return homebuying_section.find_element(By.XPATH, './/div/div[2]/div/div[1]/a/div/div/p').text

  def get_text_homebuying_container_2_body(self):
    homebuying_section = self.get_element_article_homebuying()
    return homebuying_section.find_element(By.XPATH, './/div/div[2]/div/div[2]/a/div/div/p').text
  
  def get_element_article_energy_efficiency(self):
    return self.get_section_by_aria_label('article', 'Energy efficiency')
  
  def get_text_energy_efficiency_header(self):
    energy_efficiency_section = self.get_element_article_energy_efficiency()
    return self.get_text_section_header(energy_efficiency_section)
  
  def get_text_energy_efficiency_body(self):
    energy_efficiency_section = self.get_element_article_energy_efficiency()
    return energy_efficiency_section.find_element(By.TAG_NAME, 'span').text
  
  def click_element_energy_efficiency_button(self):
    html = self.get_html()
    energy_efficiency_section = self.get_element_article_energy_efficiency()
    self.click_element_section_button(energy_efficiency_section)
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_element_energy_efficiency_image_1(self):
    energy_efficiency_section = self.get_element_article_energy_efficiency()
    return energy_efficiency_section.find_element(By.XPATH, './/div/div[1]/div/div[1]/a/img')
  
  def get_element_energy_efficiency_image_2(self):
    energy_efficiency_section = self.get_element_article_energy_efficiency()
    return energy_efficiency_section.find_element(By.XPATH, './/div/div[1]/div/div[2]/a/img')
  
  def click_element_energy_efficiency_image_1(self):
    html = self.get_html()
    energy_efficiency_section = self.get_element_article_energy_efficiency()
    energy_efficiency_section.find_element(By.XPATH, './/div/div[1]/div/div[1]/a').click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def click_element_energy_efficiency_image_2(self):
    html = self.get_html()
    energy_efficiency_section = self.get_element_article_energy_efficiency()
    energy_efficiency_section.find_element(By.XPATH, './/div/div[1]/div/div[2]/a').click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_text_energy_efficiency_container_1_header(self):
    energy_efficiency_section = self.get_element_article_energy_efficiency()
    return energy_efficiency_section.find_element(By.XPATH, './/div/div[1]/div/div[1]/a/div/div/h4').text

  def get_text_energy_efficiency_container_2_header(self):
    energy_efficiency_section = self.get_element_article_energy_efficiency()
    return energy_efficiency_section.find_element(By.XPATH, './/div/div[1]/div/div[2]/a/div/div/h4').text
  
  def get_text_energy_efficiency_container_1_body(self):
    energy_efficiency_section = self.get_element_article_energy_efficiency()
    return energy_efficiency_section.find_element(By.XPATH, './/div/div[1]/div/div[1]/a/div/div/p').text

  def get_text_energy_efficiency_container_2_body(self):
    energy_efficiency_section = self.get_element_article_energy_efficiency()
    return energy_efficiency_section.find_element(By.XPATH, './/div/div[1]/div/div[2]/a/div/div/p').text
  
  def get_element_article_home_design(self):
    return self.get_section_by_aria_label('article', 'Home design')
  
  def get_text_home_design_header(self):
    home_design_section = self.get_element_article_home_design()
    return self.get_text_section_header(home_design_section)
  
  def get_text_home_design_body(self):
    home_design_section = self.get_element_article_home_design()
    return self.get_text_section_body(home_design_section)
  
  def click_element_home_design_button(self):
    html = self.get_html()
    home_design_section = self.get_element_article_home_design()
    self.click_element_section_button(home_design_section)
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_element_home_design_image_1(self):
    home_design_section = self.get_element_article_home_design()
    return home_design_section.find_element(By.XPATH, './/div/div[2]/div/div[1]/a/img')
  
  def get_element_home_design_image_2(self):
    home_design_section = self.get_element_article_home_design()
    return home_design_section.find_element(By.XPATH, './/div/div[2]/div/div[2]/a/img')
  
  def click_element_home_design_image_1(self):
    html = self.get_html()
    home_design_section = self.get_element_article_home_design()
    home_design_section.find_element(By.XPATH, './/div/div[2]/div/div[1]/a').click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def click_element_home_design_image_2(self):
    html = self.get_html()
    home_design_section = self.get_element_article_home_design()
    home_design_section.find_element(By.XPATH, './/div/div[2]/div/div[2]/a').click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_text_home_design_container_1_header(self):
    home_design_section = self.get_element_article_home_design()
    return home_design_section.find_element(By.XPATH, './/div/div[2]/div/div[1]/a/div/div/h4').text

  def get_text_home_design_container_2_header(self):
    home_design_section = self.get_element_article_home_design()
    return home_design_section.find_element(By.XPATH, './/div/div[2]/div/div[2]/a/div/div/h4').text
  
  def get_text_home_design_container_1_body(self):
    home_design_section = self.get_element_article_home_design()
    return home_design_section.find_element(By.XPATH, './/div/div[2]/div/div[1]/a/div/div/p').text

  def get_text_home_design_container_2_body(self):
    home_design_section = self.get_element_article_home_design()
    return home_design_section.find_element(By.XPATH, './/div/div[2]/div/div[2]/a/div/div/p').text
  
  def get_aside_ready_to_find(self):
    return self.get_section_by_aria_label('aside', 'Ready to find your home?')
  
  def get_ready_to_find_header(self):
    ready_section = self.get_aside_ready_to_find()
    return self.get_text_section_header(ready_section)
  
  def get_ready_to_find_body(self):
    ready_section = self.get_aside_ready_to_find()
    return self.get_text_section_body(ready_section)
  
  def click_element_ready_to_find_button(self):
    html = self.get_html()
    ready_section = self.get_aside_ready_to_find()
    self.click_element_section_button(ready_section)
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))

