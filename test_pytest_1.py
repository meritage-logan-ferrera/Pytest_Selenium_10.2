import page as page
import pytest

@pytest.mark.usefixtures("init__driver")
class BasicTest:
    pass

class Test_URL_Chrome(BasicTest):
  def test_header_arizona(self):
    self.driver.get('https://www.meritagehomes.com/')
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)
    home_page = page.MainPage(self.driver)
    home_page.click_state("az")
    title = "Arizona"
    assert title == self.driver.title
