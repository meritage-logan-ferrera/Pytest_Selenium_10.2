from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_base import BasePage  

class FloorplanPage(BasePage):
  def get_element_image_carousel(self):
    return self.driver.find_element(By.XPATH, ".//div[contains(@class,'carousel-hero')]")
  
  def click_element_next_arrow(self):
    carousel_section = self.get_element_image_carousel()
    carousel_section.find_element(By.CLASS_NAME, 'orbit-next.slick-arrow').click()
  
  def get_elements_carousel_slides(self):
    carousel_section = self.get_element_image_carousel()
    slides = carousel_section.find_elements(By.XPATH, ".//li[contains(@class, 'slick-slide') and not(contains(@class, 'slick-cloned'))]")
    return slides
  
  def get_element_current_slide(self):
    carousel_section = self.get_element_image_carousel()
    return carousel_section.find_element(By.XPATH, ".//li[contains(@class, 'is-active')]")
  
  def get_element_slide_number(self, number):
    carousel_section = self.get_element_image_carousel()
    slides = self.get_elements_carousel_slides()
    return slides[number]
  
  def get_element_article(self):
    return self.driver.find_element(By.CLASS_NAME, 'small-12.medium-10.large-8.column.text-center')
  
  def get_text_plan_sub_header(self):
    article = self.get_element_article()
    return article.find_element(By.TAG_NAME, 'p').text
  
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
  
  def get_element_section_floorplan(self):
    return self.driver.find_element(By.CLASS_NAME, 'explore-floorplan')
  
  def click_element_virtual_walkthrough_button(self):
    floorplan_section = self.get_element_section_floorplan()
    floorplan_section.find_element(By.ID, 'floorplan-tab-virtual-walkthrough-label').click()
  
  def get_element_floorplan_image(self):
    floorplan_section = self.get_element_section_floorplan()
    return floorplan_section.find_element(By.XPATH, './/div[3]/div/div/div[1]/img')
    # use naturalWidth

  def get_element_virtual_walkthrough_iframe(self):
    floorplan_section = self.get_element_section_floorplan()
    return floorplan_section.find_element(By.XPATH, './/div[3]/div/div/div[2]/div/iframe')
  
  def click_element_download_pdf(self):
    original_window = self.driver.current_window_handler
    floorplan_section = self.get_element_section_floorplan()
    floorplan_section.find_element(By.CLASS_NAME, 'floorplan-pdf').click()
    self.new_tab(original_window)
  
  def click_element_compare_floorplan_button(self):
    html = self.get_html()
    floorplan_section = self.get_element_section_floorplan()
    floorplan_section.find_element(By.XPATH, './/div[4]/div/a[1]')
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def click_element_save_favorites_button(self):
    html = self.get_html()
    floorplan_section = self.get_element_section_floorplan()
    floorplan_section.find_element(By.XPATH, './/div[4]/div/a[2]')
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))

  def get_element_aside_promotion(self):
    return self.get_section_by_aria_label('aside', 'promotion banner')
  
  def get_element_promotion_image(self):
    promotion_section = self.get_element_aside_promotion()
    return self.get_element_section_placeholder_image(promotion_section)
  
  def get_element_promotion_button(self):
    promotion_section = self.get_element_aside_promotion()
    return promotion_section.find_element(By.CLASS_NAME, 'button.button--blue--solid')
  
  def get_element_article_home_features(self):
    return self.get_section_by_aria_label('article', 'Home Features')
  
  def get_element_home_features_image(self):
    features_section = self.get_element_article_home_features()
    return self.get_element_section_placeholder_image(features_section)

  def get_element_section_tabs(self):
    return self.driver.find_element(By.CLASS_NAME, 'tabbed-accordion    ')
  
  def get_text_tabs_header(self):
    tabs_section = self.get_element_section_tabs()
    return tabs_section.find_element(By.TAG_NAME, 'h2').text
  
  def get_text_tabs_body(self):
    tabs_section = self.get_element_section_tabs()
    return tabs_section.find_element(By.TAG_NAME, 'p').text
  
  def get_elements_tabs(self):
    tabs_section = self.get_element_section_tabs()
    tabs_container = tabs_section.find_element(By.ID, 'tab-container-floorplans')
    return tabs_container.find_elements(By.TAG_NAME, 'li')
  
  def get_element_tab_image(self, number):
    tabs = self.get_elements_tabs()
    return tabs[number].find_element(By.TAG_NAME, 'img')
    # test with naturalWidth not width since width includes width if alt text is displayed
  
  def get_text_tab_name(self, number):
    tabs = self.get_elements_tabs()
    return tabs[number].find_element(By.TAG_NAME, 'span').text
  
  def click_element_tab(self, number):
    tabs = self.get_elements_tabs()
    tabs[number].click()
  
  def get_element_active_info_tab(self, number):
    tabs_section = self.get_element_section_tabs()
    info_tab_container = tabs_section.find_element(By.CLASS_NAME, 'responsive-tabs.tabs-content')
    return info_tab_container.find_element(By.XPATH, f".//li[{number}]")
  
  def get_element_info_tab_elevations(self):
    return self.get_element_active_info_tab(1)
  
  def get_elements_elevations_containers(self):
    elevations_info_tab = self.get_element_info_tab_elevations()
    return elevations_info_tab.find_elements(By.CLASS_NAME, 'small-12.medium-6.large-4.columns.elevation')
  
  def get_element_container_image(self, number):
    tabs = self.get_elements_elevations_containers()
    return tabs[number].find_element(By.TAG_NAME, 'img')
  
  def get_text_container_elevation(self, number):
    tabs = self.get_elements_elevations_containers()
    return tabs[number].find_element(By.XPATH, ".//span[@class='title']").text
  
  def get_element_container_button(self, number):
    tabs = self.get_elements_elevations_containers()
    return tabs[number].find_element(By.XPATH, ".//a[@class='contact']")
  
  def get_element_info_tab_directions(self):
    return self.get_element_active_info_tab(2)

  def get_text_directions_community_adr_header(self):
    directions_info_tab = self.get_element_info_tab_directions()
    return directions_info_tab.find_element(By.XPATH, './/div/div/div/div[2]/div/div[1]/strong').text
  
  def get_text_directions_community_adr(self):
    directions_info_tab = self.get_element_info_tab_directions()
    return directions_info_tab.find_element(By.XPATH, ".//p[@v-if='community']").text
  
  def get_element_directions_button(self):
    directions_info_tab = self.get_element_info_tab_directions()
    return directions_info_tab.find_element(By.XPATH, './/div/div/div/div[2]/div/div[1]/a')
  
  def get_text_below_directions(self):
    directions_info_tab = self.get_element_info_tab_directions()
    return directions_info_tab.find_element(By.XPATH, './/div/div/div/div[2]/div/div[1]/p[2]').text
  
  def get_text_sales_counselors(self):
    directions_info_tab = self.get_element_info_tab_directions()
    return directions_info_tab.find_element(By.XPATH, './/div/section/div/div/div[2]/div/div[2]/strong')
  
  def get_element_info_tab_homesite(self):
    return self.get_element_active_info_tab(3)
  
  def check_clickable_homesite_button(self):
    homesite_info_tab = self.get_element_info_tab_homesite()
    button = homesite_info_tab.find_element(By.XPATH, './/div/section/a')
    return self.button_is_clickable(button)
  
  def get_element_iframe(self):
    homesite_info_tab = self.get_element_info_tab_homesite()
    return homesite_info_tab.find_element(By.XPATH, './/div/section/iframe')
  
  def get_element_map_image(self):
    homesite_info_tab = self.get_element_info_tab_homesite()
    return homesite_info_tab.find_element(By.XPATH, '/div/section/figure/img')

  def get_aside_stay_up_to_date(self):
    return self.get_section_by_aria_label('aside', 'Interest list sign up form')
  
  def click_element_homebuyer_button(self):
    stay_section = self.get_aside_stay_up_to_date()
    stay_section.find_element(By.XPATH, './/div[1]/div/form/div[1]/div/div[1]/label').click()
  
  def click_element_agent_button(self):
    stay_section = self.get_aside_stay_up_to_date()
    stay_section.find_element(By.XPATH, './/div[1]/div/form/div[1]/div/div[2]/label').click()
  
  def check_aside_button_clickable(self):
    stay_section = self.get_aside_stay_up_to_date()
    button = stay_section.find_element(By.XPATH, './/div[1]/div/form/div[3]/div[4]/button')
    return self.button_is_clickable(button)
  
