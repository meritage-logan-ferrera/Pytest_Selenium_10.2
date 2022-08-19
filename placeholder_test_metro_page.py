from email import header
# from lib2to3.pgen2 import driver
from wsgiref.handlers import BaseCGIHandler
from page import MainPage
import pytest
import header_tests
import footer_tests

# I want to be able to pass a URL into this file. For instance, when I make a test_metro_page file similar to this, I can just pass in the different metropage url's to all use the tests from the one file. But I cannot use __init__ in these classes... Need to find a solution. Pytest probably provides one but I am still looking...

@pytest.mark.usefixtures("init__driver")
class BasicTest(footer_tests.Test_Footer_Element_Visibility, header_tests.Test_Header_Element_Visibility):
  pass

class Test_Metro_Phoenix(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get('https://www.meritagehomes.com/state/az/phoenix')
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)
  
class Test_Metro_Tucson(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get('https://www.meritagehomes.com/state/az/tucson')
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)
  