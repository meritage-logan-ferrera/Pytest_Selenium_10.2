from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
from page_qmi import QMIPage
from page_base import BasePage
import math
import pytest
import time

@pytest.mark.usefixtures("init__driver")
class BasicTest():
  def test_image_carousel(self, driver_settings):
    qmi_page = QMIPage(self.driver)
    qmi_page.close_cookies()
    slides = qmi_page.get_elements_carousel_slides()
    carousel_bool = False
    for i in range(len(slides)):
      if i != 0:
        qmi_page.click_element_next_arrow()
        time.sleep(1)
      slide = qmi_page.get_element_slide_number(i)
      result = self.driver.execute_script("return arguments[0].classList.contains('slick-active')", slide)
      if result:
        carousel_bool = True
      else:
        assert False
    assert carousel_bool
  
  #CLicking this button does nothing in PROD
  def test_quick_move_in_button(self, driver_settings):
    qmi_page = QMIPage(self.driver)
    qmi_button = qmi_page.click_element_qmi_see_whats_included_button()
    result = qmi_page.button_is_clickable(qmi_button)
    assert result
  
  # Button does not appear on every QMI page in PROD
  def test_book_a_tour_button(self, driver_settings):
    qmi_page = QMIPage(self.driver)
    qmi_page.close_cookies()
    html = qmi_page.get_html()
    qmi_page.click_element_book_a_tour_button()
    result = self.driver.execute_script('return arguments[0].scrollTop != 0', html)
    assert result

  def test_plan(self, driver_settings):
    qmi_page = QMIPage(self.driver)
    plan_text = qmi_page.get_text_plan_number()
    plan_text = plan_text.replace('Plan #', '')
    assert len(plan_text) != 0
  
  def test_qmi_header(self, driver_settings):
    qmi_page = QMIPage(self.driver)
    qmi_name = qmi_page.get_text_qmi_name_header()
    assert '' != qmi_name
  
  def test_community_link(self, driver_settings):
    qmi_page = QMIPage(self.driver)
    qmi_page.close_cookies()
    community_name = qmi_page.get_text_community()
    qmi_page.click_element_community_button()
    new_page_header = qmi_page.new_page_get_community_name()
    assert community_name in new_page_header or new_page_header in community_name
  
  def test_community_description(self, driver_settings):
    qmi_page = QMIPage(self.driver)
    description = qmi_page.get_text_qmi_description()
    assert '' != description
  
  def test_estimated_completion(self, driver_settings):
    qmi_page = QMIPage(self.driver)
    estimated = qmi_page.get_text_qmi_estimated_completion()
    estimated = estimated.replace('Estimated Completion for this home:', '')
    assert len(estimated) != 0
  
  def test_home_address(self, driver_settings):
    qmi_page = QMIPage(self.driver)
    home_adr = qmi_page.get_text_qmi_home_address()
    assert len(home_adr) != 0

  def test_qmi_stats(self, driver_settings):
    qmi_page = QMIPage(self.driver)
    stats = qmi_page.get_text_aside()
    assert (
      'Approx. Sq. Ft.' in stats and
      'Bedrooms' in stats and
      'Garage' in stats and
      'Stories' in stats
    )
  
  def test_floorplan_tab(self, driver_settings):
    qmi_page = QMIPage(self.driver)
    image = qmi_page.get_element_floorplan_image()
    result = qmi_page.javascript_image(image)
    assert result
  
  @pytest.mark.iframe
  def test_virtual_walkthrough_tab(self, driver_settings):
    qmi_page = QMIPage(self.driver)
    qmi_page.close_cookies()
    qmi_page.click_element_virtual_walkthrough_button()
    time.sleep(2)
    iframe = qmi_page.get_element_virtual_walkthrough_iframe()
    result = self.driver.execute_script("return arguments[0].width == '100%' || arguments[0].width > 0", iframe)
    assert result
  
  def test_download_pdf_tab(self, driver_settings):
    qmi_page = QMIPage(self.driver)
    qmi_page.close_cookies()
    qmi_page.click_element_download_pdf()
    assert 'MRT_DEN_Ridgeline_Vista_3263_Snowberry_Web.pdf' or 'PDF.js viewer' in self.driver.title
  
  def test_interior_package_tab(self, driver_settings):
    qmi_page = QMIPage(self.driver)
    qmi_page.close_cookies()
    qmi_page.click_element_interior_package_button()
    image = qmi_page.get_element_interior_package_image()
    result = qmi_page.javascript_image(image)
    assert result
  
  def test_elevation_tab(self, driver_settings):
    qmi_page = QMIPage(self.driver)
    qmi_page.close_cookies()
    qmi_page.click_element_elevation_button()
    image = qmi_page.get_element_elevation_image()
    result = qmi_page.javascript_image(image)
    assert result

  def test_promotion_section(self, driver_settings):
    qmi_page = QMIPage(self.driver)
    qmi_page.close_cookies()
    image = qmi_page.get_element_promotion_image()
    result = qmi_page.javascript_image(image)
    button = qmi_page.get_element_promotion_button()
    button_clickable = qmi_page.button_is_clickable(button)
    assert result and button_clickable
  
  def test_buttons(self, driver_settings):
    qmi_page = QMIPage(self.driver)
    qmi_page.close_cookies()
    compare_button = qmi_page.get_element_compare_qmi_button()
    save_button = qmi_page.get_element_save_favorites_button()
    result_1 = qmi_page.button_is_clickable(compare_button)
    result_2 = qmi_page.button_is_clickable(save_button)
    assert result_1 and result_2

  def test_first_name_input(self, driver_settings):
    qmi_page = QMIPage(self.driver)
    input_value = qmi_page.get_input_first_name(self.driver)
    assert 'test_input' == input_value 
  
  def test_last_name_input(self, driver_settings):
    qmi_page = QMIPage(self.driver)
    input_value = qmi_page.get_input_last_name(self.driver)
    assert 'test_input' == input_value 
  
  # Test whether user can input into email address field
  def test_email_address_input(self, driver_settings):
    qmi_page = QMIPage(self.driver)
    input_value = qmi_page.get_input_create_account_email_address(self.driver)
    assert 'test_input' == input_value 
  
  # Test whether user can input into phone number field
  def test_phone_number_input(self, driver_settings):
    qmi_page = QMIPage(self.driver)
    input_value = qmi_page.get_input_phone_number(self.driver)
    assert 'test_input' == input_value 

  def test_company_name_input(self, driver_settings):
    qmi_page = QMIPage(self.driver)
    qmi_page.close_cookies()
    qmi_page.click_element_agent_button()
    input_value = qmi_page.get_input_company_name(self.driver)
    assert 'test_input' == input_value
  
  def test_aside_button_is_clickable(self, driver_settings):
    qmi_page = QMIPage(self.driver)
    result = qmi_page.check_aside_button_clickable()
    assert result

  pass

class Test_Snowberry_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get("https://www.meritagehomes.com/state/co/denver/ridgeline-vista/snowberry-3263/538-lost-lake-street")
    self.driver.set_window_position(0,0)
    
  
# class Test_X_Page(BasicTest):
#   @pytest.fixture()
#   def driver_settings(self):
#     self.driver.get("placeholder")
#     self.driver.set_window_position(0,0)
#     return "California"
  

# class Test_Y_Page(BasicTest):
#   @pytest.fixture()
#   def driver_settings(self):
#     self.driver.get("placeholder")
#     self.driver.set_window_position(0,0)
#     return "Colorado"