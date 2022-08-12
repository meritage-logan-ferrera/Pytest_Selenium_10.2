from email import header
import page as page
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

  metro = header_tests.metro
  @pytest.mark.parametrize('item', metro)
  def test_header_main_navigation(self, item):
      self.driver_settings()
      header_tests.Test_Header_Navigation(self.driver).header_main(item)
  
  states = header_tests.states
  @pytest.mark.parametrize('state', states)
  def test_header_level2_navigation(self, state):
    self.driver_settings()
    header_tests.Test_Header_Navigation(self.driver).header_level2_homes(state)
      