from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
from page_homebuying import HomebuyingPage
import math
import pytest
import time

URL = 'https://www.meritagehomes.com/buyer-resources/homebuying'

@pytest.mark.usefixtures("init__driver", "driver_settings")
class BasicTest():
  pass


class Test_Homebuying_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get(URL)
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)
  
  def test_main_header(self):
    home_page = HomebuyingPage(self.driver)
    header = home_page.get_text_main_header()
    assert 'Homebuying 101' in header
  
  def test_main_body(self):
    home_page = HomebuyingPage(self.driver)
    body = home_page.get_text_main_body()
    assert 'Use our Homebuying 101 guide' in body
  
  def test_main_button(self):
    home_page = HomebuyingPage(self.driver)
    home_page.close_cookies()
    home_page.click_element_main_button()
    assert 'Buying a Home in 2022' == self.driver.title
  
  def test_section_articles_header(self):
    home_page = HomebuyingPage(self.driver)
    header = home_page.get_text_section_articles_header()
    assert 'Become a homebuying pro' in header
  
  def test_section_articles_body(self):
    home_page = HomebuyingPage(self.driver)
    body = home_page.get_text_section_articles_body()
    assert 'just starting your search' in body
  
  def test_show_more_button(self):
    home_page = HomebuyingPage(self.driver)
    home_page.close_cookies()
    old_active_articles = home_page.get_elements_active_articles()
    home_page.click_element_show_more_button()
    new_active_articles = home_page.get_elements_active_articles()
    assert len(old_active_articles) < len(new_active_articles)
  
  @pytest.mark.parametrize('number', [0, 1, 2, 3, 4, 5, 6, 7])
  def test_article_containers(self, number):
    home_page = HomebuyingPage(self.driver)
    home_page.close_cookies()
    # Ensure article span appears in container
    article_element_text =  home_page.get_text_article_article(number)
    article_bool = False
    if 'Article' == article_element_text:
      article_bool = True
    # Ensure image appears in container
    image_bool = False
    article_image = home_page.get_element_article_image(number)
    result = home_page.javascript_image(article_image)
    if result:
      image_bool = True
    # Make sure the container header mathces with the header in the navigation page
    container_header = home_page.get_text_article_header(number)
    home_page.click_element_article_button(number)
    new_page_header = home_page.get_text_new_page_header()
    assert (
      container_header.lower() in new_page_header.lower() and
      article_bool and
      image_bool
    )

  def test_related_header(self):
    home_page = HomebuyingPage(self.driver)
    header = home_page.get_text_related_header()
    assert 'You might also like' in header
  
  def test_related_body(self):
    home_page = HomebuyingPage(self.driver)
    body = home_page.get_text_related_body()
    assert 'Explore these other homebuying resources' in body

  def test_article_1(self):
    home_page = HomebuyingPage(self.driver)
    home_page.close_cookies()
    header = home_page.get_text_related_article_header(0)
    body = home_page.get_text_related_article_body(0)
    final_bool = False
    if 'Kitchen design trends' in header and 'See how to personalize' in body:
      final_bool = True
    home_page.click_element_related_article_button(0)
    assert (
      final_bool and
      'Kitchens' == self.driver.title
    )

  def test_article_2(self): 
    home_page = HomebuyingPage(self.driver)
    home_page.close_cookies()
    header = home_page.get_text_related_article_header(1)
    body = home_page.get_text_related_article_body(1)
    final_bool = False
    if 'Live with more' in header and 'Start living with more' in body:
      final_bool = True
    home_page.click_element_related_article_button(1) # this page looks broken
    assert (
      final_bool and
      'Live with more savings' == self.driver.title
    )
  
  def test_article_3(self):
    home_page = HomebuyingPage(self.driver)
    home_page.close_cookies()
    header = home_page.get_text_related_article_header(2)
    body = home_page.get_text_related_article_body(2)
    final_bool = False
    if 'Guide to financing' in header and 'Ready to make your move' in body:
      final_bool = True
    home_page.click_element_related_article_button(2) # Button does not do anything
    assert (
      final_bool and
      'First-Time Homebuying Information & Guides | Meritage Homes' == self.driver.title
    )

  # Test that the correct text appears in aside header
  def test_aside_header(self, driver_settings):
    home_page = HomebuyingPage(self.driver)
    header = home_page.get_text_aside_header()
    assert "Ready to make your move" in header
  
  # Test that the correct text appears in aside sub_header
  def test_aside_sub_header(self, driver_settings):
    home_page = HomebuyingPage(self.driver)
    sub_header = home_page.get_text_aside_sub_header()
    assert "Whether you just need" in sub_header

  @pytest.mark.home
  # Test that the first button in aside section navigates to correct page on click
  def test_aside_button_1(self, driver_settings):
    home_page = HomebuyingPage(self.driver)
    home_page.close_cookies()
    home_page.click_element_aside_button_1()
    assert "Find a Home | Meritage Homes" == self.driver.title
  
  @pytest.mark.home
  # Test that the second button in aside section navigates to correct page on click
  def test_aside_button_2(self, driver_settings):
    home_page = HomebuyingPage(self.driver)
    home_page.close_cookies()
    home_page.click_element_aside_button_2()
    assert "" == self.driver.title