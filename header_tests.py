import page as page
import pytest

metro = ('homes', 'why-meritage', 'buyer-resources', 'my-home')
states = ('az', 'ca', 'co', 'fl', 'ga', 'nc', 'sc', 'tn', 'tx')

class Test_Header_Element_Visibility():
  def __init__(self, driver):
    self.driver = driver


class Test_Header_Navigation():
  def __init__(self, driver):
    self.driver = driver
  
  # With the code below, this is how the tests run:
  # -------------------CURRENT (when code below is uncommented)--------------------
  # Homes, Why-meritage,buyer-resources, my-home tests on Firefox
  # then
  # Homes, Why-meritage, etc.. on Chrome
  # then
  # Homes, WHy-meritage, etc. on Edge
  # This queues three firefox sessions and fills up selenium grid so that no edge 
  # and chrome tests can run in parallel. I want the session queue to always (or 
  # atleast 95% of the time) to  
  # be filled with an Edge tet, then a chrome test, 
  # then a Firefox test to give us the greatest amount of parallel testing.
  # ----------------------NEEDED (working for a fix)-------------------------------
  # This is how I want the test to run:
  # Homes test on Firefox, Chrome, Edge
  # then 
  # Why-meritage test on Firefox, Chrome, Edge
  # then
  # etc....
  # For now it has taken me too much time to think of a workable and clean solution so instead I am taking the easy and lazy route and copy-pasting
  #################################################################################
  def header_main(self, item):  
    metro_page = page.MetroPage(self.driver)
    metro_page.click_header_main_item(item)
    match item:
      case 'homes':
        assert 'Find a Home | Meritage Homes' == self.driver.title
      case 'why-meritage':
        assert 'Why Meritage? Energy Efficient Homes | Meritage Homes' == self.driver.title
      case 'buyer-resources':
        assert 'Buyer Resources & Tools For New Homeowners | Meritage Homes' == self.driver.title
      case 'my-home':
        assert 'My Meritage Portal' or 'Loading...' == self.driver.title
 ################################################################################
#   def test_header_main_homes(self):
#     #self.driver_settings()
#     metro_page = page.MetroPage(self.driver)
#     metro_page.header_main_items_click('homes')
#     assert 'Find a Home | Meritage Homes' == self.driver.title

#   def test_header_main_why_meritage(self):
#     #self.driver_settings()
#     metro_page = page.MetroPage(self.driver)
#     metro_page.header_main_items_click('why-meritage')
#     assert 'Why Meritage? Energy Efficient Homes | Meritage Homes' == self.driver.title
  
#   def test_header_main_buyer_resources(self):
#     #self.driver_settings()
#     metro_page = page.MetroPage(self.driver)
#     metro_page.header_main_items_click('buyer-resources')
#     assert 'Buyer Resources & Tools For New Homeowners | Meritage Homes' == self.driver.title

#   def test_header_main_my_home(self):
#     #self.driver_settings()
#     metro_page = page.MetroPage(self.driver)
#     metro_page.header_main_items_click('my-home')
#     assert 'My Meritage Portal' or 'Loading...' == self.driver.title 

  def header_level2_homes(self, state):
    metro_page = page.MetroPage(self.driver)
    metro_page.click_header_level2_homes_item(state)
    match state:
      case 'az':
        assert 'Arizona' == self.driver.title
      case 'ca':
        assert 'California' == self.driver.title
      case 'co':
        assert 'Colorado' == self.driver.title
      case 'fl':
        assert 'Florida' == self.driver.title
      case 'ga':
        assert 'Georgia' == self.driver.title
      case 'nc':
        assert 'North Carolina' == self.driver.title
      case 'sc':
        assert 'South Carolina' == self.driver.title
      case 'tn':
        assert 'Tennessee' == self.driver.title
      case 'tx':
        assert 'Texas' == self.driver.title

