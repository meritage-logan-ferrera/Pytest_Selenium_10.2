import page_android_base as page
import pytest

@pytest.mark.usefixtures("driver_android_init")
class BasicTest:
    pass

class Test_URL_Android(BasicTest):
  def test_header_arizona(self):
    self.driver.get('https://www.meritagehomes.com/')
    home_page_android = page.MainPageAndroid(self.driver)
    home_page_android.click_state()
    title = "Arizona"
    assert title == self.driver.title
