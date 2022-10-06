from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
from page_qmi_search import QMISearchPage
from page_base import BasePage
import math
import pytest
import time


@pytest.mark.usefixtures("init__driver")
class BasicTest():
  def test_city_dropdown(self, driver_settings):
    qmi_search_page = QMISearchPage(self.driver)
    city_dropdown = qmi_search_page.get_element_city_dropdown()
    result = qmi_search_page.button_is_clickable(city_dropdown)
    assert result
  
  def test_bedrooms_dropdown(self, driver_settings):
    qmi_search_page = QMISearchPage(self.driver)
    bedrooms_dropdown = qmi_search_page.get_element_bedrooms_dropdown()
    result = qmi_search_page.button_is_clickable(bedrooms_dropdown)
    assert result
  
  def test_bathrooms_dropdown(self, driver_settings):
    qmi_search_page = QMISearchPage(self.driver)
    bathrooms_dropdown = qmi_search_page.get_element_bathrooms_dropdown()
    result = qmi_search_page.button_is_clickable(bathrooms_dropdown)
    assert result
  
  def test_slider_1(self, driver_settings):
    qmi_search_page = QMISearchPage(self.driver)
    qmi_search_page.close_cookies()
    qmi_search_page.slide_to_slide('bed')
    left_tag = qmi_search_page.get_text_slider_1_left_tag()
    right_tag = qmi_search_page.get_text_slider_1_right_tag()
    assert(
      '750' not in left_tag and
      '6,000' not in right_tag
    )
  
  def test_slider_2(self, driver_settings):
    qmi_search_page = QMISearchPage(self.driver)
    qmi_search_page.close_cookies()
    qmi_search_page.slide_to_slide('bath')
    left_tag = qmi_search_page.get_text_slider_2_left_tag()
    right_tag = qmi_search_page.get_text_slider_2_right_tag()
    assert(
      '750' not in left_tag and
      '6,000' not in right_tag
    )
  
  def test_submit(self, driver_settings):
    qmi_search_page = QMISearchPage(self.driver)
    submit_button = qmi_search_page.get_element_top_bar_submit_button()
    result = qmi_search_page.button_is_clickable(submit_button)
    assert result
  
  def test_reset(self, driver_settings):
    qmi_search_page = QMISearchPage(self.driver)
    reset_button = qmi_search_page.get_element_top_bar_reset()
    result = qmi_search_page.button_is_clickable(reset_button)
    assert result
  
  def test_zoom_in(self, driver_settings):
    qmi_search_page = QMISearchPage(self.driver)
    qmi_search_page.close_cookies()
    qmi_search_page.get_element_zoom_in()
    qmi_search_page.click_element_zoom_in()
  
  def test_new_homes_title(self, driver_settings):
    qmi_search_page = QMISearchPage(self.driver)
    header = qmi_search_page.get_text_title()
    assert 'Quick Move-In Homes' in header
  
  def test_title_link(self, driver_settings):
    qmi_search_page = QMISearchPage(self.driver)
    text = qmi_search_page.get_text_qmis_and_qmi()
    assert (
      'Communities' in text and
      'Quick Move-In Homes' in text
    )
  
  def test_qmis_appear(self, driver_settings):
    qmi_search_page = QMISearchPage(self.driver)
    qmis_elements = qmi_search_page.get_elements_qmis()
    assert len(qmis_elements) > 0
  
  def test_qmi_images(self, driver_settings):
    qmi_search_page = QMISearchPage(self.driver)
    qmis_elements = qmi_search_page.get_elements_qmis()
    all_images_present = False
    for i in range(len(qmis_elements)):
      image = qmi_search_page.get_element_qmi_image(i)
      result = qmi_search_page.javascript_image(image)
      if result:
        all_images_present = True
      else:
        assert False
    assert all_images_present
  
  @pytest.mark.zoom
  def test_qmis_plan_number(self, driver_settings):
    qmi_search_page = QMISearchPage(self.driver)
    qmis_elements = qmi_search_page.get_elements_qmis()
    all_plans_good = False
    for i in range(len(qmis_elements)):
      plan_text = qmi_search_page.get_text_qmi_plan(i)
      plan_number = plan_text.replace('Plan #', '')
      if len(plan_number) != 0:
        all_plans_good = True
      else:
        assert False
    assert all_plans_good
  

  @pytest.mark.zoom
  # sometimes the click is being intercepted and the test is failing but I do not know what is causing close_cookies() to not work as expected...
  def test_click_qmi(self, driver_settings):
    qmi_search_page = QMISearchPage(self.driver)
    time.sleep(3)
    qmi_search_page.close_cookies()
    name = qmi_search_page.get_text_qmi_name(0)
    qmi_search_page.click_element_qmi_name(0)
    new_page_header = qmi_search_page.get_text_new_page_qmi_header()
    assert name in new_page_header or new_page_header in name

  pass

class Test_Denver_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get("https://cd-sit.meritageweb.dev/state/co/denver/search/qmi/1")
    self.driver.set_window_position(0,0)
    return "Arizona"
    
  
# class Test_X_Page(BasicTest):
#   @pytest.fixture()
#   def driver_settings(self):
#     self.driver.get("placeholder")
#     self.driver.set_window_position(0,0)
#     return "California"
  

# class Test_Y_Page(BasicTest):
#   @pytest.fixture()
#   def driver_settings(self):
#     self.driver.get("placeholder")
#     self.driver.set_window_position(0,0)
#     return "Colorado"