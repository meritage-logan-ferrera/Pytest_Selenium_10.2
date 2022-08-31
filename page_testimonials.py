from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_base import BasePage
import time  

class TestimonialsPage(BasePage):
  def get_text_main_header(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/header/div[1]/div/div/div/h1").text
  
  def get_text_main_sub_header(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/header/div[1]/div/div/div/p").text
  
  def click_element_play_button(self):
    self.driver.find_element(By.XPATH, "/html/body/main/header/div[1]/div/div/div/a").click()

  # One overlay is used for every video. How to distinguish?
  def get_element_youtube_overlay(self):
    return self.driver.find_element(By.XPATH, "/html/body/div[4]")
    #display block

  def get_text_section_header(self, section):
    header = section.find_element(By.TAG_NAME, 'h2')
    return header.text
  
  def get_text_section_body(self, section):
    body = section.find_element(By.TAG_NAME, 'p')
    return body.text
  
  def click_element_section_button(self, section):
    section.find_element(By.TAG_NAME, 'a').click()

  def get_element_section_placeholder_image(self, section):
    return section.find_element(By.TAG_NAME, "img")
    
  def click_element_section_play_button(self, section):
    section.find_element(By.CLASS_NAME, "video-trigger").click()

  def get_element_aside_1(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/aside[1]")

  def get_text_aside_1_header(self):
    aside_1 = self.get_element_aside_1()
    return self.get_text_section_header(aside_1)
  
  def get_text_aside_1_body(self):
    aside_1 = self.get_element_aside_1()
    return self.get_text_section_body(aside_1)
  
  def click_element_aside_1_button(self):
    aside_1 = self.get_element_aside_1()
    self.click_element_section_button(aside_1)
  
  def get_element_section_1_row(self, number):
    return self.driver.find_element(By.XPATH, f"/html/body/main/article[1]/div/div/div[{number}]")

  def get_text_row_header(self, number):
    row = self.get_element_section_1_row(number)
    return self.get_text_section_header(row)
  
  def get_text_row_body(self, number):
    row = self.get_element_section_1_row(number)
    return self.get_text_section_body(row)
  
  def click_element_row_button(self, number):
    row = self.get_element_section_1_row(number)
    self.click_element_section_button(row)
  
  def get_element_row_image(self, number):
    row = self.get_element_section_1_row(number)
    return self.get_element_section_placeholder_image(row)
  
  def click_element_row_play_button(self, number):
    row = self.get_element_section_1_row(number)
    return self.click_element_section_play_button(row)
  
  def get_element_aside_2(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/aside[2]")
  
  def get_text_avid_header(self):
    aside = self.get_element_aside_2()
    return self.get_text_section_header(aside)
  
  def get_text_avid_body(self):
    aside = self.get_element_aside_2()
    return self.get_text_section_body(aside)
  
  def get_element_avid_image(self):
    aside = self.get_element_aside_2()
    return self.get_element_section_placeholder_image(aside)
  
  #opens new tab to avid site
  def click_element_avid_button(self):
    original_window = self.driver.current_window_handle
    aside = self.get_element_aside_2()
    aside.find_element(By.TAG_NAME, 'a').click()
    WebDriverWait(self.driver, timeout=3).until(EC.number_of_windows_to_be(2))
    for window_handle in self.driver.window_handles:
      if window_handle != original_window:
        self.driver.switch_to.window(window_handle)
        break
      if self.driver.title == '':
        time.sleep(1)

  def get_element_section_local_lowdown(self):
    return self.driver.find_element(By.ID, 'testimonial-dropdown-display')

  def get_text_section_local_header(self):
    section = self.get_element_section_local_lowdown()
    return self.get_text_section_header(section)
  
  def get_text_section_local_body(self):
    section = self.get_element_section_local_lowdown()
    return self.get_text_section_body(section)
  
  def click_element_section_local_dropdown(self):
    section = self.get_element_section_local_lowdown()
    dropdown = section.find_element(By.XPATH, "/html/body/main/article[2]/div/div/div[2]/div/label/select")
    dropdown.click()
  
  def click_element_section_local_dropdown_select_a_metro(self):
    section = self.get_element_section_local_lowdown()
    select_a_metro_option = section.find_element(By.XPATH, '/html/body/main/article[2]/div/div/div[2]/div/label/select/option')
    self.click_element_section_local_dropdown()
    select_a_metro_option.click()
    
  def get_elements_section_local_under_dropdown(self):
    section = self.get_element_section_local_lowdown()
    parent_div = section.find_element(By.XPATH, '/html/body/main/article[2]/div/div/div[3]')
    homeowner_quotes = parent_div.find_elements(By.TAG_NAME, 'div')
    return homeowner_quotes

  def get_element_section_testimonial_submission(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/section/div/div/div/div/div[3]/div/form')

  def get_text_testimonial_submission_header(self):
    submission_form = self.get_element_section_testimonial_submission()
    return self.get_text_section_header(submission_form)
  
  def get_text_testimonial_submission_body(self):
    submission_form = self.get_element_section_testimonial_submission()
    body_text = submission_form.find_element(By.XPATH, '/html/body/main/section/div/div/div/div/div[3]/div/form/div[1]')
    return body_text.text
  
  def get_input_into_form(self, form):
    form.send_keys('test_input')
    return form.get_attribute('value')

  def get_input_first_name(self):
    first_name = self.driver.find_element(By.ID, 'FormModel_FirstName')
    return self.get_input_into_form(first_name)

  def get_input_last_name(self):
    last_name = self.driver.find_element(By.ID, 'FormModel_LastName')
    return self.get_input_into_form(last_name)

  def get_input_email_address(self):
    email_address = self.driver.find_element(By.ID, 'FormModel_EmailAddress')
    return self.get_input_into_form(email_address)

  def get_input_phone_number(self):
    phone_number = self.driver.find_element(By.ID, 'FormModel_PhoneNumber')
    return self.get_input_into_form(phone_number)
  
  def get_input_your_story(self):
    your_story = self.driver.find_element(By.ID, 'FormModel_YourStory')
    return self.get_input_into_form(your_story)
  
  def get_element_agree_to_terms(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/section/div/div/div/div/div[3]/div/form/div[2]/div[11]/span/label')
    
  def click_element_agree_to_terms(self):
    agree_box = self.get_element_agree_to_terms()
    agree_box.click()

  def check_element_testimonial_submission_button_is_clickable(self):
    element = self.driver.find_element(By.XPATH, '/html/body/main/section/div/div/div/div/div[3]/div/form/div[2]/div[15]/button')
    bool = False
    bool = WebDriverWait(self.driver, timeout=3).until(EC.element_to_be_clickable(element))
    return bool

  def get_element_aside_3(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/aside[3]')
  
  def get_text_aside_3_header(self):
    aside_3 = self.get_element_aside_3()
    return self.get_text_section_header(aside_3)
  
  def get_text_aside_3_body(self):
    aside_3 = self.get_element_aside_3()
    return self.get_text_section_body(aside_3)
  
  def click_element_aside_3_button(self):
    aside_3 = self.get_element_aside_3()
    self.click_element_section_button(aside_3)