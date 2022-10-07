from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
from page_floorplan import FloorplanPage
from page_base import BasePage
import math
import pytest
import time


@pytest.mark.usefixtures("init__driver")
class BasicTest():
  def test_image_carousel(self, driver_settings):
    floorplan_page = FloorplanPage(self.driver)
    floorplan_page.close_cookies()
    slides = floorplan_page.get_elements_carousel_slides()
    carousel_bool = False
    for i in range(len(slides)):
      if i != 0:
        floorplan_page.click_element_next_arrow()
        time.sleep(1)
      slide = floorplan_page.get_element_slide_number(i)
      result = self.driver.execute_script("return arguments[0].classList.contains('slick-active')", slide)
      if result:
        carousel_bool = True
      else:
        assert False
    assert carousel_bool 
  
  @pytest.mark.bruhs
  def test_plan_number_sub_header(self, driver_settings):
    floorplan_page = FloorplanPage(self.driver)
    plan_header = floorplan_page.get_text_plan_sub_header()
    plan_header = plan_header.replace('Plan #', '')
    assert len(plan_header) != 0

  def test_header(self, driver_settings):
    floorplan_page = FloorplanPage(self.driver)
    header = floorplan_page.get_text_main_header()
    assert '' != header
    
  def test_sub_header(self, driver_settings):
    floorplan_page = FloorplanPage(self.driver)
    sub_header = floorplan_page.get_text_main_body()
    assert '' != sub_header
  
  def test_floorplan_info(self, driver_settings):
    floorplan_page = FloorplanPage(self.driver)
    info = floorplan_page.get_text_aside()
    assert (
      'Approx. Sq. Ft.' in info and
      'Bedrooms' in info and
      'Garage' in info and
      'Stories' in info
    )
  
  def test_floorplan_tab(self, driver_settings):
    floorplan_page = FloorplanPage(self.driver)
    image = floorplan_page.get_element_floorplan_image()
    result = floorplan_page.javascript_image(image)
    assert result
  
  def test_virtual_walkthrough_tab(self, driver_settings):
    floorplan_page = FloorplanPage(self.driver)
    floorplan_page.close_cookies()
    floorplan_page.click_element_virtual_walkthrough_button()
    time.sleep(2)
    iframe = floorplan_page.get_element_virtual_walkthrough_iframe()
    result = self.driver.execute_script("return arguments[0].width == '100%' || arguments[0].width > 0", iframe)
    assert result
  
  def test_download_pdf_tab(self, driver_settings):
    floorplan_page = FloorplanPage(self.driver)
    floorplan_page.close_cookies()
    floorplan_page.click_element_download_pdf()
    assert (not '') or 'PDF.js viewer' in self.driver.title
  
  def test_promotion_section(self, driver_settings):
    floorplan_page = FloorplanPage(self.driver)
    floorplan_page.close_cookies()
    image = floorplan_page.get_element_promotion_image()
    result = floorplan_page.javascript_image(image)
    button = floorplan_page.get_element_promotion_button()
    button_clickable = floorplan_page.button_is_clickable(button)
    assert result and button_clickable

  def test_home_features_section(self, driver_settings):
    floorplan_page = FloorplanPage(self.driver)
    image = floorplan_page.get_element_home_features_image()
    result = floorplan_page.javascript_image(image)
    assert result

  def test_tabs_header(self, driver_settings):
    floorplan_page = FloorplanPage(self.driver)
    header = floorplan_page.get_text_tabs_header()
    assert 'possible with this plan' in header
  
  def test_tabs_body(self, driver_settings):
    floorplan_page = FloorplanPage(self.driver)
    body = floorplan_page.get_text_tabs_body()
    assert 'See the various elevations' in body
  
  def test_tab_images(self, driver_settings):
    floorplan_page = FloorplanPage(self.driver)
    tabs = floorplan_page.get_elements_tabs()
    images_bool = False
    for i in range(len(tabs)):
      tab_image = floorplan_page.get_element_tab_image(i)
      result = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", tab_image)
      if result:
        images_bool = True
        continue
      else:
        assert False
    assert images_bool and len(tabs) == 3
  
  def test_tabs_text(self, driver_settings):
    floorplan_page = FloorplanPage(self.driver)
    tabs = floorplan_page.get_elements_tabs()
    text_bool = False
    for i in range(len(tabs)):
      tab_name = floorplan_page.get_text_tab_name(i)
      match i:
        case 0:
          if 'Elevations' in tab_name:
            text_bool = True
          else:
            assert False
        case 1:
          if 'Directions' in tab_name:
            text_bool = True
          else:
            assert False
        case 2:
          if 'Homesite' in tab_name:
            text_bool = True
          else:
            assert False
    assert text_bool and len(tabs) == 3

  def test_tab_elevations(self, driver_settings):
    floorplan_page = FloorplanPage(self.driver)
    floorplan_page.close_cookies()
    containers = floorplan_page.get_elements_elevations_containers()
    final_bool = False
    for i in range(len(containers)):
      image = floorplan_page.get_element_container_image(i)
      text = floorplan_page.get_text_container_elevation(i)
      button = floorplan_page.get_element_container_button(i)
      result = floorplan_page.javascript_image(image)
      text_final = text.replace('Elevation', '')
      button_clickable = floorplan_page.button_is_clickable(button)
      if result and button_clickable and len(text_final) != 0:
        final_bool = True
      else:
        assert False, len(text_final)
    assert final_bool
  
  def test_tab_directions(self, driver_settings):
    floorplan_page = FloorplanPage(self.driver)
    floorplan_page.close_cookies()
    floorplan_page.click_element_tab(1)
    community_address = floorplan_page.get_text_directions_community_adr()
    directions_link = floorplan_page.get_element_directions_button()
    body = floorplan_page.get_text_below_directions()
    assert (
      len(community_address) > 2 and
      floorplan_page.check_plain_button(directions_link) and
      '' != body
    )

  def test_tab_homesite(self, driver_settings):
    floorplan_page = FloorplanPage(self.driver)
    floorplan_page.close_cookies()
    floorplan_page.click_element_tab(2)
    button_clickable = floorplan_page.check_clickable_homesite_button()
    assert button_clickable
  
  def test_first_name_input(self, driver_settings):
    floorplan_page = FloorplanPage(self.driver)
    input_value = floorplan_page.get_input_first_name(self.driver)
    assert 'test_input' == input_value 
  
  def test_last_name_input(self, driver_settings):
    floorplan_page = FloorplanPage(self.driver)
    input_value = floorplan_page.get_input_last_name(self.driver)
    assert 'test_input' == input_value 
  
  # Test whether user can input into email address field
  def test_email_address_input(self, driver_settings):
    floorplan_page = FloorplanPage(self.driver)
    input_value = floorplan_page.get_input_create_account_email_address(self.driver)
    assert 'test_input' == input_value 
  
  # Test whether user can input into phone number field
  def test_phone_number_input(self, driver_settings):
    floorplan_page = FloorplanPage(self.driver)
    input_value = floorplan_page.get_input_phone_number(self.driver)
    assert 'test_input' == input_value 

  def test_company_name_input(self, driver_settings):
    floorplan_page = FloorplanPage(self.driver)
    floorplan_page.close_cookies()
    floorplan_page.click_element_agent_button()
    input_value = floorplan_page.get_input_company_name(self.driver)
    assert 'test_input' == input_value
  
  def test_aside_button_is_clickable(self, driver_settings):
    floorplan_page = FloorplanPage(self.driver)
    result = floorplan_page.check_aside_button_clickable()
    assert result

  pass


class Test_The_Brook_2411_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get("https://www.meritagehomes.com/state/co/denver/horizon-uptown-the-meadow-collection/the-brook---2411")
    self.driver.set_window_position(0,0)
    return "Arizona"
    
  
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