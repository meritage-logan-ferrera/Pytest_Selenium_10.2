from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
from page_privacy_policy import PrivacyPolicyPage
from page_base import BasePage
import math
import pytest
import time

URL = 'https://cd-sit.meritageweb.dev/about-us/privacy-policy'

@pytest.mark.usefixtures("init__driver", "driver_settings")
class BasicTest():
  pass


class Test_Privacy_Policy_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get(URL)
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)

  def test_main_header(self):
    privacy_page = PrivacyPolicyPage(self.driver)
    header = privacy_page.get_text_main_header()
    assert 'Meritage Homes Privacy Notice' in header
  
  def test_page_headers(self):
    privacy_page = PrivacyPolicyPage(self.driver)
    headers = privacy_page.get_elements_headers()
    assert (
      'Definitions' in headers[0] and
      'Collecting Personal Information' in headers[1] and
      'Information Company Collects' in headers[2] and
      'Cookies' in headers[3] and
      'Sources of Personal Information' in headers[4] and
      'Who is Collecting Information' in headers[5] and
      'More Information About Why We Collect Information' in headers[6] and
      'Sharing Personal Information' in headers[7] and
      'Your Rights and Choices' in headers[8] and
      'Access to Information' in headers[9] and
      'Privacy Rights' in headers[10] and
      'Deletion Request' in headers[11] and
      'Exercising Access' in headers[12] and
      'More Information About' in headers[13] and
      'Security' in headers[14] and
      'Children Under the Age' in headers[15] and
      'Questions, Comments' in headers[16]
    )
  
  def test_image_1(self):
    privacy_page = PrivacyPolicyPage(self.driver)
    image = privacy_page.get_element_image_1()
    result = privacy_page.javascript_image(image)
    assert result
  
  def test_image_2(self):
    privacy_page = PrivacyPolicyPage(self.driver)
    image = privacy_page.get_element_image_2()
    result = privacy_page.javascript_image(image)
    assert result
  
  def test_terms_link(self):
    privacy_page = PrivacyPolicyPage(self.driver)
    privacy_page.close_cookies()
    terms_link = privacy_page.get_element_plain_button_terms()
    result = privacy_page.check_plain_button(terms_link)
    privacy_page.click_element_plain_button_terms()
    assert (
      result and
      'Meritage Homes Terms of Use | Meritage Homes' == self.driver.title
    )
  
  def test_clicking_here_link(self):
    privacy_page = PrivacyPolicyPage(self.driver)
    privacy_page.close_cookies()
    clicking_here_link = privacy_page.get_element_plain_button_clicking_here()
    result = privacy_page.check_plain_button(clicking_here_link)
    privacy_page.click_element_plain_button_clicking_here()
    assert (
      result and
      'NAI Consumer Opt Out' == self.driver.title
    )
  
  def test_visiting_request_link(self):
    privacy_page = PrivacyPolicyPage(self.driver)
    privacy_page.close_cookies()
    visiting_request_link = privacy_page.get_element_plain_button_visiting_request()
    result = privacy_page.check_plain_button(visiting_request_link)
    privacy_page.click_element_plain_button_visiting_request()
    assert (
      result and
      'OneTrust | Privacy Management Software' == self.driver.title
    )
  
  def test_still_have_questions_header(self):
    privacy_page = PrivacyPolicyPage(self.driver)
    header = privacy_page.get_text_still_have_questions_header()
    assert 'Still have questions' in header

  def test_still_have_questions_body(self):
    privacy_page = PrivacyPolicyPage(self.driver)
    body = privacy_page.get_text_still_have_questions_body()
    assert 'Schedule a quick chat' in body
  
  def test_still_have_questions_button(self):
    privacy_page = PrivacyPolicyPage(self.driver)
    privacy_page.close_cookies()
    privacy_page.click_element_still_have_questions_button()
    assert '' == self.driver.title