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
  