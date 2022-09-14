from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
from page_about_us import AboutUsPage
from page_base import BasePage
import math
import pytest
import time

URL = 'https://www.meritagehomes.com/about-us'

@pytest.mark.usefixtures("init__driver")
class BasicTest():
  pass

class Test_About_Us_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get(URL)
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)
  
  # Test whether ocrrect main header appears
  def test_main_header(self, driver_settings):
    about_page = AboutUsPage(self.driver)
    header = about_page.get_text_main_header()
    assert 'About Meritage Homes' in header

  # Test whether occret main sub header appears
  def test_main_sub_header(self, driver_settings):
    about_page = AboutUsPage(self.driver)
    sub_header = about_page.get_text_main_sub_header()
    assert 'Opening the door to a Life' in sub_header
  
  # Test whether correct header appears in building for you section
  def test_building_header(self, driver_settings):
    about_page = AboutUsPage(self.driver)
    header = about_page.get_text_building_header()
    assert 'Building for you' in header

  # Test whether correct body appears in building for you section
  def test_building_body(self, driver_settings):
    about_page = AboutUsPage(self.driver)
    body = about_page.get_text_building_body()
    assert 'invested millions of dollars' in body

  # Test that each container in building section has the correct image
  @pytest.mark.parametrize('element', ['1', '2', '3', '4'])
  def test_building_section_containers_image(self, element, driver_settings):
    about_page = AboutUsPage(self.driver)
    container_image = about_page.get_element_building_section_container_image(element)
    result = self.driver.execute_script("return arguments[0].complete &&" + " arguments[0].width > 0", container_image)
    assert result
  
  # Test that the each container in building section has the correct pre-header
  @pytest.mark.parametrize('element', ['1', '2', '3', '4'])
  def test_building_section_containers_pre_heading(self, element, driver_settings):
    about_page = AboutUsPage(self.driver)
    container_pre_heading = about_page.get_text_building_section_container_pre_heading(element)
    assert "LIVE WITH" == container_pre_heading
  
  # Test that each container in building section has the correct header
  @pytest.mark.parametrize('element', ['1', '2', '3', '4'])
  def test_building_section_containers_header(self, element, driver_settings):
    about_page = AboutUsPage(self.driver)
    container_header = about_page.get_text_building_section_container_header(element)
    match element:
      case '1':
        assert 'MORE SAVINGS' == container_header
      case '2':
        assert 'BETTER HEALTH' == container_header
      case '3':
        assert 'REAL COMFORT' == container_header
      case '4':
        assert 'PEACE OF MIND' == container_header
      case _:
        assert False
  
  # Test that each container in building section has the correct description
  @pytest.mark.parametrize('element', ['1', '2', '3', '4'])
  def test_building_section_containers_description(self, element, driver_settings):
    about_page = AboutUsPage(self.driver)
    container_description = about_page.get_text_building_section_container_description(element)
    match element:
      case '1':
        assert 'Because your home is built smarter' in container_description
      case '2':
        assert 'Because your home has fresher air' in container_description
      case '3':
        assert 'Because your home is a cozy' in container_description
      case '4':
        assert 'Because you have an industry' in container_description
      case _:
        assert False
      
  # Test whether clicking building section button takes user to correct page
  def test_building_button(self, driver_settings):
    about_page = AboutUsPage(self.driver)
    about_page.close_cookies()
    about_page.click_element_building_section_button()
    assert 'Why Meritage? Energy Efficient Homes | Meritage Homes' == self.driver.title
  
  # Test whether correct header appears in "Earning the right to be your builder" section
  def test_earning_header(self, driver_settings):
    about_page = AboutUsPage(self.driver)
    header = about_page.get_text_earning_header()
    assert 'Earning the right to be your builder' in header
  
  # Test whether correct sub header appears in "Earning the right to be your builder" section
  def test_earning_sub_header(self, driver_settings):
    about_page = AboutUsPage(self.driver)
    sub_header = about_page.get_text_earning_sub_header()
    assert 'Experience Life' in sub_header
  
  # Test whether correct body appears in "Earning the right to be your builder" section
  def test_earning_body(self, driver_settings):
    about_page = AboutUsPage(self.driver)
    body = about_page.get_text_earning_body()
    assert 'Earning the right to be your builder' in body

  # Tets whether the correct image appears in the earning the right section
  def test_earning_image(self, driver_settings):
    about_page = AboutUsPage(self.driver)
    image = about_page.get_element_earning_image()
    result =  self.driver.execute_script("return arguments[0].complete && " + "argumnts[0].width > 0", image)
    assert result
  
  # Test wheter the button in the earning section takes the user to the correct page when clicked
  def test_earning_button(self, driver_settings):
    about_page = AboutUsPage(self.driver)
    about_page.close_cookies()
    about_page.click_element_earning_button()
    assert 'Tour a Meritage Home' == self.driver.title

  # Test wheter the play button in the earning section opens the youtube overlay
  def test_earning_play_button(self, driver_settings):
    about_page = AboutUsPage(self.driver)
    about_page.close_cookies()
    about_page.click_element_earning_play_button()
    youtube_overlay = about_page.get_element_youtube_overlay()
    result = self.driver.execute_script("return arguments[0].style.display != 'none", youtube_overlay)
    assert result
  
  # Test whether correct header appears in "Building a track record" section
  def test_track_header(self, driver_settings):
    about_page = AboutUsPage(self.driver)
    header = about_page.get_text_track_header()
    assert 'Building a track record of success' in header
  
  # Test whether correct body appears in "Building a track record" section
  def test_track_body(self, driver_settings):
    about_page = AboutUsPage(self.driver)
    body = about_page.get_text_track_body()
    assert 'nationally recognized leader in the homebuilding' in body
  
  # Test whether the button in track record page takes user to correct page when clicked
  def test_track_button(self, driver_settings):
    about_page = AboutUsPage(self.driver)
    about_page.close_cookies()
    about_page.click_element_track_button()
    assert 'Meritage Homes Awards and Accolades | Meritage Homes' == self.driver.title  
  
  # Tets whether all the correct (currently 7) images appears in the track record section
  def test_track_images(self, driver_settings):
    about_page = AboutUsPage(self.driver)
    images = about_page.get_elements_track_images()
    image_exists = False
    if len(images) == 7:
      for i in range(len(images)):
        result = self.driver.execute_script("return arguments[0].compelte && " + "argumnets[0].width > 0", images[i])
        if result:
          image_exists = True
        else:
          assert False
      assert image_exists
    else:
      assert False

  # Test whether correct header appears in "Giving back where we build" section
  def test_giving_back_header(self, driver_settings):
    about_page = AboutUsPage(self.driver)
    header = about_page.get_text_giving_back_header()
    assert 'Giving back where we build' in header

  # Test whether correct body appears in "Giving back where we build" section
  def test_giving_back_body(self, driver_settings):
    about_page = AboutUsPage(self.driver)
    body = about_page.get_text_giving_back_body()
    assert 'committed to building better homes' in body

  # Test whether correct sub_header appears in "Giving back where we build" section
  def test_giving_back_sub_header(self, driver_settings):
    about_page = AboutUsPage(self.driver)
    sub_header = about_page.get_text_giving_back_sub_header()
    assert '30+ years of building strong communities' in sub_header

  # Test whether correct bpdy under the sub header appears in "Giving back where we build" section
  def test_giving_back_sub_header_body(self, driver_settings):
    about_page = AboutUsPage(self.driver)
    sub_header_body = about_page.get_text_giving_back_sub_header_body()
    assert 'Supporting communities through giving is a cornerstone' in sub_header_body
  
  # Test whether the button in the "Giving back" section navigates to correct page hwen clicked
  def test_giving_back_button(self, driver_settings):
    about_page = AboutUsPage(self.driver)
    about_page.close_cookies()
    about_page.click_element_giving_back_button()
    assert 'Meritage Cares: Operation Homefront | Meritage Homes' in self.driver.title
  
  # Test whether correct image appears in "Giving back" section
  def test_giving_back_image(self, driver_settings):
    about_page = AboutUsPage(self.driver)
    image = about_page.get_element_giving_back_image()
    result = about_page.javascript_image(image)
    assert result

  
  # Test whether correct header appears in "We build great careers, too." section
  def test_great_careers_header(self, driver_settings):
    about_page = AboutUsPage(self.driver)
    header = about_page.get_text_great_careers_header()
    assert 'We build great careers, too.' in header

  # Test whether correct body appears in "We build great careers, too." section
  def test_great_careers_body(self, driver_settings):
    about_page = AboutUsPage(self.driver)
    body = about_page.get_text_great_careers_body()
    assert 'From constructing a home' in body

  # Test whether the button in the "Great careers" section navigates to correct page hwen clicked
  def test_great_careers_button(self, driver_settings):
    about_page = AboutUsPage(self.driver)
    about_page.close_cookies()
    about_page.click_element_great_careers_button()
    assert 'Meritage Careers - Real Estate Careers | Meritage Homes' == self.driver.title
  
  # Test whether correct image appears in "Great careers" section
  def test_great_careers_image(self, driver_settings):
    about_page = AboutUsPage(self.driver)
    image = about_page.get_element_great_careers_image()
    result = about_page.javascript_image(image)
    assert result
  
  # Test whether correct header appears in "Building where you want to live" section
  def test_building_where_header(self, driver_settings):
    about_page = AboutUsPage(self.driver)
    header = about_page.get_text_building_where_header()
    assert 'Building where you want to live' in header

  # Test whether correct body appears in "Building where you want to live" section
  def test_building_where_body(self, driver_settings):
    about_page = AboutUsPage(self.driver)
    body = about_page.get_text_building_where_body()
    assert 'proud to build homes that are located' in body

  # Test whether the button in the "Great careers" section navigates to correct page hwen clicked
  def test_building_where_button(self, driver_settings):
    about_page = AboutUsPage(self.driver)
    about_page.close_cookies()
    about_page.click_element_building_where_button()
    assert 'Find a Home | Meritage Homes' == self.driver.title