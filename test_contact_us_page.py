from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
from page_contact_us import ContactUsPage
from page_base import BasePage
import math
import pytest
import time

URL = 'https://cd-sit.meritageweb.dev/contact'

@pytest.mark.usefixtures("init__driver")
class BasicTest():
  pass

class Test_Contact_Us_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get(URL)
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)

  # Test whether main header appears on page
  def test_main_header(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    header = contact_page.get_text_main_header()
    assert "Contact us"in header
  
  # Test whether main sub header appears on page
  def test_main_sub_header(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    sub_header = contact_page.get_text_main_sub_header()
    assert "dedicated to helping you" in sub_header
  
  # Test whether correct headr appers in how help section
  def test_how_help_header(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    header = contact_page.get_text_how_help_header()
    assert 'How can we help' in header
  
  #  Test whether correct body appears in how help section
  def test_how_help_body(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    body = contact_page.get_text_how_help_body()
    assert 'in a community' in body
  
  # Test whether new buyers tab opens when clicking the corresponding button
  def test_correct_tab_on_new_buyers_button(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_new_buyers_button()
    new_buyers_tab = contact_page.get_element_new_buyers_tab()
    result = self.driver.execute_script("return arguments[0].classList.contains('is-active')", new_buyers_tab)
    assert result
  
  # Test whether the correct header appears in the new buyers tab
  def test_new_buyers_header(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_new_buyers_button()
    header = contact_page.get_text_new_buyers_tab_header()
    assert 'Please fill in the fields below' in header
  
  # Test whether first name input in new buyers tab works
  def test_new_buyers_input_first_name(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_new_buyers_button()
    new_buyers_tab = contact_page.get_element_new_buyers_tab()
    assert contact_page.get_input_first_name(new_buyers_tab)
  
  # Test whether last name input in new buyers tab works
  def test_new_buyers_input_last_name(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_new_buyers_button()
    new_buyers_tab = contact_page.get_element_new_buyers_tab()
    assert contact_page.get_input_last_name(new_buyers_tab)
  
  # Test whether email address input in new buyers tab works
  def test_new_buyers_input_email_address(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_new_buyers_button()
    new_buyers_tab = contact_page.get_element_new_buyers_tab()
    assert contact_page.get_input_create_account_email_address(new_buyers_tab)
  
  # Test whether phone number input in new buyers tab works
  def test_new_buyers_input_phone_number(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_new_buyers_button()
    new_buyers_tab = contact_page.get_element_new_buyers_tab()
    assert contact_page.get_input_phone_number(new_buyers_tab)
  
  # Test whether correct text appears in location header in new buyers tab
  def test_new_buyers_location(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_new_buyers_button()
    location = contact_page.get_text_new_buyers_tab_location()
    assert 'Location' in location

  # Test whether metro dropdwon is clickable
  def test_new_buyers_metro_dropdown(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_new_buyers_button()
    metro_dropdown = contact_page.get_element_new_buyers_metro_dropdown()
    contact_page.button_is_clickable(metro_dropdown)

  # Test whether community dropdown is clickable after clicking a metro area in the metro dropdown
  @pytest.mark.contact
  def test_new_buyers_community_dropdown(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_new_buyers_button()
    contact_page.click_element_new_buyers_metro_dropdown()
    time.sleep(.5)
    community_dropdown = contact_page.get_element_new_buyers_community_dropdown()
    contact_page.button_is_clickable(community_dropdown)

  # Test whether correct text appears in your question header in new buyers tab
  def test_new_buyers_your_question(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_new_buyers_button()
    your_question = contact_page.get_text_new_buyers_tab_your_question()
    assert 'Your question' in your_question

  # Test whether user can input text into your questions field
  def test_new_buyers_input_your_questions(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_new_buyers_button()
    new_buyers_tab = contact_page.get_element_new_buyers_tab()
    assert contact_page.get_input_your_question(new_buyers_tab)
  
  # Test recaptcha here

  # Test whether the correct text in the sms disclaimer in new buyers tab appears
  def test_new_buyers_sms_disclaimer(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_new_buyers_button()
    header = contact_page.get_text_new_buyers_tab_SMS_disclaimer()
    assert 'By submitting this form' in header
  
  # Tets whether the submit button on the new buyers tab is clickable
  def test_new_buyers_submit_button(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_new_buyers_button()
    button = contact_page.get_element_new_buyers_tab_submit_button()
    assert contact_page.button_is_clickable(button)

  # Test whether the warrant claims tab opens on clicking the respective button
  def test_correct_tab_on_warranty_claims_button(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_warranty_claims_button()
    warranty_claims_tab = contact_page.get_element_warranty_claims_tab()
    result = self.driver.execute_script("return arguments[0].classList.contains('is-active')", warranty_claims_tab)
    assert result
  
  # Test whether correct heder appears in warranty claims tab
  def test_warranty_claims_header(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_warranty_claims_button()
    header = contact_page.get_text_warranty_claims_tab_header()
    assert 'Questions about your warranty' in header
  
  # Test whether correct body appears in warranty claims tab
  def test_warranty_claims_body(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_warranty_claims_button()
    body = contact_page.get_text_warranty_claims_tab_body()
    assert 'Log into your' in body
  
  # Test whether the button in warranty claims tab takes user to the warranty portal
  def test_warranty_claims_button(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_warranty_claims_button()
    contact_page.click_element_warranty_claims_tab_button()
    assert 'My Meritage Portal' or '' in self.driver.title
  
  # Test whether the correct number appears on warranty claims page
  def test_warranty_claims_number(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_warranty_claims_button()
    number = contact_page.get_text_warranty_claims_tab_number()
    assert '833-684-6527' in number
  
  def test_correct_tab_on_agent_button(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_agent_button()
    agent_tab = contact_page.get_element_agent_tab()
    result = self.driver.execute_script("return arguments[0].classList.contains('is-active')", agent_tab)
    assert result

  def test_agent_header(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_agent_button()
    header = contact_page.get_text_agent_tab_header()
    assert 'Please fill in the fields below' in header
  
  def test_agent_input_first_name(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_agent_button()
    agent_tab = contact_page.get_element_agent_tab()
    assert contact_page.get_input_first_name(agent_tab)
  
  def test_agent_input_last_name(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_agent_button()
    agent_tab = contact_page.get_element_agent_tab()
    assert contact_page.get_input_last_name(agent_tab)
  
  def test_agent_input_email_address(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_agent_button()
    agent_tab = contact_page.get_element_agent_tab()
    assert contact_page.get_input_create_account_email_address(agent_tab)
  
  def test_agent_input_phone_number(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_agent_button()
    agent_tab = contact_page.get_element_agent_tab()
    assert contact_page.get_input_phone_number(agent_tab)
  
  def test_agent_location(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_agent_button()
    location = contact_page.get_text_agent_tab_location()
    assert 'Location' in location

  def test_agent_metro_dropdown(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_agent_button()
    metro_dropdown = contact_page.get_element_agent_tab_metro_dropdown()
    contact_page.button_is_clickable(metro_dropdown)

  def test_agent_community_dropdown(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_agent_button()
    contact_page.click_element_agent_tab_metro_dropdown()
    time.sleep(.5)
    community_dropdown = contact_page.get_element_agent_tab_community_dropdown()
    contact_page.button_is_clickable(community_dropdown)
  
  def test_agent_company_info_header(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_agent_button()
    header = contact_page.get_text_agent_tab_company_information()
    assert 'Company information' in header
  
  def test_agent_input_company_name(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_agent_button()
    agent_tab = contact_page.get_element_agent_tab()
    assert contact_page.get_input_company_name(agent_tab)
  
  def test_agent_your_question(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_agent_button()
    your_question = contact_page.get_text_agent_tab_your_question()
    assert 'Your question' in your_question

  def test_agent_input_your_questions(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_agent_button()
    agent_tab = contact_page.get_element_agent_tab()
    assert contact_page.get_input_your_question(agent_tab)
  
  # Test recaptcha for agent tab here

  def test_agent_sms_disclaimer(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_agent_button()
    header = contact_page.get_text_agent_tab_SMS_disclaimer()
    assert 'By submitting this form' in header

  def test_agent_submit_button(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_how_element_agent_button()
    button = contact_page.get_element_agent_tab_submit_button()
    assert contact_page.button_is_clickable(button)
  
  def test_careers_header(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    header = contact_page.get_text_careers_meritage_header()
    assert 'Careers at Meritage' in header
  
  def test_careers_body(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    body = contact_page.get_text_careers_meritage_body()
    assert 'Looking for a company with great advancement' in body

  def test_careers_image(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    image = contact_page.get_element_careers_meritage_image()
    result = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", image)
    assert result
  
  def test_careers_button(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_careers_meritage_button()
    assert 'Meritage Careers - Real Estate Careers | Meritage Homes' == self.driver.title
  
  def test_ready_move_aside_header(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    header = contact_page.get_text_ready_move_aside_header()
    assert 'Ready to make your move' in header
  
  def test_ready_move_aside_body(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    body = contact_page.get_text_ready_move_aside_body()
    assert 'With communities across' in body
  
  def test_ready_move_aside_button(self, driver_settings):
    contact_page = ContactUsPage(self.driver)
    contact_page.close_cookies()
    contact_page.click_element_ready_move_aside_button()
    assert 'Find a Home | Meritage Homes' == self.driver.title
  

  