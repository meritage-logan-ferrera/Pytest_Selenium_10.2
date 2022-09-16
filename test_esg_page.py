from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
from page_meritage_cares import MeritageCaresPage
from page_esg import ESGPage
import math
import pytest
import time

URL = 'https://www.meritagehomes.com/esg'

@pytest.mark.usefixtures("init__driver")
class BasicTest():
  pass

class Test_ESG_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get(URL)
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)
  
  # Test whether correct text appears in main header of ESG page
  def test_main_header(self, driver_settings):
    esg_page = ESGPage(self.driver)
    header = esg_page.get_text_main_header()
    assert 'Environmental, Social & Governance' in header
  
  # Test whether correct header appears in aside
  def test_aside_body(self, driver_settings):
    esg_page = ESGPage(self.driver)
    body = esg_page.get_elements_aside_body()
    assert (
      'one of the top national public builders' in body[0].text and
      'board of directors' in body[1].text
    )
  
  # Test whether button in first aside section navigates to correct page when clicked
  @pytest.mark.esg
  def test_aside_button(self, driver_settings):
    esg_page = ESGPage(self.driver)
    esg_page.close_cookies()
    esg_page.click_element_aside_button()
    assert 'ESG Reports :: Meritage Homes Corporation (MTH)' == self.driver.title
  
  # Test whether the correct image appears in environmental section
  def test_environmental_image(self, driver_settings):
    esg_page = ESGPage(self.driver)
    image = esg_page.get_element_environmental_image()
    result = esg_page.javascript_image(image)
    assert result
  
  # Test whether the correct body text appears in environmental section
  def test_environmental_body(self, driver_settings):
    esg_page = ESGPage(self.driver)
    body = esg_page.get_elements_environmental_body()
    assert (
      'A Commitment to Building Better' in body[0].text and
      'At Meritage Homes, we look to improve upon our environmental stewardship' in body[1].text and
      'The US EPA' in body[2].text
    )
  
  # Test whether the correct header appears in environmental section
  def test_environmental_header(self, driver_settings):
    esg_page = ESGPage(self.driver)
    header = esg_page.get_text_environmental_header()
    assert 'Environmental' in header
  
  # Test whether button in environmental section navigates to correct page when clicked
  @pytest.mark.esg
  def test_environmental_button(self, driver_settings):
    esg_page = ESGPage(self.driver)
    esg_page.close_cookies()
    esg_page.click_element_environmental_button()
    assert 'Best Home Builders for Energy Efficient Homes | Meritage Homes' in self.driver.title
  
  # Test whether the correct image appears in social corporate section
  def test_social_corporate_image(self, driver_settings):
    esg_page = ESGPage(self.driver)
    image = esg_page.get_element_social_corporate_image()
    result = esg_page.javascript_image(image)
    assert result
  
  # Test whether the correct body text appears in "Social: Corporate Social Responsibility" section
  def test_social_corporate_body(self, driver_settings):
    esg_page = ESGPage(self.driver)
    body = esg_page.get_elements_social_corporate_body()
    assert (
      'A Commitment to Our Employees' in body[0].text and
      'approach to corporate social responsibility focuses on enhancing an inclusive culture' in body[1].text and
      'Meritage Homes CEO, Phillippe Lord, signed' in body[2].text and
      'As a proud founding partner' in body[3].text and
      'We are proud of the diversity in our team' in body[4].text
    )
  
  # Test whether the correct header appears in "Social: Corporate Social Responsibility" section
  def test_social_corporate_header(self, driver_settings):
    esg_page = ESGPage(self.driver)
    header = esg_page.get_text_social_corporate_header()
    assert 'Social: Corporate' in header
  
  # Test whether button in "Social: Corporate Social Responsibility" section navigates to correct page when clicked
  @pytest.mark.esg
  def test_social_corporate_button(self, driver_settings):
    esg_page = ESGPage(self.driver)
    esg_page.close_cookies()
    esg_page.click_element_social_corporate_button()
    assert 'Meritage Homes Announces Commitments to Advance Diversity, Equity and Inclusion :: Meritage Homes Corporation (MTH)' == self.driver.title
  
  # Test whether the correct image appears in "Social: Service & Philanthropy" section
  def test_social_philanthropy_image(self, driver_settings):
    esg_page = ESGPage(self.driver)
    image = esg_page.get_element_social_philanthropy_image()
    result = esg_page.javascript_image(image)
    assert result
  
  # Test whether the correct body text appears in "Social: Service & Philanthropy" section
  @pytest.mark.esg
  def test_social_philanthropy_body(self, driver_settings):
    esg_page = ESGPage(self.driver)
    body = esg_page.get_elements_social_philanthropy_body()
    assert (
      'A Commitment to Community' in body[0].text and
      'Meritage Cares Foundation is our company' in body[1].text and
      'Meritage Homes works with organizations like Operation Homefront' in body[2].text and
      'In 2021, in addition to contributing to education' in body[3].text
    )
  
  # Test whether the correct header appears in "Social: Service & Philanthropy" section
  def test_social_philanthropy_header(self, driver_settings):
    esg_page = ESGPage(self.driver)
    header = esg_page.get_text_social_philanthropy_header()
    assert 'Social: Service & Philanthropy' in header
  
  # Test whether button in "Social: Service & Philanthropy" section navigates to correct page when clicked
  def test_social_philanthropy_button(self, driver_settings):
    esg_page = ESGPage(self.driver)
    esg_page.close_cookies()
    esg_page.click_element_social_philanthropy_button()
    assert 'Meritage Cares: Operation Homefront | Meritage Homes' == self.driver.title
  
  # Test whether the correct image appears in "Corporate Governance" section
  def test_corporate_governance_image(self, driver_settings):
    esg_page = ESGPage(self.driver)
    image = esg_page.get_element_corporate_governance_image()
    result = esg_page.javascript_image(image)
    assert result
  
  # Test whether the correct body text appears in "Corporate Governance" section
  def test_corporate_governance_body(self, driver_settings):
    esg_page = ESGPage(self.driver)
    body = esg_page.get_elements_corporate_governance_body()
    assert (
      'A Commitment to Corporate Responsibility' in body[0].text and
      'At Meritage, we take pride in the way we responsibly govern our business' in body[1].text and
      'With the addition of Louis E. Caldera' in body[2].text
    )
  
  # Test whether the correct header appears in "Corporate Governance" section
  def test_corporate_governance_header(self, driver_settings):
    esg_page = ESGPage(self.driver)
    header = esg_page.get_text_corporate_governance_header()
    assert 'Corporate Governance' in header
  
  # Test whether button in "Corporate Governance" section navigates to correct page when clicked
  @pytest.mark.esg
  def test_corporate_governance_button(self, driver_settings):
    esg_page = ESGPage(self.driver)
    esg_page.close_cookies()
    esg_page.click_element_corporate_governance_button()
    assert 'Board Committees :: Meritage Homes Corporation (MTH)' == self.driver.title
  
  # Test whether the correct quote appears in last section 
  def test_quote(self, driver_settings):
    esg_page = ESGPage(self.driver)
    quote = esg_page.get_text_quote()
    assert 'In order to uphold our core values, we must expand our commitment to DE&I' in quote
  
  # Test whether the quote is attributed correctly in last section
  def test_quote_body(self, driver_settings):
    esg_page = ESGPage(self.driver)
    quote_body = esg_page.get_text_quote_body()
    assert 'Phillippe Lord, CEO' in quote_body