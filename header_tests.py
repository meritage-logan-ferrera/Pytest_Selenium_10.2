import page as page
import pytest
import time

class Test_Header_Element_Visibility:
  # Test that when the page is not scrolled, the translucent meritage logo is visible (as opposed to the opaque one that is displayed after scroll)
  def test_header_meritage_image_translucent(self, driver_settings):
    base_page = page.BasePage(self.driver)
    meritage_logo_container = base_page.header_get_element_meritage_image_container()
    meritage_logo_translucent = base_page.header_get_element_meritage_image_translucent()
    
    result = self.driver.execute_script("return arguments[0].complete && "+
    "typeof arguments[0].width != \"undefined\" && "+
    "arguments[0].width > 0 && " + "arguments[1].style.display != \"none\"", meritage_logo_translucent, meritage_logo_container)
    loaded = False
    loaded = bool(result)
    assert loaded, "result: " + str(result) + "loaded: " + str(type(loaded))
  
  # Clicking the search button pops of the search overlay
  def test_header_search_button(self, driver_settings):
    base_page = page.BasePage(self.driver)
    search_site_overlay = base_page.header_get_element_site_search_overlay()
    base_page.header_click_search_button()
    
    result = self.driver.execute_script("return arguments[0].className != \"hidden\"", search_site_overlay)
    assert bool(result)
  
  # Test the naviagtion of the elements in the very top bar on the site (ie My Account, Agents, etc)
  top_bar_elements = page.BasePage.TOP_BAR_ELEMENTS
  @pytest.mark.parametrize('element', top_bar_elements)
  def test_header_top_bar_info(self, element, driver_settings):
    base_page = page.BasePage(self.driver)
    base_page.header_click_top_bar_element(element)
    match element:
      case 'myaccount':
        assert "Meritage Account Registration – Create an Account | Meritage Homes" == self.driver.title
      case 'agents':
        assert "Agent Rocks Rewards Program | Meritage Homes" == self.driver.title
      case 'contact':
        assert "" == self.driver.title
      case _:
        assert False, str(self.driver.title)
  
  # Test the main navigation links in the header
  main_nav_elements = page.BasePage.MAIN_NAV_ELEMENTS
  @pytest.mark.parametrize('element', main_nav_elements)
  def test_header_main(self, element, driver_settings):  
    base_page = page.BasePage(self.driver)
    base_page.header_click_main_element(element)
    match element:
      case 'homes':
        assert 'Find a Home | Meritage Homes' == self.driver.title
      case 'why-meritage':
        assert 'Why Meritage? Energy Efficient Homes | Meritage Homes' == self.driver.title
      case 'buyer-resources':
        assert 'Buyer Resources & Tools For New Homeowners | Meritage Homes' == self.driver.title
      case 'my-home':
        assert 'My Meritage Portal' or 'Loading...' == self.driver.title
  
  # Test the navigaton links in the homes dropdown
  states = page.BasePage.STATES
  @pytest.mark.parametrize('state', states)
  def test_header_level2_homes(self, state, driver_settings):
    base_page = page.BasePage(self.driver)
    base_page.header_click_level2_element(page.BasePage.MAIN_NAV_ELEMENTS[0], state)
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
      case 'map':
        assert "Find a Home | Meritage Homes" == self.driver.title
      case _:
        assert False
  
  # Test the navigation links in the why-meritage dropdown
  why_meritage_nav_elements = page.BasePage.WHY_MERITAGE_NAV_ELEMENTS
  @pytest.mark.parametrize('why_meritage_nav_element', why_meritage_nav_elements)
  def test_header_level2_why_meritage(self, why_meritage_nav_element, driver_settings):
    base_page = page.BasePage(self.driver)
    base_page.header_click_level2_element(page.BasePage.MAIN_NAV_ELEMENTS[1], why_meritage_nav_element)
    match why_meritage_nav_element:
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
  
  # Test the navigation links in the buyer-resources dropdown
  buyer_resources_nav_elements = page.BasePage.BUYER_RESOURCES_NAV_ELEMENTS
  @pytest.mark.parametrize('buyer_resources_nav_element', buyer_resources_nav_elements)
  def test_header_level2_buyer_resources(self, buyer_resources_nav_element, driver_settings):
    base_page = page.BasePage(self.driver)
    base_page.header_click_level2_element(page.BasePage.MAIN_NAV_ELEMENTS[2], buyer_resources_nav_element)
    match buyer_resources_nav_element:
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

  ########################################################################
  # With the code below, this is how the tests run when called by a paramaterized pytest test function in of the test_* files:
  # ------------------------ CURRENT --------------------------
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
  # --------------------- IDEAL -------------------------------
  # This is how I want the test to run:
  # Homes test on Firefox, Chrome, Edge
  # then 
  # Why-meritage test on Firefox, Chrome, Edge
  # then
  # etc....
  #################################################################################
  


