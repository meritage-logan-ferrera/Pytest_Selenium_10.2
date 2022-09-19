from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_base import BasePage
import time  

class HowWeBuildPage(BasePage):
  def get_text_main_header(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/header/div/div/h1')
    
  def get_text_main_sub_header(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/header/div/div/')
  
  def get_element_article_successful(self):
    return self.get_section_by_aria_label('article', 'A successful build involves two key components.')
  
  def get_text_successful_header(self):
    successful_section = self.get_element_article_successful()
    return self.get_text_section_header(successful_section)
  
  def get_element_article_successful_div_column(self, number):
    successful_section = self.get_element_article_successful()
    return successful_section.find_element(By.XPATH, f"(.//div[@class='column'])[{number}]")
  
  def get_element_successful_div_column_image(self, number):
    column = self.get_element_successful_div_column_image(number)
    return self.get_element_section_placeholder_image(column)
  
  def get_text_successful_div_column_header(self, number):
    column = self.get_element_successful_div_column_image(number)
    return column.find_element(By.TAG_NAME, 'h3')
  
  def get_text_successful_div_column_body(self, number):
    column = self.get_element_successful_div_column_image(number)
    return self.get_text_section_body(column)
  
  def get_element_section_1(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/section")
  
  def get_element_section_1_drop_down_container(self, number):
    section_1 = self.get_element_section_1()
    return section_1.find_element(By.XPATH, f"/html/body/main/section/div/div[2]/div/ul[1]/li[{number}]")
  
  def get_element_section_1_drop_down_container_image(self, number):
    container = self.get_element_section_1_drop_down_container(number)
    return container.find_element(By.TAG_NAME, "img")
  
  def get_text_section_1_drop_down_container_header(self, number):
    container = self.get_element_section_1_drop_down_container(number)
    return container.find_element(By.TAG_NAME, "span").text
  
  def click_element_section_1_drop_down(self, number):
    container = self.get_element_section_1_drop_down_container(number)
    container.click()
  
  def get_element_section_1_responsive_tabs(self):
    section_1 = self.get_element_section_1()
    return section_1.find_element(By.XPATH, "/html/body/main/section/div/div[2]/div/ul[2]")
  
  def get_element_section_1_responsive_tab(self, number):
    tabs_container = self.get_element_section_1_responsive_tabs()
    return tabs_container.find_element(By.ID, f"tab-{number}-title")
    # classlist is-active

  def get_text_section_1_responsive_tab_header(self, number):
    tab = self.get_element_section_1_responsive_tab(number)
    return tab.find_element(By.TAG_NAME, "h2").text
  
  def get_elements_section_1_responsive_tab_body(self, number):
    tab = self.get_element_section_1_responsive_tab(number)
    return tab.find_elements(By.TAG_NAME, "p")
  
  def get_element_section_1_responsive_tab_image(self, number):
    tab = self.get_element_section_1_responsive_tab(number)
    return tab.find_element(By.TAG_NAME, "img")
  
  def get_element_section_pro_tip(self):
    return self.get_section_by_aria_label('article', 'How we build Testimonial')
  
  def get_element_pro_tip_current_slide(self):
    tip_section = self.get_element_section_pro_tip()
    return tip_section.find_element(By.XPATH, ".//li[contains(@class, 'slick-current')]")
  
  def get_text_pro_tip_header(self):
    current_slide = self.get_element_pro_tip_current_slide()
    return current_slide.find_element(By.TAG_NAME, 'h2')
  
  def get_text_pro_tip_body(self):
    current_slide = self.get_element_pro_tip_current_slide()
    return current_slide.text
  
  def click_element_next_arrow(self):
    tip_section = self.get_element_section_pro_tip()
    tip_section.find_element(By.XPATH, './/div/div/ul/button[2]').click()
  
  def get_element_article_quality_of_your_home(self):
    return self.driver.find_element(By.ID, 'how-we-build')
  
  def get_text_quality_header(self):
    quality_section = self.get_element_article_quality_of_your_home()
    return self.get_text_section_header(quality_section)
  
  def get_elements_quality_body(self):
    quality_section = self.get_element_article_quality_of_your_home()
    return quality_section.find_elements(By.TAG_NAME, 'p')
  
  def get_element_section_slider(self):
    return self.driver.find_element(By.ID, 'how-we-build-slider')
  
  def get_element_active_slide(self):
    slider_section = self.get_element_section_slider()
    return slider_section.find_element(By.XPATH, ".//li[contains(@class, 'is-active')]")
  
  