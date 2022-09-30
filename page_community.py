from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_base import BasePage  

class CommunityPage(BasePage):
  def get_element_image_carousel(self):
    return self.driver.find_element(By.ID, 'Orchard and Woodland')
  
  def click_element_next_arrow(self):
    carousel_section = self.get_element_image_carousel()
    carousel_section.find_element(By.CLASS_NAME, 'orbit-next.slick-arrow').click()
  
  def get_elements_carousel_slides(self):
    carousel_section = self.get_element_image_carousel()
    slides = carousel_section.find_elements(By.XPATH, ".//li[contains(@class, 'slick-slide') and not contains(@class, 'slick-cloned')]")
    return slides
  
  def get_element_current_slide(self):
    carousel_section = self.get_element_image_carousel()
    return carousel_section.find_element(By.XPATH, ".//li[contains(@class, 'is-active')]")
  
  def get_element_compare(self):
    carousel_section = self.get_element_image_carousel()
    return carousel_section.find_element(By.CLASS_NAME, 'trigger-compare.top.has-tip')
  
  def get_element_heart(self):
    carousel_section = self.get_element_image_carousel()
    return carousel_section.find_element(By.CLASS_NAME, 'add-community-favorite')
  
  def get_element_article(self):
    return self.driver.find_element(By.CLASS_NAME, 'small-12.medium-10.large-8.column.text-center')
  
  def get_text_main_header(self):
    article = self.get_element_article()
    return article.find_element(By.TAG_NAME, 'h1').text
  
  def get_text_main_body(self):
    article = self.get_element_article()
    return article.find_element(By.TAG_NAME, 'p').text
  
  def get_element_aside(self):
    return self.driver.find_element(By.CLASS_NAME, 'multi-column-info.has-dividers')
  
  def get_text_aside(self):
    aside = self.get_element_aside()
    return aside.text
  
  def get_element_brochure(self):
    return self.driver.find_element(By.XPATH, "//div[@class='small-12 columns text-center']/a")
  
  def get_element_section_tabs(self):
    return self.driver.find_element(By.CLASS_NAME, 'tabbed-accordion    ')
  
  def get_element_tabs_header(self):
    tabs_section = self.get_element_section_tabs()
    return tabs_section.find_element(By.TAG_NAME, 'h2')
  
  def get_element_tabs_body(self):
    tabs_section = self.get_element_section_tabs()
    return tabs_section.find_element(By.TAG_NAME, 'p')
  
  def get_elements_tabs(self):
    tabs_section = self.get_element_section_tabs()
    tabs_container = tabs_section.find_element(By.XPATH, ".//ul[contains(@id, 'tab-container')]")
    return tabs_container.find_elements(By.TAG_NAME, 'li')
  
  def get_element_tab_image(self, number):
    tabs = self.get_elements_tabs()
    return tabs[number].find_element(By.TAG_NAME, 'img')
  
  def get_text_tab_name(self, number):
    tabs = self.get_elements_tabs()
    return tabs[number].find_element(By.TAG_NAME, 'span').text
  
  def click_element_tab(self, number):
    tabs = self.get_elements_tabs()
    tabs[number].click()

  def get_element_active_info_tab(self, number):
    tabs_section = self.get_element_section_tabs()
    info_tab_container = tabs_section.find_element(By.CLASS_NAME, 'responsive-tabstabs-content')
    return info_tab_container.find_element(By.XPATH, f".//li[{number}]")
  
  def get_element_info_tab_overview(self):
    return self.get_element_active_info_tab(1)
  
  def get_text_community_address(self):
    overview_info_tab = self.get_element_info_tab_overview()
    return overview_info_tab.find_element(By.XPATH, ".//p[@v-if='community']").text
    # string includes mroe than just a comma
  
  def get_element_directions_link(self):
    overview_info_tab = self.get_element_info_tab_overview()
    return overview_info_tab.find_element(By.XPATH, './/div/section/div/div/div[2]/div/div[1]/a')
  
  def get_text_below_directions(self):
    overview_info_tab = self.get_element_info_tab_overview()
    return overview_info_tab.find_element(By.XPATH, './/div/section/div/div/div[2]/div/div[1]/p[2]').text
    #assert string is not empty

  

