from ast import match_case
from pickletools import ArgumentDescriptor
from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
from page_agents import AgentsPage
from page_base import BasePage
import math
import pytest
import time

URL = 'https://www.meritagehomes.com/agents'

@pytest.mark.usefixtures("init__driver")
class BasicTest():
  pass

class Test_Agents_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get(URL)
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)
  
  def test_main_header(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    header = agents_page.get_text_main_header()
    assert 'kind of a big deal' in header
  
  def test_main_sub_header(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    sub_header = agents_page.get_text_main_sub_header()
    assert 'Thanks for really rocking it' in sub_header
  
  def test_main_button_1(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    html = agents_page.get_html()
    agents_page.close_cookies()
    agents_page.click_elemenet_main_button_1()
    result = self.driver.execute_script("return arguments[0].scrollTop > 100", html)
    assert result
  
  def test_main_button_2(self, driver_settings):
    agents_page = AgentsPage(self.driver)
    html = agents_page.get_html()
    agents_page.close_cookies()
    agents_page.click_elemenet_main_button_2()
    result = self.driver.execute_script("return arguments[0].scrollTop > 100", html)
    assert result
  
  def test_aside_1_header(self):
    agents_page = AgentsPage(self.driver)
    header = agents_page.get_text_aside_1_header()
    assert 'When you sell with us' in header
  
  def test_aside_1_body(self):
    agents_page = AgentsPage(self.driver)
    body = agents_page.get_text_aside_1_body()
    assert 'Watching you hand over the keys to' in body
  
  def test_aside_1_image(self):
    agents_page = AgentsPage(self.driver)
    image = agents_page.get_element_aside_1_image()
    result = self.drive.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", image)
    assert result
  
  @pytest.mark.parametrize('container', [1, 2, 3, 4, 5])
  def test_article_1_containers(self, container, driver_settings):
    agents_page = AgentsPage(self.driver)
    header = agents_page.get_text_article_1_container_header(container)
    body = agents_page.get_text_article_1_container_body(container)
    image = agents_page.get_element_article_1_container_image(container)
    result = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", image)
    match container:
      case 1:
        assert (
          'advanced commission' in header and
          'not too good to be true' in body and
          result
        )
      case 2:
        assert (
          'Enjoy exciting local perks' in header and
          'Earn local perks' in body and
          result
        )
      case 3:
        assert (
          'Regular updates to keep you in the loop' in header and
          'here to help you succeed' in body and
          result
        )
      case 4:
        assert (
          'Register your clients online or by phone' in header and
          'Create an account below to register your clients' in body and
          result
        )
      case 5:
        assert (
          'Tutorials on how to best sell new homes' in header and
          'Knowledge is power' in body and
          result
        )
      
    # Up to Learn more about Agetns Rock
  