from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_base import BasePage  

class MetroPage(BasePage):
  def get_element_top_bar(self):
    return self.driver.find_element(By.CLASS_NAME, 'row.full-width.diff.collapse')
  
  def get_element_city_dropdown(self):
    top_bar = self.get_element_top_bar()
    return top_bar.find_element(By.ID, 'region-select')
  
  def get_element_bedrooms_dropdown(self):
    top_bar = self.get_element_top_bar()
    return top_bar.find_element(By.ID, 'bedroomDropDown')
  
  def get_element_bathrooms_dropdown(self):
    top_bar = self.get_element_top_bar()
    return top_bar.find_element(By.ID, 'bathroomDropDown')
  
  def get_element_slider_1(self):
    top_bar = self.get_element_top_bar()
    return top_bar.find_element(By.XPATH, './/div/div/div/div/div[4]/div/span/span[1]')
  
  def get_element_slider_1_left_circle(self):
    slider_1 = self.get_element_slider_1()
    return slider_1.find_element(By.CLASS_NAME, 'irs-slider.from')
  
  def get_text_slider_1_left_tag(self):
    slider_1 = self.get_element_slider_1()
    return slider_1.find_element(By.CLASS_NAME, 'irs-from').text
  
  def get_element_slider_1_right_circle(self):
    slider_1 = self.get_element_slider_1()
    return slider_1.find_element(By.CLASS_NAME, 'irs-slider.to')
  
  def get_text_slider_1_right_tag(self):
    slider_1 = self.get_element_slider_1()
    return slider_1.find_element(By.CLASS_NAME, 'irs-to').text
  
  def get_element_slider_2(self):
    top_bar = self.get_element_top_bar()
    return top_bar.find_element(By.XPATH, './/div/div/div/div/div[5]/div/span/span[1]')
  
  def get_element_slider_2_left_circle(self):
    slider_2 = self.get_element_slider_2()
    return slider_2.find_element(By.CLASS_NAME, 'irs-slider.from')
  
  def get_text_slider_2_left_tag(self):
    slider_2 = self.get_element_slider_2()
    return slider_2.find_element(By.CLASS_NAME, 'irs-from').text
  
  def get_element_slider_2_right_circle(self):
    slider_2 = self.get_element_slider_2()
    return slider_2.find_element(By.CLASS_NAME, 'irs-slider.to')

  def get_text_slider_2_right_tag(self):
    slider_2 = self.get_element_slider_2()
    return slider_2.find_element(By.CLASS_NAME, 'irs-to').text
  
  def slide_to_slide(self, slider):
    action = ActionChains(self.driver)
    slider_1_left = self.get_element_slider_1_left_circle()
    slider_1_right = self.get_element_slider_1_right_circle()
    slider_2_left = self.get_element_slider_2_left_circle()
    slider_2_right = self.get_element_slider_2_right_circle()
    if slider == 'bed':
      action.move_to_element(slider_1_left).pause(.5).click_and_hold(slider_1_left).pause(.5).move_by_offset(50, 0).release().perform()
      action.move_to_element(slider_1_right).pause(.5).click_and_hold(slider_1_right).pause(.5).move_by_offset(-50, 0).release().perform()
    elif slider == 'bath':
      action.move_to_element(slider_2_left).pause(.5).click_and_hold(slider_2_left).pause(.5).move_by_offset(50, 0).release().perform()
      action.move_to_element(slider_2_right).pause(.5).click_and_hold(slider_2_right).pause(.5).move_by_offset(-50, 0).release().perform()
    

  def get_element_top_bar_submit_button(self):
    top_bar = self.get_element_top_bar()
    return top_bar.find_element(By.CLASS_NAME, 'button.button--blue--solid.see-results-top')
  
  def get_element_top_bar_reset(self):
    top_bar = self.get_element_top_bar()
    return top_bar.find_element(By.ID, 'resetFilters')
  
  def get_element_map_keyboard_shortcuts_button(self):
    return self.driver(By.XPATH, '/html/body/div[3]/div/div/div[1]/div[1]/div/div[1]/div[1]/div/div/div[16]/div/div[1]/div/div[2]/button')
  
  def get_element_map(self):
    return self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/div[1]/div/div[1]/div[1]/div/div/div[2]')
  
  def get_element_section_right_side(self):
    return self.driver.find_element(By.CLASS_NAME, 'community-right-side')
  
  def get_text_title(self):
    right_side = self.get_element_section_right_side()
    return right_side.find_element(By.CLASS_NAME, 'page-title').text
  
  def get_text_communities_and_qmi(self):
    right_side = self.get_element_section_right_side()
    return right_side.find_element(By.CLASS_NAME, 'page-title-link').text
  
  def get_elements_communities(self):
    right_side = self.get_element_section_right_side()
    return right_side.find_elements(By.CLASS_NAME, 'community-horizontal  ')
  
  def get_element_community_image(self, number):
    communities = self.get_elements_communities()
    return communities[number].find_element(By.TAG_NAME, 'img')
  
  def get_text_community_snipe_overlay(self, number):
    communities = self.get_elements_communities()
    return communities[number].find_element(By.TAG_NAME, 'span').text
    # assert != ''
  
