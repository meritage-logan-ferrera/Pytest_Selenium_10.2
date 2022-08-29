from page_testimonials import TestimonialsPage
from page_base import BasePage
from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
import pytest

URL = 'https://www.meritagehomes.com/why-meritage/testimonials'

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
  def test_main_sub_header(self):
    test_page = TestimonialsPage(self.driver)
    sub_header = test_page.get_text_main_sub_header()
    assert "Alex and Catherine describe" in sub_header
  
  # Test whether the plauy button opens youtube overlay on click
  def test_main_video_button(self):
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
  def test_aside_1_body(self):
    test_page = TestimonialsPage(self.driver)
    body = test_page.get_text_aside_1_body()
    assert "the place we yearn for" in body
  
  # Test whether the aside 1 button navigates to correct page on click
  def test_aside_1_button(self):
    test_page = TestimonialsPage(self.driver)
    test_page.click_element_aside_1_button()
    assert "" == self.driver.title
  
  # Test whether the header's of each testimonial row contains the correct text
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
  
  # Test whether the bodies of each testimonial row contains the correct text
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
  
  # Test whether the buttons for each testimonials row navigates to the correct page
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
  
  # Test whether the play buttons on the testimonial rows open the yotubue ovelray when pressed
  @pytest.mark.testim
  @pytest.mark.parametrize('row', [1, 2, 3, 4, 5, 6])
  def test_row_overlay_on_play_button_press(self, row, driver_settings):
    test_page = TestimonialsPage(self.driver)
    test_page.close_cookies()
    test_page.click_element_row_play_button(row)
    youtube_overlay = test_page.get_element_youtube_overlay()
    result = self.driver.execute_script("return arguments[0].style.display != \"none\"", youtube_overlay)
    assert result