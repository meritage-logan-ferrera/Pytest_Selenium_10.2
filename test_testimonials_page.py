from page_testimonials import TestimonialsPage
from page_base import BasePage
from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
import pytest

URL = 'https://cd-sit.meritageweb.dev/why-meritage/testimonials'

@pytest.mark.usefixtures("init__driver")
class BasicTest():
  pass

class Test_Testimonials_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get(URL)
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)
  
  # Test whether the correct text is displayed in main header
  def test_main_header(self, driver_settings):
    test_page = TestimonialsPage(self.driver)
    header = test_page.get_text_main_header()
    assert "Alex & Catherine" in header

  # Test whether the correct text is displayed in main sub_header
  def test_main_sub_header(self, driver_settings):
    test_page = TestimonialsPage(self.driver)
    sub_header = test_page.get_text_main_sub_header()
    assert "Alex and Catherine describe" in sub_header
  
  # Test whether the play button opens youtube overlay on click
  def test_main_video_button(self, driver_settings):
    test_page = TestimonialsPage(self.driver)
    test_page.click_element_play_button()
    youtube_overlay = test_page.get_element_youtube_overlay()
    result = self.driver.execute_script("return arguments[0].style.display != \"none\"", youtube_overlay)
    assert result
  
  # Test whether the correct text is displayed in aside_1 header
  def test_aside_1_header(self, driver_settings):
    test_page = TestimonialsPage(self.driver)
    header = test_page.get_text_aside_1_header()
    assert "A slice" in header
  
  # Test whether the correct text is displayed in aside 1 body
  def test_aside_1_body(self, driver_settings):
    test_page = TestimonialsPage(self.driver)
    body = test_page.get_text_aside_1_body()
    assert "the place we yearn for" in body
  
  # Test whether the aside 1 button navigates to correct page on click
  @pytest.mark.nlog
  def test_aside_1_button(self, driver_settings):
    test_page = TestimonialsPage(self.driver)
    test_page.close_cookies()
    test_page.click_element_aside_1_button()
    assert "" == self.driver.title
  
  # Test whether the headers of each testimonial row contain the correct text
  @pytest.mark.parametrize('row', [1, 2, 3, 4, 5, 6])
  def test_row_headers(self, row, driver_settings):
    test_page = TestimonialsPage(self.driver)
    header = test_page.get_text_row_header(row)
    match row:
      case 1:
        assert "Ken & Cheryl" in header
      case 2:
        assert "Alan & Alison" in header
      case 3:
        assert "Tom & Kristie" in header
      case 4:
        assert "Alex & Rachel" in header
      case 5:
        assert "Daniel & Terry" in header
      case 6:
        assert "Nick & Stephanie" in header
  
  # Test whether the bodies of each testimonial row contain the correct text
  @pytest.mark.parametrize('row', [1, 2, 3, 4, 5, 6])
  def test_row_bodies(self, row, driver_settings):
    test_page = TestimonialsPage(self.driver)
    body = test_page.get_text_row_body(row)
    match row:
      case 1:
        assert "Ken and Cheryl" in body
      case 2:
        assert "Alan and Alison" in body
      case 3:
        assert "Tom and Kristie" in body
      case 4:
        assert "Rachel and Alex" in body # Switched from header
      case 5:
        assert "Daniel and Terri" in body # Terry's name different
      case 6:
        assert "Nick and Stephanie" in body
  
  # Test whether the buttons for each testimonials row navigate to the correct page
  @pytest.mark.testimonials
  @pytest.mark.parametrize('row', [1, 2, 3, 4, 5, 6])
  def test_row_buttons(self, row, driver_settings):
    test_page = TestimonialsPage(self.driver)
    test_page.close_cookies()
    test_page.click_element_row_button(row)
    youtube_overlay = test_page.get_element_youtube_overlay()
    result = self.driver.execute_script("return arguments[0].style.display != \"none\"", youtube_overlay)
    assert result
  
  # Test whether the placeholder images for each testimonials row is on the page
  @pytest.mark.parametrize('row', [1, 2, 3, 4, 5, 6])
  def test_row_images(self, row, driver_settings):
    test_page = TestimonialsPage(self.driver)
    image = test_page.get_element_row_image(row)
    result = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", image)
    assert result
  
  # Test whether the play buttons on the testimonial rows open the youtube overlay when pressed
  @pytest.mark.parametrize('row', [1, 2, 3, 4, 5, 6])
  def test_row_overlay_on_play_button_press(self, row, driver_settings):
    test_page = TestimonialsPage(self.driver)
    test_page.close_cookies()
    test_page.click_element_row_play_button(row)
    youtube_overlay = test_page.get_element_youtube_overlay()
    result = self.driver.execute_script("return arguments[0].style.display != \"none\"", youtube_overlay)
    assert result
  
  # Test that the correct header is displayed in aside 2
  def test_aside_2_header(self, driver_settings):
    test_page = TestimonialsPage(self.driver)
    header = test_page.get_text_avid_header()
    assert "Get the local lowdown" in header
  
  # Test that the correct body text is displayed in aside 2
  def test_aside_2_body(self, driver_settings):
    test_page = TestimonialsPage(self.driver)
    body = test_page.get_text_avid_body()
    assert "Select your state to see what homeowners" in body
  
  # Test that the correct image is displayed in aside 2
  def test_aside_2_image(self, driver_settings):
    test_page = TestimonialsPage(self.driver)
    image = test_page.get_element_avid_image()
    result = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", image)
    assert result
  
  # Test that the button in aside 2 navigates to correct page when clicked
  # THIS LINK IS BROKEN, avid website also automatically closes selenium driver so assert title == nothing
  @pytest.mark.testim
  def test_aside_2_button(self, driver_settings):
    test_page = TestimonialsPage(self.driver)
    test_page.close_cookies()
    test_page.click_element_avid_button()
    assert "" in self.driver.title
  
  # Test that the correct header is displayed for the local lowdown section/article
  def test_section_local_lowdown_header(self, driver_settings):
    test_page = TestimonialsPage(self.driver)
    header = test_page.get_text_section_local_header()
    assert "Get the local lowdown" in header
  
  # Test that the correct body text is displayed in section local lowdown
  def test_section_local_lowdown_body(self, driver_settings):
    test_page = TestimonialsPage(self.driver)
    body = test_page.get_text_section_local_body()
    assert "Select your state to see what homeowners" in body
  
  # Test that clicking on a metro area in the dropdown displays a dynamic number of homeowner testimonials depending on region selected. To test this, first make sure that the default option is displaying quotes, then select "select a metro area" from the dropdown and test that there are no quotes displayed
  def test_section_local_lowdown_dropdwon(self, driver_settings):
    test_page = TestimonialsPage(self.driver)
    test_page.close_cookies()
    
    # For option Phoenix selected
    phoenix = False
    phoenix_homeowner_testimonials = test_page.get_elements_section_local_under_dropdown()
    if len(phoenix_homeowner_testimonials) > 0:
      phoenix = True
    
    #For "Select a metro area" selected
    select_metro = False
    test_page.click_element_section_local_dropdown()
    test_page.click_element_section_local_dropdown_select_a_metro()
    select_homeowner_testimonials = test_page.get_elements_section_local_under_dropdown()
    if len(select_homeowner_testimonials) == 0:
      select_metro = True
    
    assert phoenix and select_metro
  
  # Test whether correct header is displayed for the testimonial submission section
  def test_testimonial_submission_header(self, driver_settings):
    test_page = TestimonialsPage(self.driver)
    header = test_page.get_text_testimonial_submission_header()
    assert "Share your story" in header

  # Test whether correct body text is displayed for the testimonial submission section
  def test_testimonial_submission_body(self, driver_settings):
    test_page = TestimonialsPage(self.driver)
    body = test_page.get_text_testimonial_submission_body()
    assert "Are you a Meritage homeowner with a noteworthy story to tell" in body
  
  # Tests for the share your story form
  ###############
  # Test whether user can input into first name field
  def test_first_name_input(self, driver_settings):
    test_page = TestimonialsPage(self.driver)
    input_value = test_page.get_input_first_name(self.driver)
    assert 'test_input' == input_value 
  
  # Test whether user can input into last name field
  def test_last_name_input(self, driver_settings):
    test_page = TestimonialsPage(self.driver)
    input_value = test_page.get_input_last_name(self.driver)
    assert 'test_input' == input_value 
  
  # Test whether user can input into email address field
  def test_email_address_input(self, driver_settings):
    test_page = TestimonialsPage(self.driver)
    input_value = test_page.get_input_create_account_email_address(self.driver)
    assert 'test_input' == input_value 
  
  # Test whether user can input into phone number field
  def test_phone_number_input(self, driver_settings):
    test_page = TestimonialsPage(self.driver)
    input_value = test_page.get_input_phone_number(self.driver)
    assert 'test_input' == input_value 
  
  # Test whether user can input into your story field
  def test_your_story_input(self, driver_settings):
    test_page = TestimonialsPage(self.driver)
    input_value = test_page.get_input_your_story()
    assert 'test_input' == input_value 
  
  # Test whether the green checkmark appears on clicking agree to terms
  def test_checkmark_on_agree_terms_click(self, driver_settings):
    test_page = TestimonialsPage(self.driver)
    test_page.close_cookies()
    test_page.click_element_agree_to_terms()
    agree_box = test_page.get_element_agree_to_terms()
    result = self.driver.execute_script("return arguments[0].className != 'is-invalid-label'", agree_box)
    assert result
  
  # Test whether the button in the testimonial submission form is clickable (I do not want to actually click it or else it would send trash to our integration every time we test)
  def test_testimonial_submission_button_is_clickable(self, driver_settings):
    test_page = TestimonialsPage(self.driver)
    result = test_page.check_element_testimonial_submission_button_is_clickable()
    assert result
  ###############

  # Test whether correct header is displayed in aside 3
  def test_aside_3_header(self, driver_settings):
    test_page = TestimonialsPage(self.driver)
    header = test_page.get_text_aside_3_header()
    assert "Your story begins here" in header
  
  # Test whether correct body is displayed in aside 3
  def test_aside_3_body(self, driver_settings):
    test_page = TestimonialsPage(self.driver)
    body = test_page.get_text_aside_3_body()
    assert "There are many great homes" in body

  # Test whether button in aside 3 navigates to correct page on click
  def test_aside_3_button(self, driver_settings):
    test_page = TestimonialsPage(self.driver)
    test_page.close_cookies()
    test_page.click_element_aside_3_button()
    assert "Find a Home | Meritage Homes" == self.driver.title

  # Further testing:
  # After checking and unchecking the accept terms and conditions box, the text turns red
  # Labels inside testimonial submission
  # Dropdown for location in testimonial submission