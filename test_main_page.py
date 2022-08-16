from email import header
from page import MainPage
import pytest
import header_tests

URL = 'https://www.meritagehomes.com/'

@pytest.mark.usefixtures("init__driver")
class BasicTest:
  pass

class Test_Main_Page(BasicTest):
  def driver_settings(self):
    self.driver.get(URL)
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)
  
  # For all the below tests with test_header_* see header_tests for documentation on what they do...
  def test_header_meritage_logo_translucent(self):
    self.driver_settings()
    header_tests.Test_Header_Element_Visibility(self.driver).meritage_image_translucent()

  def test_header_search_button(self):
    self.driver_settings()
    header_tests.Test_Header_Element_Visibility(self.driver).search_button()
  
  top_bar_elements = MainPage.TOP_BAR_ELEMENTS
  @pytest.mark.parametrize('element', top_bar_elements)
  def test_header_top_bar_navigation(self, element):
    self.driver_settings()
    header_tests.Test_Header_Navigation(self.driver).header_top_bar_info(element)

  main_nav_elements = MainPage.MAIN_NAV_ELEMENTS
  @pytest.mark.parametrize('element', main_nav_elements)
  def test_header_main_navigation(self, element):
    self.driver_settings()
    header_tests.Test_Header_Navigation(self.driver).header_main(element)
  
  # With how pytest is interacting with the grid right now, it is better to have less tests use the paramaterize feature so that they can run in parellel more often. See the issue in header_tests.py. So I am trying to balance the amount of unique tests and the cleaness/organization of the code. Thats why these below tests are separate, makes testing run faster.
  states = MainPage.STATES
  @pytest.mark.parametrize('state', states)
  def test_header_level2_homes_navigation(self, state):
    self.driver_settings()
    header_tests.Test_Header_Navigation(self.driver).header_level2_homes(state)

  
  why_meritage_nav_elements = MainPage.WHY_MERITAGE_NAV_ELEMENTS
  @pytest.mark.blogan
  @pytest.mark.parametrize('why_meritage_nav_element', why_meritage_nav_elements)
  def test_header_level2_why_meritage_navigation(self, why_meritage_nav_element):
    self.driver_settings()
    header_tests.Test_Header_Navigation(self.driver).header_level2_why_meritage(why_meritage_nav_element)
  
  buyer_resources_nav_elements = MainPage.BUYER_RESOURCES_NAV_ELEMENTS
  @pytest.mark.parametrize('buyer_resources_nav_element', buyer_resources_nav_elements)
  def test_header_level2_buyer_resources_navigation(self, buyer_resources_nav_element):
    self.driver_settings()
    header_tests.Test_Header_Navigation(self.driver).header_level2_buyer_resources(buyer_resources_nav_element)
