from page_state import StatePage
from page_base import BasePage
from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
import pytest
import time

@pytest.mark.usefixtures("init__driver")
class BasicTest():
  # How the code works for this page: 
  # As an example I have Test_Arizona_Page and Test_California_Page. These two classes create their own driver and return the name of the state asscoiated with them. These two classes also inherit all the tests from BasicTest. That means they can both run the test_breadcrumbs_header test. So, the driver associated with the Test_Arizona_page class calls test_breadcrumbs_header. Inside this test it needs to assert that 'Arizona' == header. But when the driver associated with the Test_California_Page calls the same test it needs to assert that 'California' == header. This will be repeated across all the Test_Page classes for each state. The switch statement used to do this will also be repeated across most of the tests, thus, this function.
  def cases(self, AZ, CA, CO, FL, GA, NC, SC, TN, TX, assert_compare, driver_settings):
    match driver_settings:
      case 'Arizona':
        assert AZ in assert_compare
      case 'California':
        assert CA in assert_compare
      case 'Colorado':
        assert CO in assert_compare
      case 'Florida':
        assert FL in assert_compare
      case 'Georgia':
        assert GA in assert_compare
      case 'North Carolina':
        assert NC in assert_compare
      case 'South Carolina':
        assert SC in assert_compare
      case 'Tennessee':
        assert TN in assert_compare
      case 'Texas':
        assert TX in assert_compare
      case _:
        assert False
  
  # Used
  def cases_metro(self, AZ, CA, CO, FL, GA, NC, SC, TN, TX, num, assert_compare, driver_settings):
    idx = num - 1
    match driver_settings:
      case 'Arizona':
        if AZ[idx] in assert_compare:
          return True
      case 'California':
        if CA[idx] in assert_compare:
          return True
      case 'Colorado':
        if CO[idx] in assert_compare:
          return True
      case 'Florida':
        if FL[idx] in assert_compare:
          return True
      case 'Georgia':
        if GA[idx] in assert_compare:
          return True
      case 'North Carolina':
        if NC[idx] in assert_compare:
          return True
      case 'South Carolina':
        if SC[idx] in assert_compare:
          return True
      case 'Tennessee':
        if TN[idx] in assert_compare:
          return True
      case 'Texas':
        if TX[idx] in assert_compare:
          return True
      case _:
        return False

  # Test that the small house icon appears in the state's header
  def test_breadcrumbs_house(self, driver_settings):
    state_page = StatePage(self.driver)
    house_image = state_page.get_element_breadcrumbs_house()
    result = self.driver.execute_script("return arguments[0].clientWidth > 0", house_image)
    assert result
  
  # Test that the state's name appears in the state's header
  def test_breadcrumbs_header(self, driver_settings):
    current_state_being_tested = driver_settings
    state_page = StatePage(self.driver)
    header = state_page.get_text_breadcrumbs_header()
    self.cases('Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'North Carolina', 'South Carolina', 'Tennessee', 'Texas', header, current_state_being_tested)
  
  # Test that the correct state name appers in the main header
  def test_state_header(self, driver_settings):
    current_state_being_tested = driver_settings
    state_page = StatePage(self.driver)
    header = state_page.get_text_state_header()
    self.cases('Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'North Carolina', 'South Carolina', 'Tennessee', 'Texas', header, current_state_being_tested)

  # Test that the correct sub-header is displayed for the state
  def test_state_sub_header(self, driver_settings):
    current_state_being_tested = driver_settings
    state_page = StatePage(self.driver)
    sub_header = state_page.get_text_state_sub_header()
    self.cases(
      'Unbelievable sunsets', 
      'Come for the classic beach towns',
      'Between the vibrant, family',
      'The Sunshine State',
      'Big business, ample educational',
      'Enjoy diverse landscapes',
      'The lively culture',
      'Enjoy the rhythm of life',
      'Tex-Mex cuisine',
      sub_header,
      current_state_being_tested
    )
  
  # Test that the correct header is displayed above the scroll down arrow
  def test_arrow_text(self, driver_settings):
    state_page = StatePage(self.driver)
    header = state_page.get_text_scroll_down_arrow()
    assert 'View all plans and homes' in header
  
  # Test that clicking the down arrow scrolls the page
  def test_arrow_scroll(self, driver_settings):
    state_page = StatePage(self.driver)
    html = state_page.get_html()
    state_page.close_cookies()
    state_page.click_element_scroll_down_arrow()
    result = self.driver.execute_script("return arguments[0].scrollTop > 100", html)
    assert result

  # Test that the correct header is displayed in aside
  def test_aside_header(self, driver_settings):
    current_state_being_tested = driver_settings
    state_page = StatePage(self.driver)
    header = state_page.get_text_aside_header()
    see = 'See where we build in '
    self.cases(see + 'Arizona', see + 'California', see + 'Colorado', see + 'Florida', see + 'Georgia', see + 'North Carolina', see + 'South Carolina' , see + 'Tennessee', see + 'Texas', header, current_state_being_tested)

  # Test that the correct sub-header is displayed in aside
  def test_aside_sub_header(self, driver_settings):
    state_page = StatePage(self.driver)
    sub_header = state_page.get_text_aside_sub_header()
    assert 'Find a community to call home' in sub_header

  # # Test the metro cotnainers
  # def test_metro_container_1(self, driver_settings):
  #   state_page = StatePage(self.driver)
  #   current_state = driver_settings
  #   metro_container = state_page.get_element_metro_div('1')
  #   metro_header = state_page.get_text_metro_header('1')
  #   metro_cities_build = state_page.get_text_metro_cities_build('1')
  #   metro_city_areas = state_page.get_text_metro_city_areas('1')
  #   metro_stats = state_page.get_text_metro_stats('1')
    


  # Test that the correct metro page sections appear on the state page.
  # This is bad code. It will work until I can figure out how to change the paramaterize accept a dynamic list as an argument which changes based on what state the current driver is on.
  @pytest.mark.state
  @pytest.mark.parametrize('div', ['1', '2', '3', '4']) 
  def test_metro_container(self, div, driver_settings):
    current_state_being_tested = driver_settings
    state_page = StatePage(self.driver)
    match driver_settings:
      case 'Arizona':
        if int(div) > 2:
          pytest.skip('Arizona only has 2 metro pages')
      case 'California':
        if int(div) > 3:
          pytest.skip('California only has 3 metro pages')
      case 'Colorado':
        if int(div) > 1:
          pytest.skip('Colorado only has 1 metro page')
      case 'Florida':
        if int(div) > 3:
          pytest.skip('Florida only has 3 metro pages')
      case 'Georgia':
        if int(div) > 1:
          pytest.skip('Georgia only has 1 metro page')
      case 'North Carolina':
        if int(div) > 2:
          pytest.skip('North Carolina only has 2 metro pages')
      case 'South Carolina':
        if int(div) > 3:
          pytest.skip('South Carolina only has 3 metro pages')
      case 'Tennessee':
        if int(div) > 1:
          pytest.skip('Tennessee only has 1 metro page')
      case 'Texas':
        if int(div) > 4:
          pytest.skip('Texas only has 4 metro pages')
      
    metro_div = state_page.get_text_metro_header(div)
    header_correct = self.cases_metro(
      ['Phoenix', 'Tucson'], 
      ['Bay Area', 'Sacramento', 'Southern'], 
      ['Denver'], 
      ['Orlando', 'Tampa', 'South Florida'], 
      ['Atlanta'], 
      ['Charlotte', 'Raleigh'], 
      ['Greenville', 'York County', 'Myrtle Beach'], 
      ['Nashville'], 
      ['Austin', 'Dallas', 'Houston', 'San Antonio'], 
      int(div),
      metro_div,
      current_state_being_tested
    )
  
    metro_cities_build = state_page.get_text_metro_cities_build(div)
    cities_build_correct = self.cases_metro(
      ['Avondale, Buckeye, Casa Grande', 'Marana, Maricopa'], 
      ['Dixon, Hayward, Hollister', 'Elk Grove, Lincoln', 'Huntington Beach, Lake Elsinore, Menifee'], 
      ['Arvada, Aurora, Brighton, Broomfield'], 
      ['Clermont, Davenport, Daytona Beach', 'Auburndale, Brandon, Lakewood Ranch', 'Babcock Ranch, Jensen Beach'], 
      ['Braselton, Canton, Dawsonville'], 
      ['Albemarle, Belmont, Charlotte', 'Cary, Clayton'], 
      ['Fountain Inn, Greenville', 'Fort Mill, York', 'Little River, Myrtle Beach'], 
      ['Cane Ridge, Columbia, Gallatin'], 
      ['Austin, Buda, Dripping Springs', 'Denton, Forney, Fort Worth', 'Baytown, Conroe', 'Boerne, Cibolo'], 
      int(div),
      metro_cities_build,
      current_state_being_tested
    )

    metro_city_areas = state_page.get_text_metro_city_areas(div)
    city_areas_correct = self.cases_metro(
      ['East Valley, West Valley', 'North Tucson, Oro Valley, Tucson'], 
      ['Bay Area, Northern California', 'Northern California, Sacramento', 'Orange County, SoCal'], 
      ['Denver Metro Area'], 
      ['Celebration, Central Florida, Championsgate', 'Auburndale, Bradenton, Crystal Springs', 'Babcock Ranch, Cape Coral'], 
      [''],  # somone forgot to fill this in??
      ['Fort Mill, Monroe', ''], # not filled 
      ['Downtown, Foothills', 'Fort Mill', 'Conway, Little River'], 
      [''],  # None
      ['Dripping Springs', 'Dallas', 'Northwest Houston, Southeast Houston', 'Cibolo, New Braunfels'], 
      int(div),
      metro_city_areas,
      current_state_being_tested
    )

    metro_stats = state_page.get_text_metro_stats(div)
    stats_correct = False
    if (
      'Communities' in metro_stats and 
      'Floorplans' in metro_stats and 
      'Quick Move-in Homes' in metro_stats
    ):  
      stats_correct = True

    testimonial_div = div

    if current_state_being_tested == "Florida": # South Florida has no quote block
      testimonial_div = int(div) - 1
    
    if current_state_being_tested == "South Carolina": # SC missing quot elbock from york county and myrtle beach
      testimonial_div = int(div)-2

    testimonial_header = state_page.get_text_testimonial_header(testimonial_div)
    testimonial_header_correct = self.cases_metro(
      ['Phoenix', 'Tucson'], 
      ['Bay Area', 'Sacramento', 'Southern'], 
      ['Denver'], 
      ['Orlando', 'Tampa', 'South Florida'], 
      ['Atlanta'], 
      ['Charlotte', 'Raleigh'], 
      ['Greenville'], 
      ['Nashville'], 
      ['Austin', 'Dallas', 'Houston', 'San Antonio'], 
      int(testimonial_div),
      testimonial_header,
      current_state_being_tested
    )

    testimonial_quote = state_page.get_text_testimonial_quote(testimonial_div)
    testimonial_quote_correct = self.cases_metro(
      ['very pleased with our low', 'We loved the energy-efficient'], 
      ['Every day is a comfortable', 'The home has many wonderful', 'The home is everything'], 
      ['The temperature is comfortable in all rooms'], 
      ['Our new home', 'We simply could not be happier'], 
      ['My utility bills are the lowest'], 
      ['not only walked us through', 'I love the location'], 
      ['My experience with Meritage'], 
      ['were knowledgeable and more importantly'], 
      ['Our overall experience', 'Working with Meritage', 'have been loving', 'The home lived up to how'], 
      int(testimonial_div),
      testimonial_quote,
      current_state_being_tested
    )
  
    testimonial_attribution = state_page.get_text_testimonial_attribution(testimonial_div)
    testimonial_attribution_correct = self.cases_metro(
      ['Cari G.', 'Rita & Glen S.'], 
      ['Catherine & Alex H.', 'Alan & Kimberly C.', 'John D.'], 
      ['Brooke W.'], 
      ['Allison D.', 'Earl & Ellen C.'], 
      ['Min C.'], 
      ['Himanshu & Jigna D.', 'Theodora M.'], 
      ['Flonsel A.'], 
      ['Kenneth P.'], 
      ['Tyler L.', 'Michelle & Lee C.', 'Lucy B.', 'Suwaid K.'], 
      int(testimonial_div),
      testimonial_attribution,
      current_state_being_tested
    )
    
    assert (
      header_correct and
      cities_build_correct and
      city_areas_correct and
      stats_correct and
      testimonial_header_correct and
      testimonial_quote_correct and
      testimonial_attribution_correct
    )
  # These state pages are not fully transfered to the new site yet...

  def test_why_meritage_header(self, driver_settings):
    state_page = StatePage(self.driver)
    header = state_page.get_text_why_meritage_header()
    assert 'Why Meritage Homes' in header
  
  def test_why_meritage_body(self, driver_settings):
    state_page = StatePage(self.driver)
    body = state_page.get_text_why_meritage_body()
    assert 'Why Meritage Homes' in body
  
  def test_why_meritage_image(self, driver_settings):
    state_page = StatePage(self.driver)
    image = state_page.get_element_why_meritage_image()
    result = state_page.javascript_image(image)
    assert result
  
  def test_why_meritage_button(self, driver_settings):
    state_page = StatePage(self.driver)
    state_page.close_cookies()
    state_page.click_element_why_meritage_button()
    assert 'Why Meritage? Energy Efficient Homes | Meritage Homes' == self.driver.title
  
  def test_aside_know_florida_header(self, driver_settings):
    state_page = StatePage(self.driver)
    header = state_page.get_text_aside_know_florida_header()
    assert 'Ready to make your move' in header
  
  def test_aside_know_florida_body(self, driver_settings):
    state_page = StatePage(self.driver)
    body = state_page.get_text_aside_know_florida_body()
    assert 'Whether you need a little help' in body
  
  def test_aside_know_florida_button_1(self, driver_settings):
    state_page = StatePage(self.driver)
    state_page.close_cookies()
    state_page.click_element_aside_know_florida_button_1()
    assert 'Find a Home | Meritage Homes' == self.driver.title

  def test_aside_know_florida_button_2(self, driver_settings):
    state_page = StatePage(self.driver)
    state_page.close_cookies()
    state_page.click_element_aside_know_florida_button_2()
    assert 'Tour A Meritage Home' == self.driver.title
  
  def test_aside_know_florida_number(self, driver_settings):
    state_page = StatePage(self.driver)
    time.sleep(4)
    number = state_page.get_text_aside_know_florida_number()
    assert 'or call' in number
    
  

class Test_Arizona_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get("https://www.meritagehomes.com/state/az")
    self.driver.set_window_position(0,0)
    return "Arizona"
    
  
class Test_California_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get("https://www.meritagehomes.com/state/ca")
    self.driver.set_window_position(0,0)
    return "California"
  

class Test_Colorado_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get("https://www.meritagehomes.com/state/co")
    self.driver.set_window_position(0,0)
    return "Colorado"

class Test_Florida_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get("https://www.meritagehomes.com/state/fl")
    self.driver.set_window_position(0,0)
    return "Florida"

class Test_Georgia_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get("https://www.meritagehomes.com/state/ga")
    self.driver.set_window_position(0,0)
    return "Georgia"
  
class Test_North_Carolina_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get("https://www.meritagehomes.com/state/nc")
    self.driver.set_window_position(0,0)
    return "North Carolina"

class Test_South_Carolina_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get("https://www.meritagehomes.com/state/sc")
    self.driver.set_window_position(0,0)
    return "South Carolina"

class Test_Tennessee_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get("https://www.meritagehomes.com/state/tn")
    self.driver.set_window_position(0,0)
    return "Tennessee"
 
class Test_Texas_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get("https://www.meritagehomes.com/state/tx")
    self.driver.set_window_position(0,0)
    return "Texas"