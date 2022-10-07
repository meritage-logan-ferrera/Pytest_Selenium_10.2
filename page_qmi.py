from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_base import BasePage   

class QMIPage(BasePage):
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
  
  #clicking does nothing on PROD
  def click_element_qmi_see_whats_included_button(self):
    carousel_section = self.get_element_image_carousel()
    return carousel_section.find_element(By.XPATH, ".//a[@href='#includedDesignFeatures']")
  
  def click_element_book_a_tour_button(self):
    carousel_section = self.get_element_image_carousel()
    button =carousel_section.find_element(By.ID, 'BookATourNavCallout2')
    self.driver.execute_script('arguments[0].scrollIntoView(true); window.scrollBy(0, -500)', button)
    button.click()

  def get_element_section_main(self):
    return self.get_section_by_aria_label('article', 'overview B article')

  def get_text_plan_number(self):
    main_section = self.get_element_section_main()
    return main_section.find_element(By.TAG_NAME, 'p').text
  
  def get_text_qmi_name_header(self):
    main_section = self.get_element_section_main()
    return main_section.find_element(By.TAG_NAME, 'h1').text
  
  def get_text_community(self):
    main_section = self.get_element_section_main()
    return main_section.find_element(By.TAG_NAME, 'a').text
  
  def click_element_community_button(self):
    html = self.get_html()
    main_section = self.get_element_section_main()
    main_section.find_element(By.TAG_NAME, 'a').click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def new_page_get_community_name(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/div[1]/div[1]/div/article/h1').text
  
  def get_text_qmi_description(self):
    main_section = self.get_element_section_main()
    return main_section.find_element(By.XPATH, 'p[2]').text
  
  def get_text_qmi_estimated_completion(self):
    main_section = self.get_element_section_main()
    return main_section.find_element(By.XPATH, 'p[3]').text
  
  def get_text_qmi_home_address(self):
    main_section = self.get_element_section_main()
    return main_section.find_element(By.XPATH, 'p[2]').text
  
  def get_element_section_aside(self):
    return self.get_section_by_aria_label('aside', 'overview B aside')
  
  def get_text_aside(self):
    aside = self.get_element_section_aside()
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
    original_window = self.driver.current_window_handle
    floorplan_section = self.get_element_section_floorplan()
    floorplan_section.find_element(By.CLASS_NAME, 'floorplan-pdf').click()
    self.new_tab(original_window)
  
  def get_element_compare_qmi_button(self):
    floorplan_section = self.get_element_section_floorplan()
    return floorplan_section.find_element(By.XPATH, './/div[4]/div/a[1]')
  
  def get_element_save_favorites_button(self):
    floorplan_section = self.get_element_section_floorplan()
    return floorplan_section.find_element(By.XPATH, './/div[4]/div/a[2]')
  
  def click_element_interior_package_button(self):
    floorplan_section = self.get_element_section_floorplan()
    floorplan_section.find_element(By.ID, 'floorplan-tab-design-label').click()
  
  def get_element_interior_package_image(self):
    floorplan_section = self.get_element_section_floorplan()
    return floorplan_section.find_element(By.XPATH, './/div[3]/div/div/div[3]/ul/div/div/li/img')
  
  def click_element_elevation_button(self):
    floorplan_section = self.get_element_section_floorplan()
    floorplan_section.find_element(By.ID, 'Elevation-label').click()
  
  def get_element_elevation_image(self):
    floorplan_section = self.get_element_section_floorplan()
    return floorplan_section.find_element(By.XPATH, './/div[3]/div/div/div[4]/img')
  
  def get_element_aside_promotion(self):
    return self.get_section_by_aria_label('aside', 'promotion banner')
  
  def get_element_promotion_image(self):
    promotion_section = self.get_element_aside_promotion()
    return self.get_element_section_placeholder_image(promotion_section)
  
  def get_element_promotion_button(self):
    promotion_section = self.get_element_aside_promotion()
    return promotion_section.find_element(By.CLASS_NAME, 'button.button--blue--solid')
  
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