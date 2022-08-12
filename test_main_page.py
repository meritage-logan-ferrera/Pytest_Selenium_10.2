from email import header
from page import MainPage
import pytest
import header_tests

URL = 'https://uat.meritagehomes.com/'

@pytest.mark.usefixtures("init__driver")
class BasicTest:
  pass

class Test_Main_Page(BasicTest):
  def driver_settings(self):
    self.driver.get(URL)
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)

  main_nav_elements = MainPage.MAIN_NAV_ELEMENTS
  @pytest.mark.parametrize('element', main_nav_elements)
  def test_header_main_navigation(self, element):
      self.driver_settings()
      header_tests.Test_Header_Navigation(self.driver).header_main(element)
  
  states = MainPage.STATES
  why_meritage_nav_elements = MainPage.WHY_MERITAGE_NAV_ELEMENTS
  level2_elements = states + why_meritage_nav_elements
  @pytest.mark.parametrize('level2_element', level2_elements)
  def test_header_level2_navigation(self, level2_element):
    self.driver_settings()
    header_tests.Test_Header_Navigation(self.driver).header_level2_homes(level2_element)