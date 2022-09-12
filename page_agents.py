from venv import create
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_base import BasePage
import time  

class AgentsPage(BasePage):
  def click_element_play_button(self):
    return self.driver.find_element(By.XPATH, "//*[@id='quick-home-search-hero']/div[1]/div/div/div/a")
  
  def get_text_main_header(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/header/div/div/h1').text
  
  def get_text_main_sub_header(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/header/div/div/p').text
  
  def click_elemenet_main_button_1(self):
    self.driver.find_element(By.XPATH, '/html/body/main/header/div/div/a[1]')
  
  def click_elemenet_main_button_2(self):
    self.driver.find_element(By.XPATH, '/html/body/main/header/div/div/a[2]')
  
  def get_element_aside_1_when_you_sell_with_us(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/aside[1]')
  
  def get_text_aside_1_header(self):
    aside_1 = self.get_element_aside_1_when_you_sell_with_us()
    return self.get_text_section_header(aside_1)
  
  def get_text_aside_1_body(self):
    aside_1 = self.get_element_aside_1_when_you_sell_with_us()
    return self.get_text_section_body(aside_1)
  
  def get_element_aside_1_image(self):
    aside_1 = self.get_element_aside_1_when_you_sell_with_us()
    return self.get_element_section_placeholder_image(aside_1)
  
  def get_element_article_1(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/article[1]')
  
  def get_element_article_1_container(self, number):
    article_1 = self.get_element_article_1()
    return article_1.find_element(By.XPATH, f'/html/body/main/article[1]/div/div/div[2]/div[{number}]')
  
  def get_text_article_1_container_header(self, number):
    container = self.get_element_article_1_container(number)
    return container.find_element(By.TAG_NAME, 'h3').text
  
  def get_text_article_1_container_body(self, number):
    container = self.get_element_article_1_container(number)
    return self.get_text_section_body(container)
  
  def get_element_article_1_container_image(self, number):
    container = self.get_element_article_1_container(number)
    return self.get_element_section_placeholder_image(container)
  
  def get_element_article_2_meritage_agent_terms(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/article[2]')
  
  def get_text_article_2_call_header(self):
    article_2 = self.get_element_article_2_meritage_agent_terms()
    return article_2.find_element(By.TAG_NAME, 'h3').text
  
  def get_text_article_2_header(self):
    article_2 = self.get_element_article_2_meritage_agent_terms()
    return article_2.find_element(By.XPATH, '/html/body/main/article[2]/header/div/p[3]/strong').text
  
  def get_elements_article_2_body_numbered_list(self):
    article_2 = self.get_element_article_2_meritage_agent_terms()
    return article_2.find_elements(By.XPATH, '/html/body/main/article[2]/header/div/ol/li')
  
  def get_text_article_2_body_numbered_list(self):
    list_elements = self.get_elements_article_2_body_numbered_list()
    span_elements = []
    for i in range(len(list_elements)):
      span_element = list_elements[i].find_element(By.TAG_NAME, 'span').text
      span_elements.append(span_element)
    return span_elements

  def get_elements_article_2_body_one_sublist(self):
    article_2 = self.get_element_article_2_meritage_agent_terms()
    return article_2.find_elements(By.XPATH, '/html/body/main/article[2]/header/div/ol/li[1]/ol/li')
  
  def get_text_article_2_body_one_sublist(self):
    sublist = self.get_elements_article_2_body_one_sublist()
    sublist_text = []
    for i in range(len(sublist)):
      sublist_text.append(sublist[i].text)
    return sublist_text
  
  def get_text_article_2_bottom(self):
    article_2 = self.get_element_article_2_meritage_agent_terms()
    return article_2.find_element(By.XPATH, '/html/body/main/article[2]/header/div/p[4]/span[2]').text
  
  def get_text_article_2_disclaimer(self):
    article_2 = self.get_element_article_2_meritage_agent_terms()
    disclaimer = article_2.find_elements(By.XPATH, '/html/body/main/article[2]/header/div/ul/li')
    disclaimer_text = []
    for i in range(len(disclaimer)):
      disclaimer_text.append(disclaimer[i].text)
    return disclaimer_text
  
  def get_element_section_user_input_account(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/section')
  
  def click_element_create_account_button(self):
    section_input = self.get_element_section_user_input_account()
    section_input.find_element(By.ID, 'register-tab').click()
  
  def click_element_sign_in_button(self):
    section_input = self.get_element_section_user_input_account()
    section_input.find_element(By.ID, 'sign-in-tab').click()
  
  def get_element_sign_in_form(self):
    section_input = self.get_element_section_user_input_account()
    return section_input.find_element(By.ID, 'sign-in-form')
  
  def get_element_create_account_form(self):
    section_input = self.get_element_section_user_input_account()
    return section_input.find_element(By.ID, 'register-form')
  
  def get_text_sign_in_form_body(self):
    sign_in = self.get_element_sign_in_form()
    return sign_in.find_element(By.XPATH, './/p[1]').text
  
  def check_element_clickable_sign_in_button(self):
    sign_in = self.get_element_sign_in_form()
    button = sign_in.find_element(By.ID, 'sign-in-button')
    return self.button_is_clickable(button)
  
  def click_element_sign_in_get_help_button(self):
    sign_in = self.get_element_sign_in_form()
    sign_in.find_element(By.CLASS_NAME, 'plain.show-password-reset').click()
  
  def get_element_forgot_password_tab(self):
    return self.driver.find_element(By.ID, 'forgot-password')
  
  def get_text_create_account_form_body(self):
    create_account = self.get_element_create_account_form()
    return create_account.find_element(By.XPATH, './/p[1]').text
  
  def get_element_create_account_metro_dropdown(self):
    create_account = self.get_element_create_account_form()
    return create_account.find_element(By.ID, 'agent-metro-area-select')
  
  def get_text_create_account_form_company_info(self):
    create_account = self.get_element_create_account_form()
    return create_account.find_element(By.XPATH, './/h5[1]').text
  
  def get_element_create_account_state_dropdown(self):
    create_account = self.get_element_create_account_form()
    return create_account.find_element(By.ID, 'FormModel_State')
  
  def get_text_create_account_form_client(self):
    create_account = self.get_element_create_account_form()
    return create_account.find_element(By.XPATH, './/h5[2]').text
  
  def click_element_create_account_optional_register_client(self):
    create_account = self.get_element_create_account_form()
    create_account.find_element(By.XPATH, ".//span[@class='colored-checkbox inline no-margin-bottom']").click()
  
  def get_element_create_account_optional_form(self):
    create_account = self.get_element_create_account_form()
    return create_account.find_element(By.CLASS_NAME, 'small-12.columns.checkbox.pad-bottom-1.flex.align-middle')
  
  def get_input_client_first_name(self):
    client_first_name = self.driver.find_element(By.ID, 'FormModel_ClientFirstName')
    return self.get_input_into_form(client_first_name)
  
  def get_input_client_last_name(self):
    client_last_name = self.driver.find_element(By.ID, 'FormModel_ClientLastName')
    return self.get_input_into_form(client_last_name)
  
  def get_input_client_email_address(self):
    client_email_address = self.driver.find_element(By.ID, 'FormModel_ClientEmailAddress')
    return self.get_input_into_form(client_email_address)
  
  def get_element_create_account_client_metro_area(self):
    create_account = self.get_element_create_account_form()
    return create_account.find_element(By.ID, 'metro-area-select')
  
  def get_element_create_account_client_community(self):
    create_account = self.get_element_create_account_form()
    return create_account.find_element(By.ID, 'community-select')
  
  def get_element_create_account_optional_ack_button(self):
    create_account = self.get_element_create_account_form()
    return create_account.find_element(By.XPATH, "(.//span[@class='colored-checkbox inline no-margin-bottom'])[2]")
  
  def get_text_create_account_header(self):
    create_account = self.get_element_create_account_meritage_agent_terms()
    return create_account.find_element(By.XPATH, './/div/div/div/form/div[1]/div[28]/div/p').text

  def get_elements_create_account_body_numbered_list(self):
    create_account = self.get_element_create_account_form()
    return create_account.find_elements(By.XPATH, './/div/div/div/form/div[1]/div[28]/div/ol/li')

  def get_text_create_account_body_numbered_list(self):
    list_elements = self.get_elements_create_account_body_numbered_list()
    span_elements = []
    for i in range(len(list_elements)):
      if i == 0:
        span_element = list_elements[i].find_element(By.XPATH, './/span[2]').text
      else:
        span_element = list_elements[i].find_element(By.TAG_NAME, 'span').text
      span_elements.append(span_element)
    return span_elements

  def get_elements_create_account_body_one_sublist(self):
    create_account = self.get_element_create_account_form()
    return create_account.find_elements(By.XPATH, './/div/div/div/form/div[1]/div[28]/div/ol/li[1]/ol/li')

  def get_text_create_account_body_one_sublist(self):
    sublist = self.get_elements_create_account_body_one_sublist()
    sublist_text = []
    for i in range(len(sublist)):
      sublist_text.append(sublist[i].text)
    return sublist_text
  
  def get_text_create_account_bottom(self):
    create_account = self.get_element_create_account_form()
    return create_account.find_element(By.XPATH, './/div/div/div/form/div[1]/div[28]/div/div/div/p/span').text
  
  def get_element_create_account_terms_and_conditions_button(self):
    create_account = self.get_element_create_account_form()
    return create_account.find_element(By.XPATH, "(.//span[@class='colored-checkbox inline no-margin-bottom'])[3]")
  
  def get_element_create_account_complete_registration_button(self):
    create_account = self.get_element_create_account_form()
    return create_account.find_element(By.XPATH, ".//div/div/div/form/fieldset/div[3]/div[2]/button")
  