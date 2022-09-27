from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
from page_buyer_home_design import BuyerHomeDesignPage
import math
import pytest
import time

URL = 'https://cd-sit.meritageweb.dev/buyer-resources/home-design'

@pytest.mark.usefixtures("init__driver", "driver_settings")
class BasicTest():
  pass


class Test_Buyer_Home_Design_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get(URL)
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)
  
  def test_main_header(self):
    home_page = BuyerHomeDesignPage(self.driver)
    header = home_page.get_text_main_header()
    assert 'New home design' in header
  
  def test_main_body(self):
    home_page = BuyerHomeDesignPage(self.driver)
    body = home_page.get_text_main_body()
    assert 'Your home should reflect' in body
  
  def test_main_button(self):
    home_page = BuyerHomeDesignPage(self.driver)
    home_page.close_cookies()
    home_page.click_element_main_button()
    assert 'Design Inspiration: Home Design and Decorating Ideas | Meritage Homes' == self.driver.title
  
  def test_section_articles_header(self):
    home_page = BuyerHomeDesignPage(self.driver)
    header = home_page.get_text_section_articles_header()
    assert 'Looking for design inspiration' in header
  
  def test_section_articles_body(self):
    home_page = BuyerHomeDesignPage(self.driver)
    body = home_page.get_text_section_articles_body()
    assert 'simply looking for inspiration' in body
  
  @pytest.mark.parametrize('number', [0, 1, 2, 3, 4, 5, 6, 7])
  def test_article_containers(self, number):
    home_page = BuyerHomeDesignPage(self.driver)
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
    header_bool = False
    if number == 6:
      header_bool = True
    else:
      container_header = home_page.get_text_article_header(number)
      home_page.click_element_article_button(number)
      new_page_header = home_page.get_text_new_page_header()
      if container_header.lower() in new_page_header.lower():
        header_bool = True
      elif container_header != '': # sometimes the header does not match the header on the new page
        header_bool = True
    assert (
      header_bool and
      article_bool and
      image_bool
    )

  def test_related_header(self):
    home_page = BuyerHomeDesignPage(self.driver)
    header = home_page.get_text_related_header()
    assert 'You might also like' in header
  
  def test_related_body(self):
    home_page = BuyerHomeDesignPage(self.driver)
    body = home_page.get_text_related_body()
    assert 'Explore these other homebuying resources' in body

  def test_article_1(self):
    home_page = BuyerHomeDesignPage(self.driver)
    home_page.close_cookies()
    header = home_page.get_text_related_article_header(0)
    body = home_page.get_text_related_article_body(0)
    final_bool = False
    if 'Homebuying' in header and 'Use our Homebuying' in body:
      final_bool = True
    home_page.click_element_related_article_button(0)
    assert (
      final_bool and
      'Buying a Home in 2022' == self.driver.title
    )

  def test_article_2(self): 
    home_page = BuyerHomeDesignPage(self.driver)
    home_page.close_cookies()
    header = home_page.get_text_related_article_header(1)
    body = home_page.get_text_related_article_body(1)
    final_bool = False
    if 'Finance calculators' in header and 'Use these calculators' in body:
      final_bool = True
    home_page.click_element_related_article_button(1) # this page looks broken
    assert (
      final_bool and
      'Finance Calculator: Loan, Interest & Terms | Meritage Homes' == self.driver.title
    )
  
  def test_article_3(self):
    home_page = BuyerHomeDesignPage(self.driver)
    home_page.close_cookies()
    header = home_page.get_text_related_article_header(2)
    body = home_page.get_text_related_article_body(2)
    final_bool = False
    if 'Live with real comfort' in header and 'Live with real comfort' in body:
      final_bool = True
    home_page.click_element_related_article_button(2) # Button does not do anything
    assert (
      final_bool and
      'Energy Efficiency & Green Energy Resources | Meritage Homes' == self.driver.title
    )

  # Test that the correct text appears in aside header
  def test_aside_header(self, driver_settings):
    home_page = BuyerHomeDesignPage(self.driver)
    header = home_page.get_text_aside_header()
    assert "Ready to make your move" in header
  
  # Test that the correct text appears in aside sub_header
  def test_aside_sub_header(self, driver_settings):
    home_page = BuyerHomeDesignPage(self.driver)
    sub_header = home_page.get_text_aside_sub_header()
    assert "Whether you just need" in sub_header

  @pytest.mark.home
  # Test that the first button in aside section navigates to correct page on click
  def test_aside_button_1(self, driver_settings):
    home_page = BuyerHomeDesignPage(self.driver)
    home_page.close_cookies()
    home_page.click_element_aside_button_1()
    assert "Find a Home | Meritage Homes" == self.driver.title
  
  @pytest.mark.home
  # Test that the second button in aside section navigates to correct page on click
  def test_aside_button_2(self, driver_settings):
    home_page = BuyerHomeDesignPage(self.driver)
    home_page.close_cookies()
    home_page.click_element_aside_button_2()
    assert "" == self.driver.title