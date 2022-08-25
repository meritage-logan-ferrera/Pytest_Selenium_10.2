from page_state import StatePage
from page_base import BasePage
from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
import pytest

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
  @pytest.mark.state
  def test_aside_sub_header(self, driver_settings):
    state_page = StatePage(self.driver)
    sub_header = state_page.get_text_aside_sub_header()
    assert 'Find a community to call home' in sub_header

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