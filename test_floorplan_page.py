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
  
  def test_tabs_header(self, driver_settings):
    floorplan_page = FloorplanPage(self.driver)
    header = floorplan_page.get_text_tabs_header()
    assert 'Explore what makes' in header
  
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
      result = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].naturalWidth > 0", tab_image)
      if result:
        images_bool = True
        continue
      else:
        assert False
    assert images_bool and len(tabs) == 6
  
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

  pass


class Test_The_Brook_2411_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get("https://www.meritagehomes.com/state/co/denver")
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