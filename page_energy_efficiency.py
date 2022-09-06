from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_base import BasePage
import time  

class EnergyEfficiencyPage(BasePage):
  def click_element_play_button(self):
    return self.driver.find_element(By.XPATH, "//*[@id='quick-home-search-hero']/div[1]/div/div/div/a")

  def get_element_youtube_overlay(self):
    return self.driver.find_element(By.XPATH, "/html/body/div[4]")
  
  def get_element_section_1(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/section")
  
  # Literally same code as Why Meritage accordian tabs
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
  
  # Same code for testing the dyanmic responsive tab that opens after pressing the above tabs as from Why Meritage page
  def get_element_section_1_responsive_tabs(self):
    section_1 = self.get_element_section_1()
    return section_1.find_element(By.XPATH, "/html/body/main/section/div/div[2]/div/ul[2]")
  
  def get_element_section_1_responsive_tab(self, number):
    tabs_container = self.get_element_section_1_responsive_tabs()
    return tabs_container.find_element(By.ID, f"tab-{number}-title")

  def get_text_section_1_responsive_tab_header(self, number):
    tab = self.get_element_section_1_responsive_tab(number)
    return tab.find_element(By.TAG_NAME, "h2").text
  
  # This is different from the same funciton in Why Meritage. We only need to find one element here.
  def get_text_section_1_responsive_tab_body(self, number):
    return self.driver.find_element(By.CSS_SELECTOR, f"#tab-{number}-title > div:nth-child(2) > article:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > p:nth-child(3)").text
  
  def click_element_section_1_responsive_tab_button(self, number):
    html = BasePage(self.driver).get_html()
    tab = self.get_element_section_1_responsive_tab(number)
    tab.find_element(By.CLASS_NAME, "button.button--blue--solid.view").click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_element_section_1_responsive_tab_image(self, number):
    tab = self.get_element_section_1_responsive_tab(number)
    return tab.find_element(By.TAG_NAME, "img")
  
  def get_element_article_1(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/article[1]')
  
  # h4 not h2
  def get_text_article_1_header(self):
    article_1 = self.get_element_article_1()
    return article_1.find_element(By.TAG_NAME, 'h4')
  
  # text is innerText on div not a p tag
  def get_text_article_1_body(self):
    article_1 = self.get_element_article_1()
    return article_1.find_element(By.XPATH, '/html/body/main/article[1]/div/div[1]')
  
  def get_element_article_1_image(self):
    article_1 = self.get_element_article_1()
    return self.get_element_section_placeholder_image(article_1)
  
  def get_element_donut_section_donut_container(self):
    return self.driver.find_element(By.ID, 'ee-donut-slider')

  def get_element_donut_section_slides_container(self):
    return self.driver.find_element(By.ID, 'donut-slider--slides')

  def get_element_donut_section_current_slick_slide(self):
    # slides_container = self.get_element_donut_section_slides_container()
    # does not get a subset of only the elements with slick-slide
    # when I do slides_container.find_element(By.XPATH, '//li[contains(@class, "slick-slide") and not(contains(@class, "slick-cloned"))]')
    # Theoretically that should do the same thing as what I have now...
    return self.driver.find_element(By.XPATH, f'/html/body/main/div[1]/div[1]/div/div/div/div[2]/div/ul[1]/div/div//li[contains(@class, "slick-active") and contains(@class, "slick-current")]')
  
  def get_text_donut_section_slide_header(self):
    current_slide = self.get_element_donut_section_current_slick_slide()
    return current_slide.find_element(By.TAG_NAME, 'strong').text
  
  def get_text_donut_section_slide_sub_header(self):
    current_slide = self.get_element_donut_section_current_slick_slide()
    return current_slide.find_element(By.TAG_NAME, 'h4').text
  
  def get_text_donut_section_slide_body(self):
    current_slide = self.get_element_donut_section_current_slick_slide()
    return current_slide.find_element(By.TAG_NAME, 'p').text
    
  def click_element_donut_section_right_arrow(self):
    self.driver.find_element(By.XPATH, '/html/body/main/div[1]/div[1]/div/div/div/div[2]/div/div/button[2]').click()
  
  def get_elements_donut_current_slide_buttons(self):
    current_slide = self.get_element_donut_section_current_slick_slide()
    return current_slide.find_elements(By.TAG_NAME, 'li')