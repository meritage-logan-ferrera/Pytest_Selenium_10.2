from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_base import BasePage
import time  

class MeritageCaresPage(BasePage):
  def get_text_main_header(self):
    return self.driver.find_element(By.XPATH, '/html/body/header/div/div/h1').text
  
  def get_text_main_sub_header(self):
    return self.driver.find_element(By.XPATH, '/html/body/header/div/div/p').text

  def get_element_article_putting_our_mission(self):
    return self.driver.find_element(By.XPATH, "//article[@aria-label='Putting Our Mission Into Action']")
  
  def get_text_putting_our_mission_header(self):
    putting_section = self.get_element_article_putting_our_mission()
    return self.get_text_section_header(putting_section)
  
  def get_text_putting_our_mission_body(self):
    putting_section = self.get_element_article_putting_our_mission()
    return self.get_text_section_body(putting_section)
  
  def get_elements_putting_our_mission_column_containers(self):
    putting_section = self.get_element_article_putting_our_mission()
    return putting_section.find_elements(By.XPATH, ".//div[@class='row align-center small-up-1 medium-up-3 ']/div")
  
  def get_text_putting_our_mission_container_header(self, number):
    putting_containers = self.get_elements_putting_our_mission_column_containers()
    return putting_containers[number].find_element(By.TAG_NAME, 'h3').text
  
  def get_text_putting_our_mission_container_body(self, number):
    putting_containers = self.get_elements_putting_our_mission_column_containers()
    return putting_containers[number].find_element(By.XPATH, './/span[2]').text
  
  def get_text_putting_our_mission_container_image(self, number):
    putting_containers = self.get_elements_putting_our_mission_column_containers()
    return putting_containers[number].find_element(By.TAG_NAME, 'img')
  
  def click_element_pdf_button(self):
    html = self.get_html()
    self.driver.find_element(By.XPATH, "/html/body/main/aside[1]/div/div/div/a").click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_element_article_why_we_give(self):
    return self.driver.find_element(By.XPATH, "//article[@aria-label='Why We Give']")
  
  def get_text_why_we_give_header(self):
    why_we_give_section = self.get_element_article_why_we_give()
    return why_we_give_section.find_element(By.TAG_NAME, 'h4').text
  
  def get_text_why_we_give_body(self):
    why_we_give_section = self.get_element_article_why_we_give()
    return self.get_text_section_body(why_we_give_section)
  
  def get_element_why_we_give_image(self):
    why_we_give_section = self.get_element_article_why_we_give()
    return self.get_element_section_placeholder_image(why_we_give_section)

  def get_text_why_we_give_disclaimer(self):
    why_we_give_section = self.get_element_article_why_we_give()
    return why_we_give_section.find_element(By.CLASS_NAME, 'disclaimer').text
  
  def get_element_article_feeding_america(self):
    return self.driver.find_element(By.XPATH, "//article[@aria-label='Feeding America']")
  
  def get_text_feeding_america_header(self):
    feeding_america_section = self.get_element_article_feeding_america()
    return feeding_america_section.find_element(By.TAG_NAME, 'h4').text
  
  def get_text_feeding_america_body(self):
    feeding_america_section = self.get_element_article_feeding_america()
    return feeding_america_section.find_elements(By.TAG_NAME, 'p') #multiple p tags in section
  
  def get_element_feeding_america_image(self):
    feeding_america_section = self.get_element_article_feeding_america()
    return self.get_element_section_placeholder_image(feeding_america_section)
  
  def get_element_article_arizona_housing_fund(self):
    return self.driver.find_element(By.XPATH, "//article[@aria-label='Arizona Housing Fund']")
  
  def get_text_arizona_housing_fund_header(self):
    arizona_housing_fund_section = self.get_element_article_arizona_housing_fund()
    return arizona_housing_fund_section.find_element(By.TAG_NAME, 'h4').text
  
  def get_text_arizona_housing_fund_body(self):
    arizona_housing_fund_section = self.get_element_article_arizona_housing_fund()
    return arizona_housing_fund_section.find_elements(By.TAG_NAME, 'p') #multiple p tags in section
  
  def get_element_arizona_housing_fund_image(self):
    arizona_housing_fund_section = self.get_element_article_arizona_housing_fund()
    return self.get_element_section_placeholder_image(arizona_housing_fund_section)
  
  def click_element_arizona_housing_fund_play_button(self):
    arizona_housing_fund_section = self.get_element_article_arizona_housing_fund()
    self.click_element_section_play_button(arizona_housing_fund_section)

  def get_element_article_giving_milestones(self):
    return self.driver.find_element(By.XPATH, "//article[@aria-label='Giving Milestones']")
  
  def get_text_giving_milestones_header(self):
    giving_section = self.get_element_article_giving_milestones()
    return self.get_text_section_header(giving_section)
  
  def get_text_giving_milestones_body(self):
    giving_section = self.get_element_article_giving_milestones()
    return giving_section.find_element(By.TAG_NAME, 'div').text
  
  def get_element_giving_milestones_div(self):
    return self.driver.find_element(By.CLASS_NAME, 'large-image-block.no-pad-bottom.no-pad-top.no-pad-bottom.no-pad-top')

  def get_element_giving_milestones_image(self):
    giving_section = self.get_element_giving_milestones_div()
    return self.get_element_section_placeholder_image(giving_section)
  
  def get_text_giving_milestones_caption(self):
    giving_section = self.get_element_giving_milestones_div()
    return giving_section.find_element(By.TAG_NAME, 'figcaption').text
  
  def get_element_article_operation_homefront(self):
    return self.get_section_by_aria_label('article', 'Operation Homefront.')
  
  def get_text_operation_homefront_header(self):
    operation_section = self.get_element_article_operation_homefront()
    return self.get_text_section_header(operation_section)
  
  def get_text_operation_homefront_sub_header(self):
    operation_section = self.get_element_article_operation_homefront()
    return operation_section.find_element(By.TAG_NAME, 'h4').text
  
  def get_text_operation_homefront_sub_sub_header(self):
    operation_section = self.get_element_article_operation_homefront()
    return operation_section.find_element(By.XPATH, './/div/div[1]/h4').text

  def get_text_operation_homefront_body(self):
    operation_section = self.get_element_article_operation_homefront()
    return self.get_text_section_body(operation_section)
  
  def get_element_operation_homefront_image(self):
    operation_section = self.get_element_article_operation_homefront()
    return self.get_element_section_placeholder_image(operation_section)
  
  def click_element_operation_homefront_button_1(self):
    html = self.get_html()
    operation_section = self.get_element_article_operation_homefront()
    operation_section.find_element(By.XPATH, './/div/div[1]/p[2]/a[1]').click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def click_element_operation_homefront_button_2(self):
    html = self.get_html()
    operation_section = self.get_element_article_operation_homefront()
    operation_section.find_element(By.XPATH, './/div/div[1]/p[2]/a[2]').click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_element_article_american_flag(self):
    return self.get_section_by_aria_label('article', 'M5 - Meritage Cares - Full Width Quote Block')
  
  def get_text_american_flag_quote(self):
    american_section = self.get_element_article_american_flag()
    return self.get_text_section_header(american_section)
  
  def get_text_american_flag_body(self):
    american_section = self.get_element_article_american_flag()
    return self.get_text_section_body(american_section)

  def get_element_section_where_we_give(self):
    return self.get_section_by_aria_label('section', 'Where we give.')
  
  def get_text_where_we_give_header(self):
    where_section = self.get_element_section_where_we_give()
    return self.get_text_section_header(where_section)
  
  def get_text_where_we_give_body(self):
    where_section = self.get_element_section_where_we_give()
    return self.get_text_section_body(where_section)
  
  def get_element_where_we_give_state_dropdown_container(self, number):
    where_section = self.get_element_section_where_we_give()
    return where_section.find_element(By.XPATH, f'.//li[{number+1}]')
  
  def click_element_current_state(self, number):
    current_state = self.get_element_where_we_give_state_dropdown_container(number)
    current_state.click()
    time.sleep(.2)
  
  def get_elements_where_we_give_current_state_community_efforts(self, number):
    current_state = self.get_element_where_we_give_state_dropdown_container(number)
    community_efforts_container = current_state.find_element(By.TAG_NAME, 'div')
    return community_efforts_container.find_elements(By.TAG_NAME, 'p')
  
  def click_element_where_we_give_scroll_button(self):
    where_section = self.get_element_section_where_we_give()
    where_section.find_element(By.CLASS_NAME, 'plain.scroll-to-anchor').click()
    time.sleep(1)

  def get_element_aside_supporting_charities(self):
    return self.get_section_by_aria_label('aside', 'Supporting charities. Strengthening communities.')
  
  def get_text_supporting_charities_header(self):
    supporting_section = self.get_element_aside_supporting_charities()
    return self.get_text_section_header(supporting_section)
  
  def get_text_supporting_charities_body(self):
    supporting_section = self.get_element_aside_supporting_charities()
    return self.get_text_section_body(supporting_section)
  
  def click_element_supporting_charities_button_1(self):
    html = self.get_html()
    supporting_section = self.get_element_aside_supporting_charities()
    supporting_section.find_element(By.XPATH, './/div/div/div[2]/a[1]').click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))

  def click_element_supporting_charities_button_2(self):
    html = self.get_html()
    supporting_section = self.get_element_aside_supporting_charities()
    supporting_section.find_element(By.XPATH, './/div/div/div[2]/a[2]').click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
 