import page as page
import pytest

class Test_Header_Element_Visibility():
  def __init__(self, driver):
    self.driver = driver

  def meritage_image_translucent(self):
    base_page = page.BasePage(self.driver)
    meritage_logo_translucent = base_page.get_element_meritage_image_translucent()
    # Need to find a better script that does not just show that the width of the elemnt isgreater than 0 but that it is displayed currently. Scrolling on the website changes the image, I want this to assert false if the webstie is crolled down to the other meritage image. 
    result = self.driver.execute_script("return arguments[0].complete && "+
    "typeof arguments[0].width != \"undefined\" && "+
    "arguments[0].width > 0", meritage_logo_translucent)
    loaded = False
    loaded = bool(result)
    assert loaded, "result: " + str(result) + "loaded: " + str(type(loaded))

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
  def header_main(self, element):  
    base_page = page.BasePage(self.driver)
    base_page.click_header_main_element(element)
    match element:
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
#     metro_page.header_main_elements_click('homes')
#     assert 'Find a Home | Meritage Homes' == self.driver.title

#   def test_header_main_why_meritage(self):
#     #self.driver_settings()
#     metro_page = page.MetroPage(self.driver)
#     metro_page.header_main_elements_click('why-meritage')
#     assert 'Why Meritage? Energy Efficient Homes | Meritage Homes' == self.driver.title
  
#   def test_header_main_buyer_resources(self):
#     #self.driver_settings()
#     metro_page = page.MetroPage(self.driver)
#     metro_page.header_main_elements_click('buyer-resources')
#     assert 'Buyer Resources & Tools For New Homeowners | Meritage Homes' == self.driver.title

#   def test_header_main_my_home(self):
#     #self.driver_settings()
#     metro_page = page.MetroPage(self.driver)
#     metro_page.header_main_elements_click('my-home')
#     assert 'My Meritage Portal' or 'Loading...' == self.driver.title 

  def header_level2_homes(self, level2_element):
    base_page = page.BasePage(self.driver)
    base_page.click_header_level2_element(page.BasePage.MAIN_NAV_ELEMENTS[0], level2_element)
    match level2_element:
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
      case _:
        assert False
      
  def header_level2_why_meritage(self, level2_element):
    base_page = page.BasePage(self.driver)
    base_page.click_header_level2_element(page.BasePage.MAIN_NAV_ELEMENTS[1], level2_element)
    match level2_element:
      case 'why-meritage':
        assert 'Why Meritage? Energy Efficient Homes | Meritage Homes' == self.driver.title
      case 'testimonials':
        assert 'Meritage Homes Testimonials | Meritage Homes' == self.driver.title
      case 'reviews':
        assert 'Meritage Homes Reviews | Meritage Homes' == self.driver.title
      case 'energy-efficiency':
        assert 'Best Home Builders for Energy Efficient Homes | Meritage Homes' == self.driver.title, 'current title' + self.driver.title
      case 'how-we-design':
        assert 'How We Design | Meritage Homes' == self.driver.title
      case 'how-we-build':
        assert 'How We Build New Home Communities | Meritage Homes' == self.driver.title
      case 'awards':
        assert 'Meritage Homes Awards and Accolades | Meritage Homes' == self.driver.title
      case _:
        assert False
  
  def header_level2_buyer_resources(self, level2_element):
    base_page = page.BasePage(self.driver)
    base_page.click_header_level2_element(page.BasePage.MAIN_NAV_ELEMENTS[2],level2_element)
    match level2_element:
      case 'buyer-resources':
        assert 'Buyer Resources & Tools For New Homeowners | Meritage Homes' == self.driver.title
      case 'homebuying':
        assert 'First-Time Homebuying Information & Guides | Meritage Homes' == self.driver.title
      case 'home-financing':
        assert 'New Home Financing Guides & Resources | Meritage Homes' == self.driver.title
      case 'energy-efficiency':
        assert 'Energy Efficiency & Green Energy Resources | Meritage Homes' == self.driver.title
      case 'home-design':
        assert 'New Home Design Inspiration | Meritage Homes' == self.driver.title
      case _:
        assert False


