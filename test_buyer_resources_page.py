from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
from page_buyer_resources import BuyerResourcesPage
import math
import pytest
import time

URL = 'https://cd-sit.meritageweb.dev/buyer-resources'

@pytest.mark.usefixtures("init__driver", "driver_settings")
class BasicTest():
  pass


class Test_Buyer_Resources_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get(URL)
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)
  
  def test_main_header(self):
    buyer_page = BuyerResourcesPage(self.driver)
    header = buyer_page.get_text_main_header()
    assert 'Buyer resources' in header
  
  def test_main_body(self):
    buyer_page = BuyerResourcesPage(self.driver)
    body = buyer_page.get_text_main_sub_header()
    assert 'Find helpful information' in body
  
  def test_affiliates_header(self):
    buyer_page = BuyerResourcesPage(self.driver)
    header = buyer_page.get_text_affiliates_header()
    assert 'Meet our preferred affiliates' in header
  
  def test_affiliates_body(self):
    buyer_page = BuyerResourcesPage(self.driver)
    body = buyer_page.get_text_affiliates_body()
    assert 'Learn more about the Meritage' in body
  
  def test_affiliate_image_1(self):
    buyer_page = BuyerResourcesPage(self.driver)
    buyer_page.close_cookies()
    image = buyer_page.get_element_affiliates_image(1)
    result = buyer_page.javascript_image(image)
    buyer_page.click_element_affiliates_image(1)
    assert (
      'Affiliated Providers | Meritage Homes' == self.driver.title and
      result
    )
  
  def test_affiliate_image_2(self):
    buyer_page = BuyerResourcesPage(self.driver)
    buyer_page.close_cookies()
    image = buyer_page.get_element_affiliates_image(2)
    result = buyer_page.javascript_image(image)
    buyer_page.click_element_affiliates_image(2)
    assert (
      'Affiliated Providers | Meritage Homes' == self.driver.title and
      result
    )
  
  def test_affiliate_image_3(self):
    buyer_page = BuyerResourcesPage(self.driver)
    buyer_page.close_cookies()
    image = buyer_page.get_element_affiliates_image(3)
    result = buyer_page.javascript_image(image)
    buyer_page.click_element_affiliates_image(3)
    assert (
      'Affiliated Providers | Meritage Homes' == self.driver.title and
      result
    )
  
  def test_homebuying_header(self):
    buyer_page = BuyerResourcesPage(self.driver)
    header = buyer_page.get_text_homebuying_header()
    assert 'Homebuying process' in header

  def test_homebuying_body(self):
    buyer_page = BuyerResourcesPage(self.driver)
    body = buyer_page.get_text_homebuying_body()
    assert 'From deciding on a new home' in body

  def test_homebuying_button(self):
    buyer_page = BuyerResourcesPage(self.driver)
    buyer_page.close_cookies()
    buyer_page.click_element_homebuying_button()
    assert 'First-Time Homebuying Information & Guides | Meritage Homes' == self.driver.title
  
  def test_homebuying_container_1(self):
    buyer_page = BuyerResourcesPage(self.driver)
    buyer_page.close_cookies()
    header = buyer_page.get_text_homebuying_container_1_header()
    body = buyer_page.get_text_homebuying_container_1_body()
    image = buyer_page.get_element_homebuying_image_1()
    image_result = buyer_page.javascript_image(image)
    final_assert = False
    if ('Homebuying 101 Guide' in header) and ('Use our Homebuying' in body) and image_result:
      final_assert = True
    buyer_page.click_element_homebuying_image_1()
    assert (
      final_assert and
      'First-Time Homebuying Information & Guides | Meritage Homes' in self.driver.title
    )
  
  def test_homebuying_container_2(self):
    buyer_page = BuyerResourcesPage(self.driver)
    buyer_page.close_cookies()
    header = buyer_page.get_text_homebuying_container_2_header()
    body = buyer_page.get_text_homebuying_container_2_body()
    image = buyer_page.get_element_homebuying_image_2()
    image_result = buyer_page.javascript_image(image)
    final_assert = False
    if ('Tour a Meritage home' in header) and ('Considering a new community' in body) and image_result:
      final_assert = True
    buyer_page.click_element_homebuying_image_2()
    assert (
      final_assert and
      'Tour A Meritage Home' in self.driver.title
    )
  
  def test_energy_efficiency_header(self):
    buyer_page = BuyerResourcesPage(self.driver)
    header = buyer_page.get_text_energy_efficiency_header()
    assert 'Energy efficiency' in header

  def test_energy_efficiency_body(self):
    buyer_page = BuyerResourcesPage(self.driver)
    body = buyer_page.get_text_energy_efficiency_body()
    assert 'Learn about energy-efficient' in body

  def test_energy_efficiency_button(self):
    buyer_page = BuyerResourcesPage(self.driver)
    buyer_page.close_cookies()
    buyer_page.click_element_energy_efficiency_button()
    assert 'Energy Efficiency & Green Energy Resources | Meritage Homes' == self.driver.title
  
  def test_energy_efficiency_container_1(self):
    buyer_page = BuyerResourcesPage(self.driver)
    buyer_page.close_cookies()
    header = buyer_page.get_text_energy_efficiency_container_1_header()
    body = buyer_page.get_text_energy_efficiency_container_1_body()
    image = buyer_page.get_element_energy_efficiency_image_1()
    image_result = buyer_page.javascript_image(image)
    final_assert = False
    if ('Live with more savings' in header) and ('time to start living' in body) and image_result:
      final_assert = True
    buyer_page.click_element_energy_efficiency_image_1()
    assert (
      final_assert and
      'Energy Efficiency & Green Energy Resources | Meritage Homes' in self.driver.title
    )
  
  def test_energy_efficiency_container_2(self):
    buyer_page = BuyerResourcesPage(self.driver)
    buyer_page.close_cookies()
    header = buyer_page.get_text_energy_efficiency_container_2_header()
    body = buyer_page.get_text_energy_efficiency_container_2_body()
    image = buyer_page.get_element_energy_efficiency_image_2()
    image_result = buyer_page.javascript_image(image)
    final_assert = False
    if ('Live with real comfort' in header) and ('See how energy efficiency' in body) and image_result:
      final_assert = True
    buyer_page.click_element_energy_efficiency_image_2()
    assert (
      final_assert and
      'Energy Efficiency & Green Energy Resources | Meritage Homes' in self.driver.title
    )
  
  def test_home_design_header(self):
    buyer_page = BuyerResourcesPage(self.driver)
    header = buyer_page.get_text_home_design_header()
    assert 'Home design' in header

  def test_home_design_body(self):
    buyer_page = BuyerResourcesPage(self.driver)
    body = buyer_page.get_text_home_design_body()
    assert 'See resources to tap' in body

  def test_home_design_button(self):
    buyer_page = BuyerResourcesPage(self.driver)
    buyer_page.close_cookies()
    buyer_page.click_element_home_design_button()
    assert 'New Home Design Inspiration | Meritage Homes' == self.driver.title
  
  def test_home_design_container_1(self):
    buyer_page = BuyerResourcesPage(self.driver)
    buyer_page.close_cookies()
    header = buyer_page.get_text_home_design_container_1_header()
    body = buyer_page.get_text_home_design_container_1_body()
    image = buyer_page.get_element_home_design_image_1()
    image_result = buyer_page.javascript_image(image)
    final_assert = False
    if ('Bathroom design trends' in header) and ('Explore bathroom' in body) and image_result:
      final_assert = True
    buyer_page.click_element_home_design_image_1()
    assert (
      final_assert and
      'Design Inspiration: Home Design and Decorating Ideas | Meritage Homes' in self.driver.title
    )
  
  def test_home_design_container_2(self):
    buyer_page = BuyerResourcesPage(self.driver)
    buyer_page.close_cookies()
    header = buyer_page.get_text_home_design_container_2_header()
    body = buyer_page.get_text_home_design_container_2_body()
    image = buyer_page.get_element_home_design_image_2()
    image_result = buyer_page.javascript_image(image)
    final_assert = False
    if ('Kitchen design trends' in header) and ('See how to personalize' in body) and image_result:
      final_assert = True
    buyer_page.click_element_home_design_image_2()
    assert (
      final_assert and
      'Design Inspiration: Home Design and Decorating Ideas | Meritage Homes' in self.driver.title
    )
  
  def test_ready_header(self):
    buyer_page = BuyerResourcesPage(self.driver)
    header = buyer_page.get_ready_to_find_header()
    assert 'Ready to find your home' in header
  
  def test_ready_body(self):
    buyer_page = BuyerResourcesPage(self.driver)
    body = buyer_page.get_ready_to_find_body()
    assert 'There are many great homes' in body
  
  def test_ready_button(self):
    buyer_page = BuyerResourcesPage(self.driver)
    buyer_page.close_cookies()
    buyer_page.click_element_ready_to_find_button()
    assert '' == self.driver.title