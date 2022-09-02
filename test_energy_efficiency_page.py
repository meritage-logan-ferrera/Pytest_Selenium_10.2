from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
from page_energy_efficiency import EnergyEfficiencyPage
from page_base import BasePage
import pytest
import time

URL = 'https://www.meritagehomes.com/why-meritage/energy-efficiency'

@pytest.mark.usefixtures("init__driver")
class BasicTest():
  pass

class Test_Energy_Efficiency_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get(URL)
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)
  
  # Test that youtube overlay pop up after clicking play button
  def test_overlay_on_play_button_click(self, driver_settings):
    energy_page = EnergyEfficiencyPage(self.driver)
    energy_page.click_element_play_button()
    youtube_overlay = energy_page.get_element_youtube_overlay()
    result = self.driver.execute_script("return arguments[0].style.display != 'none'", youtube_overlay)
    assert result
  
  # Test that the tabs have the correct image and header
  # Same as the same code form why_meritage
  @pytest.mark.parametrize('drop_down', ['1', '2', '3', '4'])
  def test_section_1_tabs(self, drop_down, driver_settings):
    energy_page = EnergyEfficiencyPage(self.driver)
    image = energy_page.get_element_section_1_drop_down_container_image(drop_down)
    header = energy_page.get_text_section_1_drop_down_container_header(drop_down)
    result = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", image)
    header_bool = False
    match drop_down:
      case '1':
        if "Keeping the Peace" in header:
          header_bool = True
      case '2':
        if "Buggin" in header:
          header_bool = True
      case '3':
        if "Playing It Cool" in header:
          header_bool = True
      case '4':
        if "Clearing the Air" in header:
          header_bool = True
      
    assert header_bool and result
  
# Test that the drop down containers open the correct tabs when clicked and that all the information within the respective tabs are correct.
# SIMILAR to the same method in test_why_meritage_page.py
# It is only used test in all the website so I am not going to make anotehr shared function for these.
  @pytest.mark.energy
  @pytest.mark.parametrize('tab', ['1', '2', '3', '4'])
  def test_section_1_tab_everything(self, tab, driver_settings):
    energy_page = EnergyEfficiencyPage(self.driver)
    energy_page.close_cookies()
    energy_page.click_element_section_1_drop_down(tab)
    current_tab = energy_page.get_element_section_1_responsive_tab(tab)
    tab_header = energy_page.get_text_section_1_responsive_tab_header(tab)
    tab_body = energy_page.get_text_section_1_responsive_tab_body(tab)
    tab_image = energy_page.get_element_section_1_responsive_tab_image(tab)
    
    # SUB TEST 1 for correct tab displayed on click:
    correct_tab =self.driver.execute_script("return arguments[0].classList.contains(\"is-active\")", current_tab) 
    
    # SUB TEST 2 for image:
    correct_image = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", tab_image)
    
    tab_header_bool = False
    tab_body_bool = False
    button_nav_bool = False
    
    # SUB TESTS 3 & 4 & 5 for header, body, and button nav in responsive tab:
    match tab:
      case '1':
        if "Noise-Reducing Spray Foam" in tab_header:
          tab_header_bool = True
        if "cut down outside noise" in tab_body:
          tab_body_bool = True
        energy_page.click_element_section_1_responsive_tab_button(tab)
        if "Noise-Reduction" == self.driver.title:
          button_nav_bool = True
      case '2':
        if "Pest-Reducing Barrier" in tab_header:
          tab_header_bool = True
        if "reduce space for pests" in tab_body:
          tab_body_bool = True
        energy_page.click_element_section_1_responsive_tab_button(tab)
        if "Pest Reduction" == self.driver.title:
          button_nav_bool = True
      case '3':
        if "Climate-Sealed Home" in tab_header:
          tab_header_bool = True
        if "keep your home cool" in tab_body:
          tab_body_bool = True
        energy_page.click_element_section_1_responsive_tab_button(tab)
        if "Temperature Regulation" == self.driver.title:
          button_nav_bool = True
      case '4':
        if "Health-Promoting Barrier" in tab_header:
          tab_header_bool = True
        if "improve indoor air quality" in tab_body:
          tab_body_bool = True
        energy_page.click_element_section_1_responsive_tab_button(tab)
        if "Air Quality Improvement" == self.driver.title:
          button_nav_bool = True    
    
    assert correct_tab and tab_header_bool and tab_body_bool and correct_image and button_nav_bool

  # Test whether correct header appears in article 1
  def test_article_1_header(self):
    energy_page = EnergyEfficiencyPage(self.driver)
    header = energy_page.get_text_article_1_header()
    assert 'Cleaner Air' in header

  # Test whether correct body appears in article 1
  def test_article_1_body(self):
    energy_page = EnergyEfficiencyPage(self.driver)
    body = energy_page.get_text_article_1_body()
    assert 'leading the way in health-concious homebuilding. In September 2020' in body
  
  # Test whether correct image appears in article 1
  def test_article_1_image(self):
    energy_page = EnergyEfficiencyPage(self.driver)
    image = energy_page.get_element_article_1_image()
    result = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", image)
    assert result