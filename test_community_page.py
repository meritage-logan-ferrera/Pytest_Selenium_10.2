from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
from page_community import CommunityPage
from page_base import BasePage
import math
import pytest
import time


@pytest.mark.usefixtures("init__driver")
class BasicTest():
  def test_image_carousel(self, driver_settings):
    community_page = CommunityPage(self.driver)
    community_page.close_cookies()
    slides = community_page.get_elements_carousel_slides()
    carousel_bool = False
    for i in range(len(slides)):
      if i != 0:
        community_page.click_element_next_arrow()
        time.sleep(1)
      slide = community_page.get_element_slide_number(i)
      result = self.driver.execute_script("return arguments[0].classList.contains('slick-active')", slide)
      if result:
        carousel_bool = True
      else:
        assert False
    assert carousel_bool 
  
  def test_compare_clickable(self, driver_settings):
    community_page = CommunityPage(self.driver)
    compare_button = community_page.get_element_compare()
    assert community_page.button_is_clickable(compare_button)
  
  def test_heart_clickable(self, driver_settings):
    community_page = CommunityPage(self.driver)
    heart_button = community_page.get_element_heart()
    assert community_page.button_is_clickable(heart_button)
  
  def test_header(self, driver_settings):
    community_page = CommunityPage(self.driver)
    header = community_page.get_text_main_header()
    assert '' != header
    
  def test_sub_header(self, driver_settings):
    community_page = CommunityPage(self.driver)
    sub_header = community_page.get_text_main_body()
    assert '' != sub_header
  
  def test_community_info(self, driver_settings):
    community_page = CommunityPage(self.driver)
    info = community_page.get_text_aside()
    assert (
      'Approx. Sq. Ft.' in info and
      'Bedrooms' in info and
      'Garage' in info and
      'Stories' in info
    )
  
  def test_brochure_clickable(self, driver_settings):
    community_page = CommunityPage(self.driver)
    brochure = community_page.get_element_brochure()
    assert community_page.button_is_clickable(brochure)
  
  def test_tabs_header(self, driver_settings):
    community_page = CommunityPage(self.driver)
    header = community_page.get_text_tabs_header()
    assert 'Explore what makes' in header
  
  def test_tabs_body(self, driver_settings):
    community_page = CommunityPage(self.driver)
    body = community_page.get_text_tabs_body()
    assert 'See why residents' in body
  
  def test_tab_images(self, driver_settings):
    community_page = CommunityPage(self.driver)
    tabs = community_page.get_elements_tabs()
    images_bool = False
    for i in range(len(tabs)):
      tab_image = community_page.get_element_tab_image(i)
      result = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].naturalWidth > 0", tab_image)
      if result:
        images_bool = True
        continue
      else:
        assert False
    assert images_bool and len(tabs) == 6
  
  def test_tabs_text(self, driver_settings):
    community_page = CommunityPage(self.driver)
    tabs = community_page.get_elements_tabs()
    text_bool = False
    for i in range(len(tabs)):
      tab_name = community_page.get_text_tab_name(i)
      match i:
        case 0:
          if 'Overview' in tab_name:
            text_bool = True
          else:
            assert False
        case 1:
          if 'Floorplans' in tab_name:
            text_bool = True
          else:
            assert False
        case 2:
          if 'Quick Move' in tab_name:
            text_bool = True
          else:
            assert False
        case 3:
          if 'Community' in tab_name:
            text_bool = True
          else:
            assert False
        case 4:
          if 'Homesite' in tab_name:
            text_bool = True
          else:
            assert False
        case 5:
          if 'Community Video' in tab_name:
            text_bool = True
          else:
            assert False
    assert text_bool and len(tabs) == 6
  
  # Some communities do not contain the approximate hoa or approximate tax rates elements. Need to include that in the test below.
  def test_tab_overview(self, driver_settings):
    community_page = CommunityPage(self.driver)
    community_page.close_cookies()
    community_address = community_page.get_text_community_address()
    directions_link = community_page.get_element_directions_link()
    body = community_page.get_text_below_directions()
    # hoa_header = community_page.get_text_hoa()
    # tax_header = community_page.get_text_tax_rate()
    # hoa_dynamic = community_page.get_text_hoa_dynamic()
    # tax_dynamic = community_page.get_text_tax_rate_dynamic()
    assert (
      len(community_address) > 2 and
      community_page.check_plain_button(directions_link) and
      '' != body
      # 'Approximate Monthly' in hoa_header and
      # '' != hoa_dynamic and
      # 'Approximate Tax' in tax_header and
      # '' != tax_dynamic
    )
  
  @pytest.mark.comm
  def test_tab_our_floorplans(self, driver_settings):
    community_page = CommunityPage(self.driver)
    community_page.close_cookies()
    time.sleep(1)
    community_page.click_element_tab(1)
    floorplan_elements = community_page.get_elements_floorplans()
    all_images_present = False
    for i in range(len(floorplan_elements)):
      image = community_page.get_element_floorplan_image(i)
      result = community_page.javascript_image(image)
      if result:
        all_images_present = True
      else:
        assert False
    for i in range(len(floorplan_elements)):
      overlay_text = community_page.get_text_floorplan_snipe_overlay(i)
      if overlay_text != '':
        all_overlays_present = True
      else:
        assert False
      
    plan = community_page.get_text_floorplan_plan(0)
    name = community_page.get_text_floorplan_name(0)
    community_page.click_element_floorplan_name(0)
      
    assert (
      len(floorplan_elements) > 0 and
      all_images_present and
      all_overlays_present and 
      len(plan) > 6 and
      name in self.driver.title
    )
  
  # some pages are supposed to have no qmis how do I fix this test to include that case
  def test_tab_qmis(self, driver_settings):
    community_page = CommunityPage(self.driver)
    community_page.close_cookies()
    community_page.click_element_tab(2)
    qmi_elements = community_page.get_elements_qmis()
    all_images_present = False
    for i in range(len(qmi_elements)):
      image = community_page.get_element_qmi_image(i)
      result = community_page.javascript_image(image)
      if result:
        all_images_present = True
      else:
        assert False
    
    if len(qmi_elements) != 0:
      container_plan_number = community_page.get_text_qmi_plan(0)
      community_page.click_element_qmi_name(0)
      new_page_plan_number = community_page.get_new_page_qmi_plan_number()

      assert (
        len(qmi_elements) > 0 and
        all_images_present and
        container_plan_number.lower() == new_page_plan_number().lower()
      )
    else:
      no_qmis_header = community_page.get_text_no_qmis()
      assert (
        len(qmi_elements) == 0 and
        'No Quick Move-in Homes available' in no_qmis_header
      )
    
  def test_tab_community(self, driver_settings):
    community_page = CommunityPage(self.driver)
    community_page.close_cookies()
    community_page.click_element_tab(3)
    rows = community_page.get_elements_community_rows()
    image_bool = False
    for i in range(len(rows)):
      image = community_page.get_element_row_image(i)
      result = community_page.javascript_image(image)
      if result:
        image_bool = True
      else:
        assert False
    assert image_bool
  
  # Some of these tabs do not have th iframe, need to include that case in the below test
  def test_tab_homesite(self, driver_settings):
    community_page = CommunityPage(self.driver)
    community_page.close_cookies()
    community_page.click_element_tab(4)
    button_clickable = community_page.check_clickable_homesite_button()
    # The iframe and/or the image are not always present on a community page, I would like to assert these in the test since they may differ between a specific community page and it's corresponding SIT page
    # iframe = community_page.get_element_iframe()
    # image = community_page.get_element_map_image()
    # result_iframe = self.driver.execute_script("return arguments[0].width > 0", iframe)
    # result_image = community_page.javascript_image(image)
    assert button_clickable
  
  def test_tab_video(self, driver_settings):
    community_page = CommunityPage(self.driver)
    community_page.close_cookies()
    community_page.click_element_tab(5)
    iframe = community_page.get_element_video_iframe()
    result = self.driver.execute_script("return arguments[0].width == '100%'", iframe)
    assert result
    
  def test_first_name_input(self, driver_settings):
    community_page = CommunityPage(self.driver)
    input_value = community_page.get_input_first_name(self.driver)
    assert 'test_input' == input_value 
  
  def test_last_name_input(self, driver_settings):
    community_page = CommunityPage(self.driver)
    input_value = community_page.get_input_last_name(self.driver)
    assert 'test_input' == input_value 
  
  # Test whether user can input into email address field
  def test_email_address_input(self, driver_settings):
    community_page = CommunityPage(self.driver)
    input_value = community_page.get_input_create_account_email_address(self.driver)
    assert 'test_input' == input_value 
  
  # Test whether user can input into phone number field
  def test_phone_number_input(self, driver_settings):
    community_page = CommunityPage(self.driver)
    input_value = community_page.get_input_phone_number(self.driver)
    assert 'test_input' == input_value 

  def test_company_name_input(self, driver_settings):
    community_page = CommunityPage(self.driver)
    community_page.close_cookies()
    community_page.click_element_agent_button()
    input_value = community_page.get_input_company_name(self.driver)
    assert 'test_input' == input_value
  
  def test_aside_button_is_clickable(self, driver_settings):
    community_page = CommunityPage(self.driver)
    result = community_page.check_aside_button_clickable()
    assert result

  pass

class Test_Denver_Horizon_Uptown_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get("https://www.meritagehomes.com/state/co/denver/horizon-uptown-the-meadow-collection")
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