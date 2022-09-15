from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_base import BasePage
import time  

class AboutUsPage(BasePage):
  def get_text_main_header(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/header/div/div/h1').text

  def get_text_main_sub_header(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/header/div/div/p').text
  
  def get_element_article_building_for_you(self):
    return self.driver.find_element(By.XPATH, "//article[@aria-label='Building for you, at a higher standard.']")
  
  def get_text_building_header(self):
    building_section = self.get_element_article_building_for_you()
    return self.get_text_section_header(building_section)
  
  def get_text_building_body(self):
    building_section = self.get_element_article_building_for_you()
    return self.get_text_section_body(building_section)
  
  def get_element_building_section_container(self, element):
    building_section = self.get_element_article_building_for_you()
    return building_section.find_element(By.XPATH, f".//div/div/div[2]/div[{element}]")

  def get_element_building_section_container_image(self, element):
    container = self.get_element_building_section_container(element)
    return container.find_element(By.TAG_NAME, "img")
  
  def get_text_building_section_container_pre_heading(self, element):
    container = self.get_element_building_section_container(element)
    return container.find_element(By.CLASS_NAME, "pre-heading").text

  def get_text_building_section_container_header(self, element):
    container = self.get_element_building_section_container(element)
    header = container.find_element(By.TAG_NAME, "h3")
    return header.text
  
  def get_text_building_section_container_description(self, element):
    container = self.get_element_building_section_container(element)
    return container.find_element(By.TAG_NAME, "p").text
  
  def click_element_building_section_button(self):
    html = self.get_html()
    building_section = self.get_element_article_building_for_you()
    self.click_element_section_button(building_section)
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_element_article_earning_the_right(self):
    return self.driver.find_element(By.XPATH, "//article[@aria-label='Earning the right to be your builder.']")
  
  def get_text_earning_header(self):
    earning_section = self.get_element_article_earning_the_right()
    return self.get_text_section_header(earning_section)
  
  def get_text_earning_sub_header(self):
    earning_section = self.get_element_article_earning_the_right()
    return earning_section.find_element(By.TAG_NAME, 'h4').text
  
  def get_text_earning_body(self):
    earning_section = self.get_element_article_earning_the_right()
    return self.get_text_section_body(earning_section)
  
  def get_element_earning_image(self):
    earning_section = self.get_element_article_earning_the_right()
    return self.get_element_section_placeholder_image(earning_section)
  
  def click_element_earning_button(self):
    html = self.get_html()
    earning_section = self.get_element_article_earning_the_right()
    self.click_element_section_button(earning_section)
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))

  def click_element_earning_play_button(self):
    earning_section = self.get_element_article_earning_the_right()
    self.click_element_section_play_button(earning_section)

  def get_element_article_track_record(self):
    return self.driver.find_element(By.XPATH, "//article[@aria-label='Building a track record of success.']")
  
  def get_text_track_header(self):
    track_section = self.get_element_article_track_record()
    return self.get_text_section_header(track_section)
  
  def get_text_track_body(self):
    track_section = self.get_element_article_track_record()
    return self.get_text_section_body(track_section)
  
  def click_element_track_button(self):
    html = self.get_html()
    track_section = self.get_element_article_track_record()
    self.click_element_section_button(track_section)
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))

  def get_elements_track_images(self):
    track_section = self.get_element_article_track_record()
    images = track_section.find_elements(By.XPATH, ".//div[@class='column']/span/img")
    return images
  
  def get_element_section_giving_back(self):
    return self.driver.find_element(By.XPATH, "//article[@aria-label='Giving back where we build.']")
  
  def get_text_giving_back_header(self):
    giving_section = self.get_element_section_giving_back()
    return self.get_text_section_header(giving_section)
  
  def get_text_giving_back_body(self):
    giving_section = self.get_element_section_giving_back()
    return self.get_text_section_body(giving_section)
  
  def get_text_giving_back_sub_header(self):
    giving_section = self.get_element_section_giving_back()
    return giving_section.find_element(By.TAG_NAME, 'h4').text
  
  def get_text_giving_back_sub_header_body(self):
    giving_section = self.get_element_section_giving_back()
    return giving_section.find_element(By.XPATH, './/div/div[1]/p[1]').text
  
  def click_element_giving_back_button(self):
    html = self.get_html()
    giving_section = self.get_element_section_giving_back()
    self.click_element_section_button(giving_section)
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_element_giving_back_image(self):
    giving_section = self.get_element_section_giving_back()
    return self.get_element_section_placeholder_image(giving_section)
  
  def get_element_section_great_careers(self):
    return self.driver.find_element(By.XPATH, "//article[@aria-label='We build great careers, too.']")
  
  def get_text_great_careers_header(self):
    great_careers_section = self.get_element_section_great_careers()
    return great_careers_section.find_element(By.TAG_NAME, 'h4').text
  
  def get_text_great_careers_body(self):
    great_careers_section = self.get_element_section_great_careers()
    return self.get_text_section_body(great_careers_section)
  
  def click_element_great_careers_button(self):
    html = self.get_html()
    great_careers_section = self.get_element_section_great_careers()
    self.click_element_section_button(great_careers_section)
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_element_great_careers_image(self):
    great_careers_section = self.get_element_section_great_careers()
    return self.get_element_section_placeholder_image(great_careers_section)
  
  def get_element_section_building_where_you_want(self):
    return self.driver.find_element(By.XPATH, "//aside[@aria-label='Building where you want to live.']")
  
  def get_text_building_where_header(self):
    building_where_section = self.get_element_section_building_where_you_want()
    return self.get_text_section_header(building_where_section)
  
  def get_text_building_where_body(self):
    building_where_section = self.get_element_section_building_where_you_want()
    return self.get_text_section_body(building_where_section)
  
  def click_element_building_where_button(self):
    html = self.get_html()
    building_where_section = self.get_element_section_building_where_you_want()
    self.click_element_section_button(building_where_section)
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  