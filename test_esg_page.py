from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
from page_meritage_cares import MeritageCaresPage
from page_esg import ESGPage
import math
import pytest
import time

URL = 'https://www.meritagehomes.com/esg'

@pytest.mark.usefixtures("init__driver")
class BasicTest():
  pass

class Test_ESG_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get(URL)
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)