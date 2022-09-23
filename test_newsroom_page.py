from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
from page_newsroom import NewsroomPage
from page_base import BasePage
import math
import pytest
import time

URL = 'https://cd-sit.meritageweb.dev/company/newsroom'

@pytest.mark.usefixtures("init__driver", "driver_settings")
class BasicTest():
  pass


class Test_Newsroom_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get(URL)
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)
  
  def test_main_header(self):
    newsroom_page = NewsroomPage(self.driver)
    header = newsroom_page.get_text_main_header()
    assert 'Meritage Homes Newsroom' in header
  
  def test_media_resources_header(self):
    newsroom_page = NewsroomPage(self.driver)
    header = newsroom_page.get_text_media_resources_header()
    assert 'Media Resources' in header
  
  def test_media_resources_body(self):
    newsroom_page = NewsroomPage(self.driver)
    body = newsroom_page.get_text_media_resources_body()
    assert 'a media professional' in body
  
  def test_download_header(self):
    newsroom_page = NewsroomPage(self.driver)
    header = newsroom_page.get_text_download_header()
    assert 'Download' in header

  def test_download_body(self):
    newsroom_page = NewsroomPage(self.driver)
    body = newsroom_page.get_text_download_body()
    assert (
      'Browse our' in body[1] and
      'By clicking' in body[2]
    )

  def test_download_image(self):
    newsroom_page = NewsroomPage(self.driver)
    image = newsroom_page.get_element_download_image()
    result = newsroom_page.javascript_image(image)
    assert result
  
  def test_download_button(self):
    newsroom_page = NewsroomPage(self.driver)
    newsroom_page.close_cookies()
    newsroom_page.click_element_download_button()
    assert 'PowerPoint Presentation - Meritage_Media_Kit_2018.pdf' or 'PDF.js viewer' == self.driver.title
  
  def test_latest_header(self):
    newsroom_page = NewsroomPage(self.driver)
    header = newsroom_page.get_text_latest_header()
    assert 'latest' in header

  def test_latest_body(self):
    newsroom_page = NewsroomPage(self.driver)
    body = newsroom_page.get_text_latest_body()
    assert 'Check here for the latest' in body

  def test_latest_image(self):
    newsroom_page = NewsroomPage(self.driver)
    image = newsroom_page.get_element_latest_image()
    result = newsroom_page.javascript_image(image)
    assert result
  
  @pytest.mark.news
  def test_latest_button(self):
    newsroom_page = NewsroomPage(self.driver)
    newsroom_page.close_cookies()
    newsroom_page.click_element_latest_button()
    assert 'Investor Relations :: Meritage Homes Corporation (MTH)' == self.driver.title

  def test_headlines_header(self):
    newsroom_page = NewsroomPage(self.driver)
    header = newsroom_page.get_text_headlines_header()
    assert 'headlines' in header

  def test_headlines_body(self):
    newsroom_page = NewsroomPage(self.driver)
    body = newsroom_page.get_text_headlines_body()
    assert 'just take our word' in body

  def test_headlines_image(self):
    newsroom_page = NewsroomPage(self.driver)
    image = newsroom_page.get_element_headlines_image()
    result = newsroom_page.javascript_image(image)
    assert result
    
  def test_headlines_button(self):
    newsroom_page = NewsroomPage(self.driver)
    newsroom_page.close_cookies()
    newsroom_page.click_element_headlines_button()
    assert 'Headlines' == self.driver.title
  
  def test_logos_header(self):
    newsroom_page = NewsroomPage(self.driver)
    header = newsroom_page.get_text_logos_header()
    assert 'logos' in header

  def test_logos_body(self):
    newsroom_page = NewsroomPage(self.driver)
    body = newsroom_page.get_text_logos_body()
    assert 'Find high-resolution' in body

  def test_logos_image(self):
    newsroom_page = NewsroomPage(self.driver)
    image = newsroom_page.get_element_logos_image()
    result = newsroom_page.javascript_image(image)
    assert result
  
  def test_answer_questions_header(self):
    newsroom_page = NewsroomPage(self.driver)
    header = newsroom_page.get_text_answer_questions_header()
    assert 'answer your questions' in header

  def test_answer_questions_body(self):
    newsroom_page = NewsroomPage(self.driver)
    body = newsroom_page.get_text_answer_questions_body()
    assert 'Need more information' in body
  
  def test_answer_questions_button(self):
    newsroom_page = NewsroomPage(self.driver)
    newsroom_page.close_cookies()
    newsroom_page.click_element_answer_questions_button()
    assert '' == self.driver.title