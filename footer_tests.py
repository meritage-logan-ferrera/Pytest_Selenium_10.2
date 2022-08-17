import page as page
import pytest
import time

class Test_Footer_Element_Visibility():
  def __init__(self, driver):
    self.driver = driver
  
  def footer_company_element(self, element):
    base_page = page.BasePage(self.driver)
    base_page.footer_click_element_company_element(element)
    match element:
      case '1':
        assert "About Meritage Homes | Meritage Homes" == self.driver.title
      case '2':
        assert "Meritage Cares: Operation Homefront | Meritage Homes" == self.driver.title
      case '3':
        assert "Environmental, Social & Governance | Meritage Homes" == self.driver.title
      case '4':
        assert "Meritage Homes Newsroom | Meritage Homes" == self.driver.title
      case '5':
        assert "Investor Relations :: Meritage Homes Corporation (MTH)" == self.driver.title
      case _:
        assert False
  
  def footer_contact_element(self, element):
    base_page = page.BasePage(self.driver)
    base_page.footer_click_element_contact_element(element)
    match element:
      case '1':
        assert "" == self.driver.title
      case '2':
        assert "Directions to reach your community | Meritage Homes" == self.driver.title
      case '3':
        assert "Meritage Careers - Real Estate Careers | Meritage Homes" == self.driver.title
      case '4':
        assert "Meritage Homes Corporate Offices | Meritage Homes" == self.driver.title
      case _:
        assert False

  def footer_enter_email_error_image(self):
    base_page = page.BasePage(self.driver)
    base_page.footer_enter_keys_email_form_input()
    base_page.footer_click_element_email_form_enter()
    error_image = base_page.footer_get_element_email_form_error_image()
    result = self.driver.execute_script("return arguments[0].classList.contains('is-visible')", error_image)
    assert result
  
  def footer_enter_email_error_field(self):
    base_page = page.BasePage(self.driver)
    base_page.footer_enter_keys_email_form_input()
    base_page.footer_click_element_email_form_enter()
    error_field = base_page.footer_get_element_error_message()
    result = self.driver.execute_script("return arguments[0].style.display != \"none\"", error_field)
    assert result
  
  def footer_social_media(self, element):
    base_page = page.BasePage(self.driver)
    base_page.footer_click_element_social_media_link(element)
    match element:
      case '1':
        assert "https://www.facebook.com/meritagehomes" == self.driver.current_url
      case '2':
        assert "https://www.twitter.com/meritagehomes" == self.driver.current_url
      case '3':
        assert "https://www.pinterest.com/meritagehomes" == self.driver.current_url
      case '4':
        assert "https://www.youtube.com/meritagehomes" == self.driver.current_url
      case '5':
        assert "https://www.instagram.com/meritagehomes" == self.driver.current_url
      case _:
        assert False