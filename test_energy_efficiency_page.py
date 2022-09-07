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
    # self.driver.set_window_position(0,0)
    # self.driver.set_window_size(1920,1080)
  
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
  def test_article_1_header(self, driver_settings):
    energy_page = EnergyEfficiencyPage(self.driver)
    header = energy_page.get_text_article_1_header()
    assert 'Cleaner Air' in header

  # Test whether correct body appears in article 1
  def test_article_1_body(self, driver_settings):
    energy_page = EnergyEfficiencyPage(self.driver)
    body = energy_page.get_text_article_1_body()
    assert 'leading the way in health-concious homebuilding. In September 2020' in body
  
  # Test whether correct image appears in article 1
  def test_article_1_image(self, driver_settings):
    energy_page = EnergyEfficiencyPage(self.driver)
    image = energy_page.get_element_article_1_image()
    result = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", image)
    assert result
  
  # Test whether the correct headers, subheaders, and body appear in the donut slides
  @pytest.mark.parametrize('slide', ['0', '1', '2', '3'])
  def test_donut_slides_header(self, slide, driver_settings):
    energy_page = EnergyEfficiencyPage(self.driver)
    energy_page.close_cookies()
    for i in range(int(slide)):
      energy_page.click_element_donut_section_right_arrow()
      time.sleep(1)
    header = energy_page.get_text_donut_section_slide_header()
    sub_header = energy_page.get_text_donut_section_slide_sub_header()
    body = energy_page.get_text_donut_section_slide_body()
    match slide:
      case '0':
        assert 'MORE SAVINGS' in header and 'BUILT SMARTER' in sub_header and 'From the first step' in body
      case '1':
        assert 'BETTER HEALTH' in header and 'FRESHER AIR' in sub_header and 'We know your home holds the people' in body
      case '2':
        assert 'REAL COMFORT' in header and 'COZY RETREAT' in sub_header and 'We design with you in mind' in body
      case '3':
        assert 'PEACE OF MIND' in header and 'AN INDUSTRY' in sub_header and 'been building better for more than' in body
  
  # Test that clicking the buttons in each slide opens the respective popups
  @pytest.mark.parametrize('slide', ['1', '2', '3', '4'])
  def test_donut_slides_buttons(self, slide, driver_settings):
    energy_page = EnergyEfficiencyPage(self.driver)
    energy_page.close_cookies()
    
    for i in range(int(slide) - 1):
      energy_page.click_element_donut_section_right_arrow()
      time.sleep(1)
    
    time.sleep(0.5)

    final_result = False
    for i in range(4): 
      energy_page.click_element_current_slide_button(i+1)
      popup = energy_page.get_element_current_slide_button_popup(i+1)
      result = self.driver.execute_script("return arguments[0].style.display != 'none'", popup)
      if result:
        final_result = True
        energy_page.click_element_empty_space()
        time.sleep(1)
        continue
      else:
        final_result = False
        break
    
    assert final_result
  
  # Test whether the correct header is displayed in the house drawing icons section
  def test_house_drawing_section_header(self):
    energy_page = EnergyEfficiencyPage(self.driver)
    header = energy_page.get_text_house_icon_section_header()
    assert "Click on any icon or scroll through" in header
  
  # Test whether the correct image is displayed in the house drawing icons section
  def test_house_drawing_section_image(self):
    energy_page = EnergyEfficiencyPage(self.driver)
    image = energy_page.get_element_house_icon_section_image()
    result = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", image)
    assert result

  # Test that the buttons on the house image are all clickable
  def test_house_icons_clickable(self, driver_settings):
    energy_page = EnergyEfficiencyPage(self.driver)
    icons = energy_page.get_elements_house_icons()
    final_result = False
    number_icons = 0
    for i in range(len(icons)):
      print("i = ", i)
      is_clickable = energy_page.check_icons_is_clickable(i+1)
      if is_clickable:
        final_result = True
        number_icons = i + 1
        continue
      else:
        final_result = False
        break
      
    assert final_result and number_icons == 32
  
  # Test whether correct header appears for the gallery slider section
  def test_gallery_header(self, driver_settings):
    energy_page = EnergyEfficiencyPage(self.driver)
    header = energy_page.get_text_gallery_slider_section_header()
    assert "Slide through the gallery below" in header
  
  # Test whether correct sub_header appears for the gallery slider section
  def test_gallery_sub_header(self, driver_settings):
    energy_page = EnergyEfficiencyPage(self.driver)
    sub_header = energy_page.get_text_gallery_slider_section_sub_header()
    assert "Click any" in sub_header
  
  # Test the navigation buttons on the top of the gallery slide container and ensure they anvigate to correct slide when pressed
  @pytest.mark.parametrize('nav_number', ['1', '2', '3', '4', '5'])
  def test_gallery_top_nav(self, nav_number, driver_settings):
    energy_page = EnergyEfficiencyPage(self.driver)
    energy_page.close_cookies()
    energy_page.click_element_gallery_slider_top_nav(int(nav_number))
    time.sleep(.5)
    expected_slide = energy_page.get_element_gallery_slider_section_slide(int(nav_number))
    result = self.driver.execute_script("return arguments[0].classList.contains('slick-current') && " + "arguments[0].classList.contains('slick-active')", expected_slide)
    assert result

  # Test whether all of the icons apper on their respective slides in the gallery
  @pytest.mark.parametrize('slide', ['0', '1', '2', '3', '4'])
  def test_icons_in_slides_are_clickable(self, slide, driver_settings):
    energy_page = EnergyEfficiencyPage(self.driver)
    energy_page.close_cookies()
    for i in range(int(slide)):
      energy_page.click_element_gallery_slider_section_right_arrow()
      time.sleep(1)
    clickable = energy_page.check_icons_gallery_section_current_slide_are_clickable()
    assert clickable
  
  # Test whether the correct footer text is appearing in the gallery section
  def test_gallery_section_footer(self):
    energy_page = EnergyEfficiencyPage(self.driver)
    footer = energy_page.get_text_gallery_slider_section_footer()
    assert "M.Connected Home" in footer
  
  # Test whether the correct text is appearing in the gallery section disclaimer
  def test_aside_disclaimer_text(self, driver_settings):
    energy_page = EnergyEfficiencyPage(self.driver)
    disclaimer = energy_page.get_element_aside_disclaimer()
    assert (
      "For additional legal" in disclaimer[0].text and
      "All of our homes built in California" in disclaimer[1].text and
      "Picture is representative and may depict or contain" in disclaimer[2].text
    )
  
  # Test whether the correct header appears in article 2 a real confidence builder section
  def test_article_2_header(self, driver_settings):
    energy_page = EnergyEfficiencyPage(self.driver)
    header = energy_page.get_text_article_2_header()
    assert "A real confidence builder" in header

  # Test whether the correct body appears in article 2 a real confidence builder section
  def test_article_2_body(self, driver_settings):
    energy_page = EnergyEfficiencyPage(self.driver)
    body = energy_page.get_text_article_2_body()
    assert "A real confidence builder" in body

  # Test whether the correct image appears in article 2 a real confidence builder section
  def test_article_2_image(self, driver_settings):
    energy_page = EnergyEfficiencyPage(self.driver)
    image = energy_page.get_element_article_2_image()
    result = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", image)
    assert result
  
  # Test whether the button in the a real confidence builder sections takes the usert ot the correct page when clicked
  def test_article_2_image(self, driver_settings):
    energy_page = EnergyEfficiencyPage(self.driver)
    energy_page.click_element_article_2_button()
    assert "Meritage Homes Awards and Accolades | Meritage Homes" == self.driver.title

# Up to HERS