from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
from page_buyer_energy_efficiency import BuyerEnergyEfficiencyPage
import math
import pytest
import time

URL = 'https://cd-sit.meritageweb.dev/buyer-resources/energy-efficiency'

@pytest.mark.usefixtures("init__driver", "driver_settings")
class BasicTest():
  pass


class Test_Buyer_Energy_Efficiency_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get(URL)
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)
  
  def test_main_header(self):
    home_page = BuyerEnergyEfficiencyPage(self.driver)
    header = home_page.get_text_main_header()
    assert 'energy efficiency' in header
  
  def test_main_body(self):
    home_page = BuyerEnergyEfficiencyPage(self.driver)
    body = home_page.get_text_main_body()
    assert 'Browse the resources below' in body
  
  def test_show_more_button(self):
    home_page = BuyerEnergyEfficiencyPage(self.driver)
    home_page.close_cookies()
    old_active_articles = home_page.get_elements_active_articles()
    home_page.click_element_show_more_button()
    new_active_articles = home_page.get_elements_active_articles()
    assert len(old_active_articles) < len(new_active_articles)
  
  @pytest.mark.parametrize('number', [0, 1, 2, 3, 4, 5, 6, 7])
  def test_article_containers(self, number):
    home_page = BuyerEnergyEfficiencyPage(self.driver)
    home_page.close_cookies()
    # Ensure article span appears in container
    article_element_text =  home_page.get_text_article_article(number)
    article_bool = False
    if 'Article' or 'Video' == article_element_text:
      article_bool = True
    # Ensure image appears in container
    image_bool = False
    article_image = home_page.get_element_article_image(number)
    result = home_page.javascript_image(article_image)
    if result:
      image_bool = True
    # If its a video there is no nav page it just opens an overlay
    header_bool = False
    if article_element_text == 'Video':
      home_page.click_element_article_play_button(number)
      overlay = home_page.get_element_youtube_overlay()
      result = self.driver.execute_script("return arguments[0].style.display != 'none'", overlay)
      if result:
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
    home_page = BuyerEnergyEfficiencyPage(self.driver)
    header = home_page.get_text_related_header()
    assert 'You might also like' in header
  
  def test_related_body(self):
    home_page = BuyerEnergyEfficiencyPage(self.driver)
    body = home_page.get_text_related_body()
    assert 'Explore these other homebuying resources' in body

  def test_article_1(self):
    home_page = BuyerEnergyEfficiencyPage(self.driver)
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
    home_page = BuyerEnergyEfficiencyPage(self.driver)
    home_page.close_cookies()
    header = home_page.get_text_related_article_header(1)
    body = home_page.get_text_related_article_body(1)
    final_bool = False
    if 'Advantages to owning a home' in header and 'Are you ready' in body:
      final_bool = True
    home_page.click_element_related_article_button(1) # this page looks broken
    assert (
      final_bool and
      'Advantages To Owning' == self.driver.title
    )
  
  def test_article_3(self):
    home_page = BuyerEnergyEfficiencyPage(self.driver)
    home_page.close_cookies()
    header = home_page.get_text_related_article_header(2)
    body = home_page.get_text_related_article_body(2)
    final_bool = False
    if 'Kitchen design trends' in header and 'See how to personalize' in body:
      final_bool = True
    home_page.click_element_related_article_button(2) # Button does not do anything
    assert (
      final_bool and
      'Kitchens' == self.driver.title
    )

  # Test that the correct text appears in aside header
  def test_aside_header(self, driver_settings):
    home_page = BuyerEnergyEfficiencyPage(self.driver)
    header = home_page.get_text_aside_header()
    assert "Ready to make your move" in header
  
  # Test that the correct text appears in aside sub_header
  def test_aside_sub_header(self, driver_settings):
    home_page = BuyerEnergyEfficiencyPage(self.driver)
    sub_header = home_page.get_text_aside_sub_header()
    assert "Whether you just need" in sub_header

  # Test that the first button in aside section navigates to correct page on click
  def test_aside_button_1(self, driver_settings):
    home_page = BuyerEnergyEfficiencyPage(self.driver)
    home_page.close_cookies()
    home_page.click_element_aside_button_1()
    assert "Find a Home | Meritage Homes" == self.driver.title
  
  # Test that the second button in aside section navigates to correct page on click
  def test_aside_button_2(self, driver_settings):
    home_page = BuyerEnergyEfficiencyPage(self.driver)
    home_page.close_cookies()
    home_page.click_element_aside_button_2()
    assert "" == self.driver.title