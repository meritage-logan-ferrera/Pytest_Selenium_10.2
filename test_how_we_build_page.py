from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
from page_how_we_build import HowWeBuildPage
from page_base import BasePage
import math
import pytest
import time

URL = 'https://cd-sit.meritageweb.dev/why-meritage/how-we-build'

@pytest.mark.usefixtures("init__driver", "driver_settings")
class BasicTest():
  pass


class Test_How_We_Build_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get(URL)
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)
  
  def test_main_header(self):
    build_page = HowWeBuildPage(self.driver)
    header = build_page.get_text_main_header()
    assert 'How we build' in header
  
  def test_main_sub_header(self):
    build_page = HowWeBuildPage(self.driver)
    sub_header = build_page.get_text_main_sub_header()
    assert 'From the moment you select your community to the moment' in sub_header
  
  def test_successful_header(self):
    build_page = HowWeBuildPage(self.driver)
    header = build_page.get_text_successful_header()
    assert 'A successful build involves two key' in header
  
  @pytest.mark.parametrize('number', [1,2])
  def test_successful_columns(self, number):
    build_page = HowWeBuildPage(self.driver)
    header = build_page.get_text_successful_div_column_header(number)
    body = build_page.get_text_successful_div_column_body(number)
    image = build_page.get_element_successful_div_column_image(number)
    result = build_page.javascript_image(image)
    match number:
      case 1:
        assert (
          'Focus on partnership' in header and
          'Count on a dedicated team keeping you' in body and
          result
        )
      case 2:
        assert (
          'Commitment to quality' in header and
          'committed to delivering a home' in body and
          result
        )
      
  def test_engaging_header(self):
    build_page = HowWeBuildPage(self.driver)
    header = build_page.get_text_section_1_header()
    assert 'Engaging you in the construction of your home' in header
  
  def test_engaging_sub_header(self):
    build_page = HowWeBuildPage(self.driver)
    sub_header = build_page.get_text_section_1_sub_header()
    assert 'From start to finish' in sub_header
  
  # Test that the drop down containers have the correct image and header
  @pytest.mark.parametrize('drop_down', ['1', '2', '3'])
  def test_section_1_tabs(self, drop_down, driver_settings):
    build_page = HowWeBuildPage(self.driver)
    image = build_page.get_element_section_1_drop_down_container_image(drop_down)
    header = build_page.get_text_section_1_drop_down_container_header(drop_down)
    result = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", image)
    header_bool = False
    match drop_down:
      case '1':
        if "Pre-construction" in header:
          header_bool = True
      case '2':
        if "Pre-drywall" in header:
          header_bool = True
      case '3':
        if "Homeowner orientation" in header:
          header_bool = True
      
    assert header_bool and result
  
  # Test that the drop down containers open the correct tabs when clicked and that all the information within the respective tabs are correct (correct tab displayed on click, header, body text, image). This can be seperated into 4 tests in the future if needed...
  @pytest.mark.parametrize('tab', ['1', '2', '3'])
  def test_section_1_tab_everything(self, tab, driver_settings):
    build_page = HowWeBuildPage(self.driver)
    build_page.close_cookies()
    build_page.click_element_section_1_drop_down(tab)
    current_tab = build_page.get_element_section_1_responsive_tab(tab)
    tab_header = build_page.get_text_section_1_responsive_tab_header(tab)
    tab_body = build_page.get_elements_section_1_responsive_tab_body(tab)
    tab_image = build_page.get_element_section_1_responsive_tab_image(tab)
    
    # SUB TEST 1 for correct tab displayed on click:
    correct_tab =self.driver.execute_script("return arguments[0].classList.contains(\"is-active\")", current_tab) 
    
    # SUB TEST 2 for image:
    correct_image = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", tab_image)
    
    tab_header_bool = False
    tab_body_bool = False
    
    # SUB TESTS 3 & 4 for header and body in tab:
    match tab:
      case '1':
        if "Meet your team" in tab_header:
          tab_header_bool = True
        if "set up a pre-construction" in tab_body[0].text and "What to expect" in tab_body[1].text:
          tab_body_bool = True
      case '2':
        if "See the progress" in tab_header:
          tab_header_bool = True
        if "At this meeting" in tab_body[0].text and "What to expect" in tab_body[1].text:
          tab_body_bool = True
      case '3':
        if "Homeowner orientation" in tab_header:
          tab_header_bool = True
        if "time to celebrate" in tab_body[0].text and "What to expect" in tab_body[1].text:
          tab_body_bool = True
    
    assert (
      correct_tab and 
      tab_header_bool and 
      tab_body_bool and 
      correct_image 
    )
  
  @pytest.mark.parametrize('number', [0, 1, 2])
  def test_pro_tip(self, number):
    build_page = HowWeBuildPage(self.driver)
    build_page.close_cookies()
    for i in range(number):
      build_page.click_element_next_arrow()
      time.sleep(1)
    
    header = build_page.get_text_pro_tip_header()
    body = build_page.get_text_pro_tip_body()

    match number:
      case 0:
        assert (
          'Pro Tip' in header and
          'A house is one of the few things' in body
        )
      case 1:
        assert (
          'Pro Tip' in header and
          'As your home build progresses' in body
        )
      case 2:
        assert (
          'Pro Tip' in header and
          'Communication is key' in body
        )

  def test_quality_header(self):
    build_page = HowWeBuildPage(self.driver)
    header = build_page.get_text_quality_header()
    assert 'The quality of your home' in header

  def test_quality_body(self):
    build_page = HowWeBuildPage(self.driver)
    body = build_page.get_elements_quality_body()
    assert (
      'Nothing is more exciting than' in body[0].text and
      'Use the slider below to navigate' in body[1].text
    )
  
  @pytest.mark.how
  @pytest.mark.parametrize('slide_number', [1, 2, 3, 4, 5, 6, 7, 8, 9])
  def test_slider_and_content(self, slide_number):
    build_page = HowWeBuildPage(self.driver)
    build_page.close_cookies()
    build_page.slide_to_slide(slide_number)
    image = build_page.get_element_active_slide_image()
    header = build_page.get_text_active_slide_header()
    sub_header = build_page.get_text_active_slide_sub_header()
    body = build_page.get_elements_active_slide_body()
    
    result = build_page.javascript_image(image)
    
    match slide_number:
      case 1:
        assert (
          'It all starts with pre-construction' in header and
          'ESTABLISHING THE FRAMEWORK' in sub_header and
          'Congratulations on your new' in body[0].text and
          result
        )
      case 2:
        optional_header = build_page.get_text_active_slide_optional_content_header()
        assert (
          'We lay the foundation of your new' in header and
          'ESTABLISHING THE FRAMEWORK' in sub_header and
          'Construction typically begins' in body[0].text and
          'Construction activity will vary on a daily' in optional_header and
          'Some days' in body[1].text and
          result
        )
      case 3:
        optional_header = build_page.get_text_active_slide_optional_content_header()
        assert (
          'Framing helps' in header and
          'ESTABLISHING THE FRAMEWORK' in sub_header and
          'This is an exciting time' in body[0].text and
          'This phase is extremely active' in optional_header and
          'This phase in the construction' in body[1].text and
          result
        )
      case 4:
        optional_header = build_page.get_text_active_slide_optional_content_header()
        
        if ('The rough mechanics are built' in header and
          'INTERIOR SYSTEMS' in sub_header and
          'Many of the systems' in body[0].text and
          'See energy efficiency' in body[1].text and
          'This phase is a flurry of activity' in optional_header and
          'Plumbing, air ducts, electric wiring' in body[2].text and
          'Soon after this step' in body[3].text and
          result
        ):
          final = True 
        
        self.driver.execute_script("window.scrollBy(0,100)")
        build_page.click_element_active_slide_optional_button()
        assert (
          final and 
          'Best Home Builders for Energy Efficient Homes | Meritage Homes' == self.driver.title
        )
      case 5:
        optional_header = build_page.get_text_active_slide_optional_content_header()
        
        if (
          'Insulation and drywall' in header and
          'INTERIOR SYSTEMS' in sub_header and
          'While this stage may not seem' in body[0].text and
          'Get a closer look' in body[1].text and
          'Your new home will begin to reflect' in optional_header and
          'All the time' in body[2].text and
          result
        ):
          final = True
        self.driver.execute_script("window.scrollBy(0,100)")
        build_page.click_element_active_slide_optional_button()
        assert (
          final and 
          'Best Home Builders for Energy Efficient Homes | Meritage Homes' == self.driver.title
        )
      case 6:
        assert (
          'See your home start to come to life' in header and
          'BRINGING YOUR DESIGN CHOICES' in sub_header and
          'Now the fun part begins' in body[0].text and
          result
        )
      case 7:
        optional_header = build_page.get_text_active_slide_optional_content_header()
        assert (
          'Countertops are installed' in header and
          'BRINGING YOUR DESIGN CHOICES' in sub_header and
          'Your countertops are installed' in body[0].text and
          'getting close to finishing' in optional_header and
          'Now is a great time to review' in body[1].text and
          result
        )
      case 8:
        optional_header = build_page.get_text_active_slide_optional_content_header()
        assert (
          'We lay the final, finishing touches' in header and
          'BRINGING YOUR DESIGN CHOICES' in sub_header and
          'The paint is dry and flooring' in body[0].text and
          'Flooring installation is the final' in optional_header and
          'At this point' in body[1].text and
          result
        )
      case 9:
        optional_header = build_page.get_text_active_slide_optional_content_header()
        assert (
          'Construction is complete' in header and
          '' in sub_header and
          'The big day is here' in body[0].text and
          'Your new Meritage home is' in optional_header and
          'All final inspections' in body[1].text and
          'time to experience Life' in body[2].text and
          result
        )
  
  def test_mymeritage_header(self):
    build_page = HowWeBuildPage(self.driver)
    header = build_page.get_text_mymeritage_header()
    assert 'The MyMeritage portal' in header
  
  def test_mymeritage_body(self):
    build_page = HowWeBuildPage(self.driver)
    body = build_page.get_text_mymeritage_body()
    assert (
      'excited to see your home come to life' in body and
      'Take a look at some' in body
    )
  
  def test_mymeritage_list_text(self):
    build_page = HowWeBuildPage(self.driver)
    mymeritage_list = build_page.get_elements_mymeritage_list()
    assert (
      'Access your warranty' in mymeritage_list[0].text and
      'View your homes floorplan' in mymeritage_list[1].text and
      'Submit and check on the status' in mymeritage_list[2].text
    )
  
  def test_mymeritage_image(self):
    build_page = HowWeBuildPage(self.driver)
    image = build_page.get_element_mymeritage_image()
    result = build_page.javascript_image(image)
    assert result
  
  def test_buy_your_home_header(self):
    build_page = HowWeBuildPage(self.driver)
    header = build_page.get_text_buy_your_home_header()
    assert 'Buy your home with confidence' in header
  
  def test_buy_your_home_body(self):
    build_page = HowWeBuildPage(self.driver)
    body = build_page.get_text_buy_your_home_body()
    assert 'See how we empower you' in body
  
  def test_buy_your_home_button(self):
    build_page = HowWeBuildPage(self.driver)
    build_page.close_cookies()
    build_page.click_element_buy_your_home_button()
    assert 'Home Buying Experience | Meritage Homes' == self.driver.title
  
  def test_aside_ready_to_move_header(self, driver_settings):
    build_page = HowWeBuildPage(self.driver)
    header = build_page.get_text_aside_ready_to_move_header()
    assert 'Ready to make your move' in header
  
  def test_aside_ready_to_move_body(self, driver_settings):
    build_page = HowWeBuildPage(self.driver)
    body = build_page.get_text_aside_ready_to_move_body()
    assert 'Whether you need a little help' in body
  
  def test_aside_ready_to_move_button_1(self, driver_settings):
    build_page = HowWeBuildPage(self.driver)
    build_page.close_cookies()
    build_page.click_element_aside_ready_to_move_button_1()
    assert 'Find a Home | Meritage Homes' == self.driver.title

  def test_aside_ready_to_move_button_2(self, driver_settings):
    build_page = HowWeBuildPage(self.driver)
    build_page.close_cookies()
    build_page.click_element_aside_ready_to_move_button_2()
    assert 'Tour A Meritage Home' == self.driver.title
  
  def test_aside_ready_to_move_number(self):
    build_page = HowWeBuildPage(self.driver)
    time.sleep(4)
    number = build_page.get_text_aside_ready_to_move_number()
    assert 'or call' in number

