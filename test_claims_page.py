from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
from page_claims import ClaimsPage
import math
import pytest
import time

URL = 'https://cd-sit.meritageweb.dev/claims'

@pytest.mark.usefixtures("init__driver", "driver_settings")
class BasicTest():
  pass


class Test_Claims_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get(URL)
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)
  
  def test_main_header(self):
    claims_page = ClaimsPage(self.driver)
    header = claims_page.get_text_main_header()
    assert 'Claims' in header
  
  def test_header_link_1(self):
    claims_page = ClaimsPage(self.driver)
    claims_page.close_cookies()
    link_1 = claims_page.get_element_header_link_1()
    plain_result = claims_page.check_plain_button(link_1)
    claims_page.click_element_header_link_1()
    scroll_result = self.driver.execute_script("return window.scrollY != 0")
    assert (
      plain_result and
      scroll_result
    )
  
  def test_header_link_2(self):
    claims_page = ClaimsPage(self.driver)
    claims_page.close_cookies()
    link_2 = claims_page.get_element_header_link_2()
    plain_result = claims_page.check_plain_button(link_2)
    claims_page.click_element_header_link_2()
    scroll_result = self.driver.execute_script("return window.scrollY != 0")
    assert (
      plain_result and
      scroll_result
    )
  
  def test_article_1_header(self):
    claims_page = ClaimsPage(self.driver)
    header = claims_page.get_text_article_1_header()
    assert 'Energy-efficient features claims' in header

  def test_article_1_links(self):
    claims_page = ClaimsPage(self.driver)
    links = claims_page.get_elements_article_1_links()
    final_result = False
    for i in range(len(links)):
      result = claims_page.check_plain_button(links[i])
      if result:
        final_result = True
        continue
      else:
        assert False
    assert final_result
  
  def test_article_1_headers(self):
    claims_page = ClaimsPage(self.driver)
    headers = claims_page.get_elements_article_1_headers()
    assert (
      '92% High' in headers[0] and
      'Advanced building' in headers[1] and
      'Advanced framing' in headers[2] and
      'Advanced thermostat' in headers[3] and
      'Air filtration' in headers[4] and
      'All-season windows' in headers[5] and
      'CFL light bulbs' in headers[6] and
      'Climate-sealed' in headers[7] and
      'Conditioned attics' in headers[8] and
      'Dual-actuated' in headers[9] and
      'Energy-efficient' in headers[10] and
      'Dishwasher' in headers[11] and
      'certified homes' in headers[12] and
      'Partner of the Year' in headers[13] and
      'EPA' in headers[14] and
      'Flow-smart' in headers[15] and
      'Fresh air management' in headers[16] and
      'Health-promoting barrier' in headers[17] and
      'Healthier building materials' in headers[18] and
      'High-performance' in headers[19] and
      'HERS' in headers[20] and
      'Humidistat' in headers[21] and
      'HVAC' in headers[22] and
      'Indoor airPLUS' in headers[23] and
      'Insulated garage' in headers[24] and
      'LED' in headers[25] and
      'Low-E' in headers[26] and
      'Low to zero VOC' in headers[27] and
      'MERV 8' in headers[28] and
      'MERV 11' in headers[29] and
      'NET ZERO' in headers[30] and
      'PEX' in headers[31] and
      'Remote home' in headers[32] and
      'Sealed insulated' in headers[33] and
      'SEER 14 HVAC' in headers[34] and
      'SEER 15' in headers[35] and
      'SEER 16' in headers[36] and
      'Solar energy' in headers[37] and
      'Spray foam insulated attics' in headers[38] and
      'insulation' in headers[39] and
      'Tankless' in headers[40] and
      'Temperature' in headers[41] and
      'Thermal breaks' in headers[42] and
      'faucets' in headers[43] and
      'WaterSense' in headers[44] and
      'irrigation' in headers[45] and
      'Whole-home' in headers[46] and
      'Water-saving' in headers[47]
    )
  
  def test_article_2_header(self):
    claims_page = ClaimsPage(self.driver)
    header = claims_page.get_text_article_2_header()
    assert 'General Energy Claims' in header

  def test_article_2_links(self):
    claims_page = ClaimsPage(self.driver)
    links = claims_page.get_elements_article_2_links()
    final_result = False
    for i in range(len(links)):
      result = claims_page.check_plain_button(links[i])
      if result:
        final_result = True
        continue
      else:
        assert False
    assert final_result
  
  def test_article_2_headers(self):
    claims_page = ClaimsPage(self.driver)
    headers = claims_page.get_elements_article_2_headers()
    assert (
      'Live with Peace of Mind' in headers[0] and
      'Meritage Homes is the First NET ZERO' in headers[1] and
      'Twice as energy-efficient' in headers[2] and
      'Setting the new standard' in headers[3]
    )
  
  def test_looking_for_help_header(self):
    claims_page = ClaimsPage(self.driver)
    header = claims_page.get_text_looking_for_help_header()
    assert 'Looking for help' in header

  def test_looking_for_help_body(self):
    claims_page = ClaimsPage(self.driver)
    body = claims_page.get_text_looking_for_help_body()
    assert 'No matter the question' in body
  
  def test_looking_for_help_button_1(self):
    claims_page = ClaimsPage(self.driver)
    claims_page.close_cookies()
    claims_page.click_element_looking_for_help_button_1()
    assert 'Meritage Live Chat | Meritage Homes' == self.driver.title
  
  def test_looking_for_help_button_2(self):
    claims_page = ClaimsPage(self.driver)
    claims_page.close_cookies()
    claims_page.click_element_looking_for_help_button_2()
    assert '' == self.driver.title

  def test_discliamer(self):
    claims_page = ClaimsPage(self.driver)
    disclaimer = claims_page.get_text_disclaimer()
    assert 'Not all features are standard or available' in disclaimer
