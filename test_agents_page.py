from ast import match_case
from pickletools import ArgumentDescriptor
from venv import create
from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
from page_agents import AgentsPage
from page_base import BasePage
import math
import pytest
import time

URL = 'https://www.meritagehomes.com/agents'

@pytest.mark.usefixtures("init__driver")
class BasicTest():
  pass

class Test_Agents_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get(URL)
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)
  
  def test_main_header(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    header = agents_page.get_text_main_header()
    assert 'kind of a big deal' in header
  
  def test_main_sub_header(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    sub_header = agents_page.get_text_main_sub_header()
    assert 'Thanks for really rocking it' in sub_header
  
  def test_main_button_1(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    html = agents_page.get_html()
    agents_page.close_cookies()
    agents_page.click_elemenet_main_button_1()
    result = self.driver.execute_script("return arguments[0].scrollTop > 100", html)
    assert result
  
  def test_main_button_2(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    html = agents_page.get_html()
    agents_page.close_cookies()
    agents_page.click_elemenet_main_button_2()
    result = self.driver.execute_script("return arguments[0].scrollTop > 100", html)
    assert result
  
  def test_aside_1_header(self):
    agents_page = AgentsPage(self.driver)
    header = agents_page.get_text_aside_1_header()
    assert 'When you sell with us' in header
  
  def test_aside_1_body(self):
    agents_page = AgentsPage(self.driver)
    body = agents_page.get_text_aside_1_body()
    assert 'Watching you hand over the keys to' in body
  
  def test_aside_1_image(self):
    agents_page = AgentsPage(self.driver)
    image = agents_page.get_element_aside_1_image()
    result = self.drive.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", image)
    assert result
  
  @pytest.mark.parametrize('container', [1, 2, 3, 4, 5])
  def test_article_1_containers(self, container, driver_settings):
    agents_page = AgentsPage(self.driver)
    header = agents_page.get_text_article_1_container_header(container)
    body = agents_page.get_text_article_1_container_body(container)
    image = agents_page.get_element_article_1_container_image(container)
    result = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", image)
    match container:
      case 1:
        assert (
          'advanced commission' in header and
          'not too good to be true' in body and
          result
        )
      case 2:
        assert (
          'Enjoy exciting local perks' in header and
          'Earn local perks' in body and
          result
        )
      case 3:
        assert (
          'Regular updates to keep you in the loop' in header and
          'here to help you succeed' in body and
          result
        )
      case 4:
        assert (
          'Register your clients online or by phone' in header and
          'Create an account below to register your clients' in body and
          result
        )
      case 5:
        assert (
          'Tutorials on how to best sell new homes' in header and
          'Knowledge is power' in body and
          result
        )
      
  # Test whether the main header above article 2 is disolaying the correct information
  def test_article_2_main_header(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    header = agents_page.get_text_article_2_call_header()
    assert 'Learn more about agents rock by calling' in header
  
  # Test whether the correct header is appearing in article 2
  def test_article_2_header(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    header = agents_page.get_text_article_2_header()
    assert 'Meritage Agent Program Terms' in header
  
  # Test whether the correct text displays in each element of the numbered list in article 2
  def test_article_2_numbered_list_text(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    numbered_list = agents_page.get_text_article_2_body_numbered_list()
    list_correct = False
    if 'Registration' in numbered_list[0]:
      list_correct = True
    else:
      assert False
    if 'At close of escrow' in numbered_list[1]:
      list_correct = True
    else:
      assert False
    if 'Any representation by real estate' in numbered_list[2]:
      list_correct = True
    else:
      assert False
    if 'Real estate agent must hold an active' in numbered_list[3]:
      list_correct = True
    else:
      assert False
    if 'If real estate agent desires to change' in numbered_list[4]:
      list_correct = True
    else:
      assert False
    
    assert list_correct
  
  # Test whether the correct text displays in each element of the numbered list in article 2
  def test_article_2_one_sublist_text(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    sub_list = agents_page.get_text_article_2_body_one_sublist()
    list_correct = False
    if 'Unless preregistered' in sub_list[0]:
      list_correct = True
    else:
      assert False
    if 'The real estate agent may' in sub_list[1]:
      list_correct = True
    else:
      assert False
    if 'A registration is valid solely' in sub_list[2]:
      list_correct = True
    else:
      assert False
    if 'A valid registration will remain valid for 30' in sub_list[3]:
      list_correct = True
    else:
      assert False
    if 'The information on the registration form' in sub_list[4]:
      list_correct = True
    else:
      assert False
    if 'If prospective buyer returns' in sub_list[5]:
      list_correct = True
    else:
      assert False
    
    assert list_correct
  
  # Test whether correct text is displayed in paragraph after article 2 list
  def test_article_2_bottom_paragaph(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    paragraph = agents_page.get_text_article_2_bottom()
    assert 'Meritage reserves the right to provide' in paragraph

  # Test whether the correct text is displayed in article 2's disclaimer
  def test_article_2_disclaimer(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    disclaimer_text = agents_page.get_text_article_2_disclaimer()
    list_correct = False
    if 'Commission limited in all events' in disclaimer_text[0]:
      list_correct = True
    else:
      assert False
    if 'See sales agent for a written copy' in disclaimer_text[1]:
      list_correct = True
    else:
      assert False
    
    assert list_correct
  
  # Test that clicking the sing in tab opens the correct form
  def test_sign_in_form_on_sign_in_tab_click(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    agents_page.close_cookies()
    agents_page.click_element_create_account_button()
    agents_page.click_element_sign_in_button()
    sign_in_form = agents_page.get_element_sign_in_form()
    result = self.driver.execute_script("return arguments[0].classList.contains('is-active')", sign_in_form)
    assert result
  
  # Test that clicking the create account tab opens the correct form
  def test_create_account_form_on_create_account_tab_click(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    agents_page.close_cookies()
    agents_page.click_element_create_account_button()
    create_account_form = agents_page.get_element_create_account_form()
    result = self.driver.execute_script("return arguments[0].classList.contains('is-active')", create_account_form)
    assert result

  # Test whether correct body displayed in sign in form
  def test_sign_in_body(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    body = agents_page.get_text_sign_in_form_body()
    assert 'track of your client' in body
  
  # Test whether email input works on sign in form
  def test_sign_in_email_input(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    sign_in_form = agents_page.get_element_sign_in_form()
    assert agents_page.get_input_sign_in_email(sign_in_form)
    
  # Test whether password input works on sign in form
  def test_sign_in_password_input(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    sign_in_form = agents_page.get_element_sign_in_form()
    assert agents_page.get_input_sign_in_password(sign_in_form)
  
  # Test whether the sign in button is clickable
  def test_sign_in_button_is_clickable(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    assert agents_page.check_element_clickable_sign_in_button()
  
  # Test whether the get help button opens the correct forgot password form when clicked
  def test_forgot_password_tab_on_sign_in_get_help_press(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    agents_page.close_cookies()
    agents_page.click_element_sign_in_get_help_button()
    forgot_password_tab = agents_page.get_element_forgot_password_tab()
    result = self.driver.execute_script("return arguments[0].style.display == 'block'", forgot_password_tab)
    assert result
  
  # Test whether the correct body is displayed in the create account form
  def test_create_account_body(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    body = agents_page.get_text_create_account_form_body()
    assert 'track of your client' in body
  
  # Test whether first name input works on create account form
  def test_create_account_first_name_input(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    create_account_form = agents_page.get_element_create_account_form()
    assert agents_page.get_input_first_name(create_account_form)
  
  # Test whether last_name input works on create account form
  def test_create_account_last_name_input(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    create_account_form = agents_page.get_element_create_account_form()
    assert agents_page.get_input_last_name(create_account_form)
  
  # Test whether email_address input works on create account form
  def test_create_account_email_address_input(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    create_account_form = agents_page.get_element_create_account_form()
    assert agents_page.get_input_create_account_email_address(create_account_form)
  
  # Test whether phone_number input works on create account form
  def test_create_account_phone_number_input(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    create_account_form = agents_page.get_element_create_account_form()
    assert agents_page.get_input_phone_number(create_account_form)
  
  # Test whether password input works on create account form
  def test_create_account_password_input(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    create_account_form = agents_page.get_element_create_account_form()
    assert agents_page.get_input_create_account_password(create_account_form)
  
  # Test whether confirm_password input works on create account form
  def test_create_account_confirm_password_input(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    create_account_form = agents_page.get_element_create_account_form()
    assert agents_page.get_input_confirm_password(create_account_form)
  
  # Test whether the sleect metro area dropdown is clickable in create an account form
  def test_create_account_select_metro_is_clickable(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    select_metro = agents_page.get_element_create_account_metro_dropdown()
    return agents_page.button_is_clickable(select_metro)
  
  # Test whether the correct company infomration sub header is displayed in create account form
  def test_create_account_company_information_header(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    header = agents_page.get_text_create_account_form_company_info()
    assert 'Company information' in header
  
  # Test whether company_name input works on create account form
  def test_create_account_company_name_input(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    create_account_form = agents_page.get_element_create_account_form()
    assert agents_page.get_input_company_name(create_account_form)
  
  # Test whether address_1 input works on create account form
  def test_create_account_address_1_input(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    create_account_form = agents_page.get_element_create_account_form()
    assert agents_page.get_input_address_1(create_account_form)
  
  # Test whether address_2 input works on create account form
  def test_create_account_address_2_input(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    create_account_form = agents_page.get_element_create_account_form()
    assert agents_page.get_input_address_2(create_account_form)
  
  # Test whether city input works on create account form
  def test_create_account_city_input(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    create_account_form = agents_page.get_element_create_account_form()
    assert agents_page.get_input_city(create_account_form)

  # Test whether zip input works on create account form
  def test_create_account_zip_input(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    create_account_form = agents_page.get_element_create_account_form()
    assert agents_page.get_input_zip(create_account_form)
  
  # Test whether the state dropdown is clickable in create an account form
  def test_create_account_state_is_clickable(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    state_metro = agents_page.get_element_create_state_dropdown()
    return agents_page.button_is_clickable(state_metro)
  
  # Test whether the client registration button opens the optional register client form and that the inputs in the optional form work
  def test_create_account_optional_form_on_register_client_click_and_optional_input_forms(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    agents_page.close_cookies()
    agents_page.click_element_create_account_button()
    agents_page.click_element_create_account_optional_register_client()
    optional_form = agents_page.get_element_create_account_optional_form()
    result = self.driver.execute_script("return arguments[0].style.display != 'none'", optional_form)
    
    client_first_name_works = agents_page.get_input_client_first_name()
    client_last_name_works = agents_page.get_input_client_last_name()
    client_email_address_works = agents_page.get_input_client_email_address()

    ack_button = agents_page.get_element_create_account_optional_ack_button()
    metro_dropdown = agents_page.get_element_create_account_client_metro_area()
    community_dropdown = agents_page.get_element_create_account_client_community()
    ack_is_clickable = agents_page.button_is_clickable(ack_button)
    metro_is_clickable = agents_page.button_is_clickable(metro_dropdown)
    community_is_clickable = agents_page.button_is_clickable(community_dropdown)

    assert(
      result and
      client_first_name_works and
      client_last_name_works and
      client_email_address_works and
      ack_is_clickable and
      metro_is_clickable and
      community_is_clickable
    )


  # Test whether the correct text displays in each element of the numbered list in create account form
  def test_create_account_numbered_list_text(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    agents_page.close_cookies()
    agents_page.click_element_create_account_button()
    numbered_list = agents_page.get_text_create_account_body_numbered_list()
    list_correct = False
    if 'Registration' in numbered_list[0]:
      list_correct = True
    else:
      assert False, numbered_list[0]
    if 'At close of escrow' in numbered_list[1]:
      list_correct = True
    else:
      assert False
    if 'Any representation by real estate' in numbered_list[2]:
      list_correct = True
    else:
      assert False
    if 'Real estate agent must hold an active' in numbered_list[3]:
      list_correct = True
    else:
      assert False
    if 'If real estate agent desires to change' in numbered_list[4]:
      list_correct = True
    else:
      assert False
    
    assert list_correct
  
  # Test whether the correct text displays in each element of the numbered list in create account form
  def test_create_account_one_sublist_text(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    agents_page.close_cookies()
    agents_page.click_element_create_account_button()
    sub_list = agents_page.get_text_create_account_body_one_sublist()
    list_correct = False
    if 'Unless preregistered' in sub_list[0]:
      list_correct = True
    else:
      assert False
    if 'The real estate agent may' in sub_list[1]:
      list_correct = True
    else:
      assert False
    if 'A registration is valid solely' in sub_list[2]:
      list_correct = True
    else:
      assert False
    if 'A valid registration will remain valid for 30' in sub_list[3]:
      list_correct = True
    else:
      assert False
    if 'The information on the registration form' in sub_list[4]:
      list_correct = True
    else:
      assert False
    if 'If prospective buyer returns' in sub_list[5]:
      list_correct = True
    else:
      assert False
    
    assert list_correct
  
  # Test whether correct text is displayed in paragraph after the create account form list
  @pytest.mark.agents
  def test_create_account_bottom_paragaph(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    agents_page.close_cookies()
    agents_page.click_element_create_account_button()
    paragraph = agents_page.get_text_create_account_bottom()
    assert 'Meritage reserves the right to provide' in paragraph

  # Test whether the termas and conditions button in the create account form is clickable
  def test_create_account_terms_button(self):
    agents_page = AgentsPage(self.driver)
    button = agents_page.get_element_create_account_terms_and_conditions_button()
    assert agents_page.button_is_clickable(button)
  
  # Test whether the termas and conditions button in the create account form is clickable
  def test_create_account_terms_button(self):
    agents_page = AgentsPage(self.driver)
    button = agents_page.get_element_create_account_complete_registration_button()
    assert agents_page.button_is_clickable(button)

    # up to Lets Work Together