from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
from page_terms_of_use import TermsOfUsePage
import math
import pytest
import time

URL = 'https://cd-sit.meritageweb.dev/terms-of-use'

@pytest.mark.usefixtures("init__driver", "driver_settings")
class BasicTest():
  pass


class Test_Terms_Of_Use_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get(URL)
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)

  # I think the header is wrong on this page
  def test_main_header(self):
    terms_page = TermsOfUsePage(self.driver)
    header = terms_page.get_text_main_header()
    assert 'Meritage Homes Media' in header
  
  def test_page_headers(self):
    terms_page = TermsOfUsePage(self.driver)
    headers = terms_page.get_elements_headers()
    assert (
      'Acceptance' in headers[0] and
      'Privacy' in headers[1] and
      'Conduct' in headers[2] and
      'Termination of Access' in headers[3] and
      'Intellectual Property Rights' in headers[4] and
      'Linking to the Site' in headers[5] and
      'Indemnification' in headers[6] and
      'Disclaimers' in headers[7] and
      'Limitation of Liability' in headers[8] and
      'Links' in headers[9] and
      'Forward-Looking Statements' in headers[10] and
      'Miscellaneous' in headers[11]
    )
  
  def test_still_have_questions_header(self):
    terms_page = TermsOfUsePage(self.driver)
    header = terms_page.get_text_still_have_questions_header()
    assert 'Still have questions' in header

  def test_still_have_questions_body(self):
    terms_page = TermsOfUsePage(self.driver)
    body = terms_page.get_text_still_have_questions_body()
    assert 'We have a home expert' in body
  
  def test_still_have_questions_button_1(self):
    terms_page = TermsOfUsePage(self.driver)
    terms_page.close_cookies()
    terms_page.click_element_still_have_questions_button_1()
    assert 'Meritage Live Chat | Meritage Homes' == self.driver.title
  
  def test_still_have_questions_button_2(self):
    terms_page = TermsOfUsePage(self.driver)
    terms_page.close_cookies()
    terms_page.click_element_still_have_questions_button_2()
    assert '' == self.driver.title