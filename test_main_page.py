from page import MainPage
import pytest
import header_tests
import footer_tests

URL = 'https://www.meritagehomes.com/'

@pytest.mark.usefixtures("init__driver")
class BasicTest(footer_tests.Test_Footer_Element_Visibility, header_tests.Test_Header_Element_Visibility):
  pass

class Test_Main_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get(URL)
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)
  
  # Test that the Meritage video is playing

  