from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
from page_metro import MetroPage
from page_base import BasePage
import math
import pytest
import time


@pytest.mark.usefixtures("init__driver")
class BasicTest():
  def test_city_dropdown(self, driver_settings):
    metro_page = MetroPage(self.driver)
    city_dropdown = metro_page.get_element_city_dropdown()
    result = metro_page.button_is_clickable(city_dropdown)
    assert result
  
  def test_bedrooms_dropdown(self, driver_settings):
    metro_page = MetroPage(self.driver)
    bedrooms_dropdown = metro_page.get_element_bedrooms_dropdown()
    result = metro_page.button_is_clickable(bedrooms_dropdown)
    assert result
  
  def test_bathrooms_dropdown(self, driver_settings):
    metro_page = MetroPage(self.driver)
    bathrooms_dropdown = metro_page.get_element_bathrooms_dropdown()
    result = metro_page.button_is_clickable(bathrooms_dropdown)
    assert result
  
  def test_bedroom_slider(self, driver_settings):
    metro_page = MetroPage(self.driver)
    metro_page.slide_to_slide('bed')
    left_tag = metro_page.get_text_slider_1_left_tag()
    right_tag = metro_page.get_text_slider_1_right_tag()
    assert(
      '750' not in left_tag and
      '6,000' not in right_tag
    )
  
  pass

class Test_Denver_Page(BasicTest):
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