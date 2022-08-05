import pytest
import page as page
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures("driver_firefox_init")
class BasicTest:
    pass

class Test_URL_Firefox(BasicTest):
  def test_header_arizona(self):
    self.driver.get('https://www.meritagehomes.com/')
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)
    home_page = page.MainPage(self.driver)
    home_page.click_state("az")
    title = "Arizona"
    assert title == self.driver.title
