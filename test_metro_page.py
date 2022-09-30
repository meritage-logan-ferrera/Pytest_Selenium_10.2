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
  
  def test_slider_1(self, driver_settings):
    metro_page = MetroPage(self.driver)
    metro_page.close_cookies()
    metro_page.slide_to_slide('bed')
    left_tag = metro_page.get_text_slider_1_left_tag()
    right_tag = metro_page.get_text_slider_1_right_tag()
    assert(
      '750' not in left_tag and
      '6,000' not in right_tag
    )
  
  def test_slider_2(self, driver_settings):
    metro_page = MetroPage(self.driver)
    metro_page.close_cookies()
    metro_page.slide_to_slide('bath')
    left_tag = metro_page.get_text_slider_2_left_tag()
    right_tag = metro_page.get_text_slider_2_right_tag()
    assert(
      '750' not in left_tag and
      '6,000' not in right_tag
    )
  
  def test_submit(self, driver_settings):
    metro_page = MetroPage(self.driver)
    submit_button = metro_page.get_element_top_bar_submit_button()
    result = metro_page.button_is_clickable(submit_button)
    assert result
  
  def test_reset(self, driver_settings):
    metro_page = MetroPage(self.driver)
    reset_button = metro_page.get_element_top_bar_reset()
    result = metro_page.button_is_clickable(reset_button)
    assert result
  
  def test_zoom_in(self, driver_settings):
    metro_page = MetroPage(self.driver)
    metro_page.close_cookies()
    metro_page.get_element_zoom_in()
    metro_page.click_element_zoom_in()
  
  def test_new_homes_title(self, driver_settings):
    metro_page = MetroPage(self.driver)
    header = metro_page.get_text_title()
    assert 'New Homes' in header
  
  def test_title_link(self, driver_settings):
    metro_page = MetroPage(self.driver)
    text = metro_page.get_text_communities_and_qmi()
    assert (
      'Communities' in text and
      'Quick Move-In Homes' in text
    )
  
  def test_communities_appear(self, driver_settings):
    metro_page = MetroPage(self.driver)
    communities_elements = metro_page.get_elements_communities()
    assert len(communities_elements) > 0
  
  def test_communities_images(self, driver_settings):
    metro_page = MetroPage(self.driver)
    communities_elements = metro_page.get_elements_communities()
    all_images_present = False
    for i in range(len(communities_elements)):
      image = metro_page.get_element_community_image(i)
      result = metro_page.javascript_image(image)
      if result:
        all_images_present = True
      else:
        assert False
    assert all_images_present

  def test_communities_overlay(self, driver_settings):
    metro_page = MetroPage(self.driver)
    communities_elements = metro_page.get_elements_communities()
    all_overlays_present = False
    for i in range(len(communities_elements)):
      overlay_text = metro_page.get_text_community_snipe_overlay(i)
      if overlay_text != '':
        all_overlays_present = True
      else:
        assert False
    assert all_overlays_present

  @pytest.mark.zoom
  def test_click_community(self, driver_settings):
    metro_page = MetroPage(self.driver)
    metro_page.close_cookies()
    name = metro_page.get_text_community_name(0)
    metro_page.click_element_community_name(0)
    assert name in self.driver.title

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