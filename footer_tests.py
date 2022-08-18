from email.mime import base
from operator import contains
import page as page
import pytest
import time

class Test_Footer_Element_Visibility():
  def __init__(self, driver):
    self.driver = driver
    page.MainPage(self.driver).close_cookies()
  
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
        assert "https://twitter.com/meritagehomes" == self.driver.current_url, "current_url " + str(self.driver.current_url)
      case '3':
        assert "https://www.pinterest.com/meritagehomes/" == self.driver.current_url, "current_url " + str(self.driver.current_url)
      case '4':
        assert "https://www.youtube.com/meritagehomes" == self.driver.current_url
      case '5':
        assert "https://www.instagram.com/accounts/login/?next=/meritagehomes/" == self.driver.current_url, "current_url " + str(self.driver.current_url)
      case _:
        assert False
      
  def footer_privacy_links(self, element):
    base_page = page.BasePage(self.driver)
    base_page.footer_click_element_privacy_policy_links(element)
    match element:
      case '1':
        assert "Meritage Homes Privacy Policy | Meritage Homes" == self.driver.title, str(self.driver.title)
      case '2':
        assert "Meritage Homes Terms of Use | Meritage Homes" == self.driver.title, str(self.driver.title)
      case '3':
        assert "Meritage Homes General Energy Claims | Meritage Homes" == self.driver.title, str(self.driver.title)
      case '4': 
        assert "My Meritage Portal" or "Loading..." == self.driver.title, str(self.driver.title)
  
  def footer_uncollapsable_text(self):
    base_page = page.BasePage(self.driver)
    text = base_page.footer_get_text_uncollapsable_disclaimer()
    assert "Pictures and other images are modified or edited representative" in text
  
  def footer_read_more(self):
    base_page = page.BasePage(self.driver)
    read_more = base_page.footer_get_element_read_more()
    self.driver.execute_script("arguments[0].scrollIntoView()", read_more) # The bottom scroll progres sbar on the apge is getting in the way of read more...
    base_page.footer_click_element_read_more()
    read_more_wrapper = base_page.footer_get_element_read_more_wrapper()
    result = self.driver.execute_script("return arguments[0].style.display != \"none\"", read_more_wrapper)
    assert result
  
  def footer_onetrust_overlay_on_green_read_more_click(self):
    base_page = page.BasePage(self.driver)
    green_read_more = base_page.footer_get_element_green_read_more_button()
    self.driver.execute_script("arguments[0].scrollIntoView()", green_read_more)
    base_page.footer_click_element_green_read_more_button()
    onetrust_overlay = base_page.footer_get_element_onetrust_overlay_on_green_press()
    result = self.driver.execute_script("return arguments[0].style.visibility != \"hidden\"", onetrust_overlay)
    assert result
  
  def footer_eho_image(self):
    base_page = page.BasePage(self.driver)
    eho_image = base_page.footer_get_element_eho_image()
    result = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", eho_image)
    assert result
  
  def footer_energy_star_image(self):
    base_page = page.BasePage(self.driver)
    energy_star_image = base_page.footer_get_element_energy_star_image()
    result = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", energy_star_image)
    assert result