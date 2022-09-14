from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_base import BasePage
import time  

class ContactUsPage(BasePage):
  def get_text_main_header(self):
    return self.driver.find_element(By.XPATH, '/html/body/header/div/div/h1').text

  def get_text_main_sub_header(self):
    return self.driver.find_element(By.XPATH, '/html/body/header/div/div/p').text
  
  def get_element_section_how_can_we_help(self):
    return self.driver.find_element(By.CLASS_NAME, 'tabbed-accordion.background--gray.no-pad-bottom.no-pad-bottom')
  
  def get_text_how_help_header(self):
    how_help = self.get_element_section_how_can_we_help()
    return self.get_text_section_header(how_help)
  
  def get_text_how_help_body(self):
    how_help = self.get_element_section_how_can_we_help()
    return self.get_text_section_body(how_help)
  
  def click_element_how_element_new_buyers_button(self):
    how_help = self.get_element_section_how_can_we_help()
    how_help.find_element(By.ID, 'tab-1-title-label').click()
   
  def click_element_how_element_warranty_claims_button(self):
    how_help = self.get_element_section_how_can_we_help()
    how_help.find_element(By.ID, 'tab-2-title-label').click()
   
  def click_element_how_element_agent_button(self):
    how_help = self.get_element_section_how_can_we_help()
    how_help.find_element(By.ID, 'tab-3-title-label').click()
  
  def get_element_new_buyers_tab(self):
    how_help = self.get_element_section_how_can_we_help()
    return how_help.find_element(By.ID, 'tab-1-title')
  
  def get_element_warranty_claims_tab(self):
    how_help = self.get_element_section_how_can_we_help()
    return how_help.find_element(By.ID, 'tab-2-title')
  
  def get_element_agent_tab(self):
    how_help = self.get_element_section_how_can_we_help()
    return how_help.find_element(By.ID, 'tab-3-title')

  def get_text_new_buyers_tab_header(self):
    new_buyers = self.get_element_new_buyers_tab()
    return new_buyers.find_element(By.XPATH, './/div/section/div/div/div/div/div[3]/div/form/div[1]/div[1]/p/span').text
  
  def get_element_new_buyers_metro_dropdown(self):
    new_buyers = self.get_element_new_buyers_tab()
    return new_buyers.find_element(By.ID, 'contact-metro-area-select')
  
  def get_element_new_buyers_community_dropdown(self):
    new_buyers = self.get_element_new_buyers_tab()
    return new_buyers.find_element(By.ID, 'contact-community-select')

  def get_text_new_buyers_tab_location(self):
    new_buyers = self.get_element_new_buyers_tab()
    return new_buyers.find_element(By.XPATH, './/h5[1]').text
  
  def click_element_new_buyers_metro_dropdown(self):
    metro_dropdown = self.get_element_new_buyers_metro_dropdown()
    metro_dropdown.click()
    metro_area = metro_dropdown.find_element(By.XPATH, './/option[2]')
    metro_area.click()

  def get_text_new_buyers_tab_your_question(self):
    new_buyers = self.get_element_new_buyers_tab()
    return new_buyers.find_element(By.XPATH, './/div/section/div/div/div/div/div[3]/div/form/div[1]/div[11]/h5').text
  
  def get_text_new_buyers_tab_SMS_disclaimer(self):
    new_buyers = self.get_element_new_buyers_tab()
    return new_buyers.find_element(By.XPATH, ".//div[@class='SMSOptInDisclaimer']/p").text
  
  def get_element_new_buyers_tab_submit_button(self):
    new_buyers = self.get_element_new_buyers_tab()
    return new_buyers.find_element(By.CLASS_NAME, 'button.button--blue--solid.button--large-top')
  
  def get_text_warranty_claims_tab_header(self):
    warranty_claims = self.get_element_warranty_claims_tab()
    return self.get_text_section_header(warranty_claims)
  
  def get_text_warranty_claims_tab_body(self):
    warranty_claims = self.get_element_warranty_claims_tab()
    return self.get_text_section_body(warranty_claims)
  
  def click_element_warranty_claims_tab_button(self):
    original_window = self.driver.current_window_handle
    warranty_claims = self.get_element_warranty_claims_tab()
    warranty_claims.find_element(By.CLASS_NAME, 'button.button--blue--solid.button--large-top').click()
    self.new_tab(original_window)
  
  def get_text_warranty_claims_tab_number(self):
    warranty_claims = self.get_element_warranty_claims_tab()
    return warranty_claims.find_element(By.XPATH, './/div/article/header/div/span').text

  def get_text_agent_tab_header(self):
    agent_tab = self.get_element_agent_tab()
    return agent_tab.find_element(By.XPATH, './/div/section/div/div/div/div/div[3]/div/form/div[1]/div[1]/p/span').text
  
  def get_element_agent_tab_metro_dropdown(self):
    agent_tab = self.get_element_agent_tab()
    return agent_tab.find_element(By.ID, 'contact-metro-area-select')
  
  def get_element_agent_tab_community_dropdown(self):
    agent_tab = self.get_element_agent_tab()
    return agent_tab.find_element(By.ID, 'contact-community-select')

  def get_text_agent_tab_location(self):
    agent_tab = self.get_element_agent_tab()
    return agent_tab.find_element(By.XPATH, './/h5[1]').text

  def click_element_agent_tab_metro_dropdown(self):
    metro_dropdown = self.get_element_agent_tab_metro_dropdown()
    metro_dropdown.click()
    metro_area = metro_dropdown.find_element(By.XPATH, './/option[2]')
    metro_area.click()

  def get_text_agent_tab_company_information(self):
    agent_tab = self.get_element_agent_tab()
    return agent_tab.find_element(By.XPATH, './/div/section/div/div/div/div/div[3]/div/form/div[1]/div[11]/div[1]/h5').text

  def get_text_agent_tab_your_question(self):
    agent_tab = self.get_element_agent_tab()
    return agent_tab.find_element(By.XPATH, './/div/section/div/div/div/div/div[3]/div/form/div[1]/div[12]/h5').text
  
  def get_text_agent_tab_SMS_disclaimer(self):
    agent_tab = self.get_element_agent_tab()
    return agent_tab.find_element(By.XPATH, ".//div[@class='SMSOptInDisclaimer']/p").text
  
  def get_element_agent_tab_submit_button(self):
    agent_tab = self.get_element_agent_tab()
    return agent_tab.find_element(By.CLASS_NAME, 'button.button--blue--solid.button--large-top')

  def get_element_article_careers_at_meritage(self):
    return self.driver.find_element(By.XPATH, "//article[@aria-label='Careers at Meritage']")
  
  def get_text_careers_meritage_header(self):
    careers_meritage = self.get_element_article_careers_at_meritage()
    return self.get_text_section_header(careers_meritage)
  
  def get_text_careers_meritage_body(self):
    careers_meritage = self.get_element_article_careers_at_meritage()
    return careers_meritage.find_element(By.XPATH, './/p[2]').text
  
  def get_element_careers_meritage_image(self):
    careers_meritage = self.get_element_article_careers_at_meritage()
    return self.get_element_section_placeholder_image(careers_meritage)
  
  def click_element_careers_meritage_button(self):
    html = self.get_html()
    careers_meritage = self.get_element_article_careers_at_meritage()
    self.click_element_section_button(careers_meritage)
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))

  def get_element_aside_ready_to_make_your_move(self):
    return self.driver.find_element(By.XPATH, "//aside[@aria-label=' Ready to make your move?']")
  
  def get_text_ready_move_aside_header(self):
    ready_move_aside = self.get_element_aside_ready_to_make_your_move()
    return self.get_text_section_header(ready_move_aside)
  
  def get_text_ready_move_aside_body(self):
    ready_move_aside = self.get_element_aside_ready_to_make_your_move()
    return self.get_text_section_body(ready_move_aside)
  
  def click_element_ready_move_aside_button(self):
    html = self.get_html()
    ready_move_aside = self.get_element_aside_ready_to_make_your_move()
    self.click_element_section_button(ready_move_aside)
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  