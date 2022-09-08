from page_main import MainPage
from page_base import BasePage
from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
import pytest
import time

URL = 'https://www.meritagehomes.com/'

@pytest.mark.usefixtures("init__driver")
class BasicTest(test_footer, test_header):
  pass

class Test_Main_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get(URL)
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)
  
  # Test that the Meritage video is playing
  def test_meritage_video(self, driver_settings):
    main_page = MainPage(self.driver)
    meritage_video = main_page.get_element_meritage_video()
    result = self.driver.execute_script("return arguments[0].currentTime > 0", meritage_video)
    assert result

  #Test that Life. Built. Better. header is present
  def test_life_built_better(self, driver_settings):
    main_page = MainPage(self.driver)
    life_built_better = main_page.get_text_life_built_better()
    assert "Life. Built. Better." in life_built_better

  # Test that the sub header with the value "Let us help.." is present
  def test_let_us_find(self, driver_settings):
    main_page = MainPage(self.driver)
    let_us_find = main_page.get_text_let_us_find()
    assert "Let us help you find your perfect home" in let_us_find
  
  # Test that clicking the scroll down arrow scrolls the page down to the top of the next section (aside/article)
  def test_scroll_down_arrow(self, driver_settings):
    html = BasePage(self.driver).get_html()
    main_page = MainPage(self.driver)
    main_page.close_cookies()
    main_page.click_element_scroll_down_arrow()
    result = self.driver.execute_script("return arguments[0].scrollTop > 100", html)
    assert result
  
  # TESTS FOR SAVE THE RATE PROMOTION WHICH ENDED
  # # Test that the save the rate image is present 
  # def test_save_the_rate_image(self, driver_settings):
  #   main_page = MainPage(self.driver)
  #   main_page.close_cookies()
  #   save_the_rate_image = main_page.get_element_save_the_rate_image()
  #   result = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", save_the_rate_image)
  #   assert result

  # # Test that the save the rate header contains correct text
  # def test_aside_1_save_the_rate_header(self, driver_settings):
  #   main_page = MainPage(self.driver)
  #   save_the_rate_header = main_page.get_text_aside_1_save_the_rate_h2()
  #   assert "Save the Rate and buy with confidence" in save_the_rate_header
  
  # # Test that the see details button in aside 1 navigates to correct page
  # def test_aside_1_button(self, driver_settings):
  #   main_page = MainPage(self.driver)
  #   main_page.close_cookies()
  #   main_page.click_element_aside_1_save_the_rate_button()
  #   assert "Save the Rate | Meritage Homes" == self.driver.title
  
  # Test that that the image placeholder for the video is present in article 1
  def test_article_1_video_image(self, driver_settings):
    main_page = MainPage(self.driver)
    placeholder_image = main_page.get_element_article_1_video_image()
    result = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", placeholder_image)
    assert result
  
  # Test that the video overlay pops up on pressing the play button
  def test_article_1_overlay_on_play_button_click(self, driver_settings):
    main_page = MainPage(self.driver)
    main_page.close_cookies()
    main_page.click_element_article_1_play_button()
    video_overlay = main_page.get_element_article_1_video_overlay()
    result = self.driver.execute_script("return arguments[0].style.display != \"none\"", video_overlay)
    assert result

  # Test that the correct header is showing up in article 1
  def test_article_1_header(self, driver_settings):
    main_page = MainPage(self.driver)
    header_text = main_page.get_text_article_1_header()
    assert "Not all new homes are created equal" in header_text
  
  # Test that the correct sub-header is showing in article 1
  def test_article_1_sub_header(self, driver_settings):
    main_page = MainPage(self.driver)
    sub_header = main_page.get_text_article_1_subtext()
    assert "Knowing what to look for during your new home" in sub_header
  
  # Test that the correct header is displayed in article 2
  def test_article_2_header(self, driver_settings):
    main_page = MainPage(self.driver)
    header_text = main_page.get_text_article_2_header()
    assert "The search starts here:" in header_text
  
  # Test that the correct sub-header is displayed in article 2
  def test_article_2_sub_header(self, driver_settings):
    main_page = MainPage(self.driver)
    sub_header_text = main_page.get_text_article_2_subtext()
    assert "Get started by selecting a state below" in sub_header_text
  
  # Test that all the state containers take you to the correct page
  @pytest.mark.parametrize('row, column', [(2,1), (2,2), (3,1), (4,1), (4,2), (5,1), (5,2), (6,1), (6,2)])
  def test_article_2_state_containers(self, row, column, driver_settings):
    main_page = MainPage(self.driver)
    main_page.close_cookies()
    main_page.click_element_article_2_state_container_button(row, column)
    if row == 2 and column == 1:
        assert 'Arizona' == self.driver.title
    elif row == 2 and column == 2:
        assert 'California' == self.driver.title
    elif row == 3 and column == 1:
        assert 'Colorado' == self.driver.title
    elif row == 4 and column == 1:
        assert 'Georgia' == self.driver.title
    elif row == 4 and column == 2:
        assert 'Florida' == self.driver.title
    elif row == 5 and column == 1:
        assert 'North Carolina' == self.driver.title
    elif row == 5 and column == 2:
        assert 'South Carolina' == self.driver.title
    elif row == 6 and column == 1:
        assert 'Tennessee' == self.driver.title
    elif row == 6 and column == 2:
        assert 'Texas' == self.driver.title
    else:
        assert False
      
  # Test that clicking the look back container takes user to correct page
  def test_article_3_look_back(self, driver_settings):
    main_page = MainPage(self.driver)
    main_page.close_cookies()
    main_page.click_element_article_3_a_look_back()
    assert "Operation Homefront 2021 | The Johnson Family - YouTube" == self.driver.title
  
  # Test that clicking the frame signing container takes user to correct page
  def test_article_3_frame_signing(self, driver_settings):
    main_page = MainPage(self.driver)
    main_page.close_cookies()
    main_page.click_element_article_3_frame_signing()
    assert "Operation Homefront | Meritage Homes" == self.driver.title
  
  # Test that the correct header is displayed in article 3
  def test_article_3_header(self, driver_settings):
    main_page = MainPage(self.driver)
    header_text = main_page.get_text_article_3_header()
    assert "Supporting Military Families" in header_text

  # Test that the button in article 3 navigates to correct page
  def test_article_3_button(self, driver_settings):
    main_page = MainPage(self.driver)
    main_page.close_cookies()
    main_page.click_element_article_3_button()
    assert "Operation Homefront | Meritage Homes" == self.driver.title

  # Test that the correct header is displayed in article 4
  def test_article_4_header(self, driver_settings):
    main_page = MainPage(self.driver)
    header_text = main_page.get_text_article_4_header()
    assert "It's time to expect more from your homebuilder" in header_text

  # Test that the correct sub-header is displayed in article 4
  def test_article_4_header(self, driver_settings):
    main_page = MainPage(self.driver)
    sub_header_text = main_page.get_text_article_4_subtext()
    assert 'setting the new standard for' in sub_header_text
  
  # Test that each container in article 4 has the correct image
  @pytest.mark.parametrize('element', ['1', '2', '3', '4'])
  def test_article_4_containers_image(self, element, driver_settings):
    main_page = MainPage(self.driver)
    container_image = main_page.get_element_article_4_container_image(element)
    result = self.driver.execute_script("return arguments[0].complete &&" + " arguments[0].width > 0", container_image)
    assert result
  
  # Test that the each container in article 4 has the correct pre-header
  @pytest.mark.parametrize('element', ['1', '2', '3', '4'])
  def test_article_4_containers_pre_heading(self, element, driver_settings):
    main_page = MainPage(self.driver)
    container_pre_heading = main_page.get_text_article_4_container_pre_heading(element)
    assert "LIVE WITH" == container_pre_heading
  
  # Test that each container in article 4 has the correct header
  @pytest.mark.parametrize('element', ['1', '2', '3', '4'])
  def test_article_4_containers_header(self, element, driver_settings):
    main_page = MainPage(self.driver)
    container_header = main_page.get_text_article_4_container_header(element)
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
  
  # Test that each container in article 4 has the correct description
  @pytest.mark.parametrize('element', ['1', '2', '3', '4'])
  def test_article_4_containers_description(self, element, driver_settings):
    main_page = MainPage(self.driver)
    container_description = main_page.get_text_article_4_container_description(element)
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
      
  # Test that the button in article 4 navigates to the correct page
  def test_article_4_button(self, driver_settings):
    main_page = MainPage(self.driver)
    main_page.close_cookies()
    main_page.click_element_article_4_button()
    assert "Why Meritage? Energy Efficient Homes | Meritage Homes" == self.driver.title

  # Test that the Alex image appears. This is supposed to be dynamic but is BROKEN right now.
  @pytest.mark.parametrize('number', ['0'])
  def test_article_5_image_in_carousel(self, number, driver_settings):
    main_page = MainPage(self.driver)
    carousel_image = main_page.get_element_article_5_image_in_carousel(number)
    result = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", carousel_image)
    assert result
  
  # Test that the correct header is displayed in article 5
  def test_article_5_header(self, driver_settings):
    main_page = MainPage(self.driver)
    header = main_page.get_text_article_5_header()
    assert "Welcome home" in header
  
  # Test that the orbit containers are being switched to correctly
  # ALSO test that the video overlay opens on each slide
  @pytest.mark.logan
  @pytest.mark.parametrize('data_slide', ['0', '1', '2', '3', '4', '5', '6', '7'])
  def test_article_5_orbit_slides(self, data_slide, driver_settings):
    main_page = MainPage(self.driver)
    main_page.close_cookies()
    current_slide = main_page.get_element_article_5_orbit_slide(data_slide)
    
    if data_slide != '0':
      for i in range(int(data_slide)):
        main_page.click_element_article_5_right_button()
        time.sleep(.75)

    main_page.click_element_article_5_orbit_video(int(data_slide))
    youtube_overlay = main_page.get_element_article_5_youtube_overlay()
    result = self.driver.execute_script("return arguments[0].classList.contains(\"is-active\") && " + "arguments[1].style.display != \"none\"", current_slide, youtube_overlay)
    assert result
  
  # Test that each orbit slide contains the correct text content -- BOTH quote and attribution. As opposed to the test above, we get the orbit slide AFTER clicking and check that the current slide has the correct info. Whereas in the last test we got the slide we needed first and then clicked to make sure that the clicks brought us to the predetermined slide...
  @pytest.mark.parametrize('data_slide', ['0', '1', '2', '3', '4', '5', '6', '7'])
  def test_article_5_orbit_slides_text(self, data_slide, driver_settings):
    main_page = MainPage(self.driver)
    main_page.close_cookies()

    if data_slide != '0':
      for i in range(int(data_slide)):
        main_page.click_element_article_5_right_button()
        time.sleep(.5)

    quote = main_page.get_text_article_5_container_quote(data_slide)
    attribution = main_page.get_text_article_5_container_attribution(data_slide)

    match data_slide:
      case '0':
        assert "The home is very comfortable" in quote and "Alex" in attribution
      case '1':
        assert "From start to finish" in quote and "Tom" in attribution
      case '2':
        assert "The homes..." in quote and "Ken" in attribution
      case '3':
        assert "We had so many questions" in quote and "Alex" in attribution
      case '4':
        assert "It has, in every way" in quote and "Terri" in attribution
      case '5':
        assert "It's a very family-oriented" in quote and "Nick" in attribution
      case '6':
        assert "When we walked into this house" in quote and "Alan" in attribution
      case '7':
        assert "Meritage is an awesome builder" in quote and "Sylvia" in attribution
      case _:
        assert False
      
  # Test that the correct header is displayed in article 6
  def test_article_6_header(self, driver_settings):
    main_page = MainPage(self.driver)
    header = main_page.get_element_article_6_header()
    assert "Awards & Accolades" in header

  # Test that the partner image is displayed in article 6
  def test_article_6_partner_image(self, driver_settings):
    main_page = MainPage(self.driver)
    partner_image = main_page.get_element_article_6_partner_image()
    result = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", partner_image)
    assert result
  
  # Test thatthe avid image is displayed in article 6
  def test_article_6_avid_image(self, driver_settings):
    main_page = MainPage(self.driver)
    avid_image = main_page.get_element_article_6_avid_image()
    result = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", avid_image)
    assert result
  
  # Test that the correct header is displayed in article 7
  def test_article_7_header(self, driver_settings):
    main_page = MainPage(self.driver)
    header = main_page.get_text_article_7_header()
    assert "Your search just got smarter" in header
  
  # Test that the correct header is in the first image container
  def test_article_7_image_1_header(self, driver_settings):
    main_page = MainPage(self.driver)
    header = main_page.get_text_article_7_image_container_1_header()
    assert "Financing your new home" in header
  
  # Test that the correct header is in the second image container
  def test_article_7_image_2_header(self, driver_settings):
    main_page = MainPage(self.driver)
    header = main_page.get_text_article_7_image_container_2_header()
    assert "Guide to homebuying" in header
  
  # Test that clicking the first container take the user to the correct page
  def test_article_7_container_1_navigation(self, driver_settings):
    main_page = MainPage(self.driver)
    main_page.close_cookies()
    main_page.click_element_article_7_image_container_1()
    assert "New Home Builder - Energy-Efficient New Homes | Meritage Homes" in self.driver.title
  
  # Test that clicking the second container take the user to the correct page
  def test_article_7_container_2_navigation(self, driver_settings):
    main_page = MainPage(self.driver)
    main_page.close_cookies()
    main_page.click_element_article_7_image_container_2()
    assert "Buying a Home in 2022" in self.driver.title
  
  # Test that the button navigates to the correct page
  def test_article_7_button(self, driver_settings):
    main_page = MainPage(self.driver)
    main_page.close_cookies()
    main_page.click_element_article_7_button()
    assert "Buyer Resources & Tools For New Homeowners | Meritage Homes" in self.driver.title
  
  # Test that the correct header appears in aside 2
  def test_aside_2_header(self, driver_settings):
    main_page = MainPage(self.driver)
    header = main_page.get_text_aside_2_header()
    assert "Ready to find your home" in header
  
  # Test that the correct sub-header is displayed in aside 2
  def test_aside_2_sub_header(self, driver_settings):
    main_page = MainPage(self.driver)
    sub_header = main_page.get_text_aside_2_subtext()
    assert "There are many great homes" in sub_header
  
  # Test that the button in aside 2 navigates to the correct page
  def tests_aside_2_button(self, driver_settings):
    main_page = MainPage(self.driver)
    main_page.close_cookies()
    main_page.click_element_aside_2_button()
    assert "" == self.driver.title # Title is missing on contact us page
  