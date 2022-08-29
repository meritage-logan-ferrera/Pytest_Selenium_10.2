from page_testimonials import TestimonialsPage
from page_base import BasePage
from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
import pytest

URL = 'https://www.meritagehomes.com/why-meritage/testimonials'

@pytest.mark.usefixtures("init__driver")
class BasicTest():
  pass

class Test_Testimonials_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get(URL)
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)