import page as page
import pytest

@pytest.mark.usefixtures("init__driver")
class BasicTest:
    pass

class Test_Header_Main(BasicTest):
  def driver_settings(self):
    self.driver.get('https://uat.meritagehomes.com/state/ca/bay-area')
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)
  #metro = ('homes', 'why-meritage', 'buyer-resources', 'my-home')
  #@pytest.mark.parametrize('item', metro)
  def test_header_main_homes(self): # I need to find a way to condense these next 4 yests into one. I tried using @pytest.paramaterize but it causes the selenium tests to run all the firefox tests first, then all the chrome, etc. Makes it so tests cannot run in parallel.
    self.driver_settings()
    metro_page = page.MetroPage(self.driver)
    metro_page.header_main_items_click('homes')
    # match item:
    #   case 'homes':
    assert 'Find a Home | Meritage Homes' == self.driver.title
    #   case 'why-meritage':
    #     assert 'Why Meritage? Energy Efficient Homes | Meritage Homes' == self.driver.title
    #   case 'buyer-resources':
    #     assert 'Buyer Resources & Tools For New Homeowners | Meritage Homes' == self.driver.title
    #   case 'my-home':
    #     assert 'My Meritage Portal' == self.driver.title

  def test_header_main_why_meritage(self):
    self.driver_settings()
    metro_page = page.MetroPage(self.driver)
    metro_page.header_main_items_click('why-meritage')
    assert 'Why Meritage? Energy Efficient Homes | Meritage Homes' == self.driver.title
  
  def test_header_main_buyer_resources(self):
    self.driver_settings()
    metro_page = page.MetroPage(self.driver)
    metro_page.header_main_items_click('buyer-resources')

  def test_header_main_my_home(self):
    self.driver_settings()
    metro_page = page.MetroPage(self.driver)
    metro_page.header_main_items_click('my-home')