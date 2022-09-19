from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
from page_how_we_design import HowWeDesignPage
from page_base import BasePage
import math
import pytest
import time

URL = 'https://cd-sit.meritageweb.dev/why-meritage/how-we-design'

@pytest.mark.usefixtures("init__driver", "driver_settings")
class BasicTest():
  pass


class Test_How_We_Design_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get(URL)
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)
  
  def test_main_header(self):
    design_page = HowWeDesignPage(self.driver)
    header = design_page.get_text_main_header()
    assert 'Dream homes. Dream designs' in header
  
  def test_main_sub_header(self):
    design_page = HowWeDesignPage(self.driver)
    sub_header = design_page.get_text_main_sub_header()
    assert 'Find out what to expect when' in sub_header
  
  def test_article_no_header_text(self):
    design_page = HowWeDesignPage(self.driver)
    text = design_page.get_text_article_no_header_body()
    assert (
      'Discover a whole new kind of' in text and
      'After conducting third-party' in text and
      'Now, whether you choose a quick move-in' in text
    )
  
  def test_article_no_header(self):
    design_page = HowWeDesignPage(self.driver)
    design_page.close_cookies()
    design_page.click_element_article_no_header_button()
    assert 'Wakefield Study| Meritage Homes' in self.driver.title
  
  def test_design_header(self):
    design_page = HowWeDesignPage(self.driver)
    header = design_page.get_text_design_header()
    assert 'Design Collections' in header
  
  def test_design_body(self):
    design_page = HowWeDesignPage(self.driver)
    body = design_page.get_elements_design_body()
    assert (
      # first p tag is empty
      'Bring your style to life' in body[1].text and
      'Our interior design experts have created a lineup' in body[1].text and
      'Design Collections communities' in body[2].text
    )
  
  def test_design_image(self):
    design_page = HowWeDesignPage(self.driver)
    image = design_page.get_element_design_image()
    result = design_page.javascript_image(image)
    assert result
  
  def test_design_button(self):
    design_page = HowWeDesignPage(self.driver)
    design_page.close_cookies()
    design_page.click_element_design_button()
    assert 'Design Collections | Meritage Homes' in self.driver.title

  def test_live_header(self):
    design_page = HowWeDesignPage(self.driver)
    header = design_page.get_text_live_header()
    assert 'LiVE.NOW' in header
  
  def test_live_body(self):
    design_page = HowWeDesignPage(self.driver)
    body = design_page.get_elements_live_body()
    assert (
      # first p tag is empty
      'Move sooner' in body[1].text and
      'You can practically smell the fresh paint now' in body[1].text
    )
  
  def test_live_image(self):
    design_page = HowWeDesignPage(self.driver)
    image = design_page.get_element_live_image()
    result = design_page.javascript_image(image)
    assert result
  
  def test_live_button(self):
    design_page = HowWeDesignPage(self.driver)
    design_page.close_cookies()
    design_page.click_element_live_button()
    assert 'LiVE.NOW. | Meritage Homes' in self.driver.title

  @pytest.mark.parametrize('number', [1, 2, 3])
  def test_columns(self, number):
    design_page = HowWeDesignPage(self.driver)
    design_page.close_cookies()
    header = design_page.get_text_column_header(number)
    body = design_page.get_text_column_body(number)
    design_page.click_element_column_button(number)
    match number:
      case 1:
        assert (
          'Home Design Resources' in header and
          'Get the latest interior design trends' in body and
          'New Home Design Inspiration | Meritage Homes' in self.driver.title
        )
      case 2:
        assert (
          'Wakefield Study' in header and
          'After conducting third-party' in body and
          'Wakefield Study| Meritage Homes' in self.driver.title
        )
      case 3:
        assert (
          'Seven Insider House-Hunting Tips' in header and
          'House hunt like the pros' in body 
          # Button link is broken
        )
      
  def tets_asterisk(self):
    design_page = HowWeDesignPage(self.driver)
    text = design_page.get_text_bottom_asterisk()
    assert 'Third-party research of 1,000' in text