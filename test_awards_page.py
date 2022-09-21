from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
from page_awards import AwardsPage
from page_base import BasePage
import math
import pytest
import time

URL = 'https://cd-sit.meritageweb.dev/why-meritage/awards'

@pytest.mark.usefixtures("init__driver", "driver_settings")
class BasicTest():
  pass


class Test_Awards_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get(URL)
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)

  def test_main_header(self):
    awards_page = AwardsPage(self.driver)
    header = awards_page.get_text_main_header()
    assert 'Meritage awards & accolades' in header

  def test_main_sub_header(self):
    awards_page = AwardsPage(self.driver)
    sub_header = awards_page.get_text_main_sub_header()
    assert 'Every home we build is designed to exceed' in sub_header
  
  def test_real_header(self):
    awards_page = AwardsPage(self.driver)
    header = awards_page.get_text_real_header()
    assert 'A real confidence builder' in header
  
  def test_real_body(self):
    awards_page = AwardsPage(self.driver)
    body = awards_page.get_text_real_body()
    assert (
      'been pushing ourselves' in body[0] and
      'See our track record' in body[1]
    )
  
  def test_national_header(self):
    awards_page = AwardsPage(self.driver)
    header = awards_page.get_text_national_header()
    assert 'National Awards' in header
  
  def test_national_body(self):
    awards_page = AwardsPage(self.driver)
    body = awards_page.get_text_national_body()
    assert 'a nationally recognized homebuilding' in body
  
  def test_national_images(self):
    awards_page = AwardsPage(self.driver)
    images = awards_page.get_elements_national_images()
    images_correct = False
    for i in range(len(images)):
      result = awards_page.javascript_image(images[i])
      if result:
        images_correct = True
      else:
        assert False
    assert images_correct
  
  def test_first_list(self):
    awards_page = AwardsPage(self.driver)
    list_text = awards_page.get_text_first_list()
    assert (
      '2022 Avid Cup Award' in list_text[0] and
      '2013 ENERGY STAR® Partner of the Year' in list_text[1] and
      '2013 ENERGY STAR® Leadership in Housing' in list_text[2] and
      'Indoor airPLUS Leader Award' in list_text[3] and
      'Builder of the Year for Green Home Builder' in list_text[4] and
      'U.S. Department of Energy Housing' in list_text[5] and
      '2017 Avid Diamond Award' in list_text[6] and
      '2016 Avid Diamond Award' in list_text[7] and
      '2015 Avid Diamond Award' in list_text[8] and
      '2014 No. 2 Most Trusted Builder in America' in list_text[9] and
      '2012 National Green Building Awards' in list_text[10] and
      '2011 EnergyValue Housing' in list_text[11] and
      '2011 People' in list_text[12] and
      '2011 Builder of the Year' in list_text[13]
    )
  
  def test_regional_header(self):
    awards_page = AwardsPage(self.driver)
    header = awards_page.get_text_regional_header()
    assert 'Regional Awards' in header
  
  def test_regional_body(self):
    awards_page = AwardsPage(self.driver)
    body = awards_page.get_text_regional_body()
    assert 'committed to being a partner you can trust' in body
  
  def test_regional_images(self):
    awards_page = AwardsPage(self.driver)
    images = awards_page.get_elements_regional_images()
    images_correct = False
    for i in range(len(images)):
      result = awards_page.javascript_image(images[i])
      if result:
        images_correct = True
      else:
        assert False
    assert images_correct
  
  def test_second_list(self):
    awards_page = AwardsPage(self.driver)
    list_text = awards_page.get_text_second_list()
    assert (
      '2022 Avid Gold Award' in list_text[0] and
      '2022 Avid Benchmark Award' in list_text[1] and
      '2021, 2020 Avid Diamond Award' in list_text[2] and
      '2021 Avid Gold Award' in list_text[3] and
      '2021 Avid Benchmark Award' in list_text[4] and
      '2020 Avid Benchmark Award' in list_text[5] and
      '2020 Avid Gold Award' in list_text[6] and
      '2019 Avid Gold Award' in list_text[7] and
      '2019 Avid Benchmark Award' in list_text[8] and
      '2018 Avid Gold Award' in list_text[9] and
      '2018 Avid Benchmark Award' in list_text[10] and
      '2017 Avid Gold Award' in list_text[11] and
      '2017 Avid Benchmark Award' in list_text[12] and
      '2016, 2015 Avid Gold Award' in list_text[13] and
      '2016 Avid Gold Award' in list_text[14] and
      '2016, 2015 Avid Benchmark Award' in list_text[15] and
      '2016 Avid Benchmark Award' in list_text[16] and
      '2016 Builder of the Year Over 200 Units' in list_text[17] and
      '2015 Avid Gold Award Southeast Region' in list_text[18] and
      '2015 Avid Gold Award Western Region' in list_text[19] and
      '2015 Avid Benchmark Award' in list_text[20] and
      '2014 Avid Benchmark Award' in list_text[21] and
      '2014 Avid Benchmark Award' in list_text[22] and
      '2014 Avid Benchmark Award' in list_text[23] and
      '2013 AREA Homebuilder of the Year' in list_text[24] and
      '2012 MAME Green Builder of the Year' in list_text[25] and
      '2011 Best Green Building Program' in list_text[26] and
      '2011 MAME "Best Energy Efficiency"' in list_text[27] and
      '2011 Green Pioneer' in list_text[28] and
      '2014 & 2013 MAME Green Builder of the Year' in list_text[29]
    )
  
  def test_setting_header(self):
    awards_page = AwardsPage(self.driver)
    header = awards_page.get_text_setting_header()
    assert 'Setting the standard for energy-efficient' in header
  
  def test_setting_body(self):
    awards_page = AwardsPage(self.driver)
    body = awards_page.get_text_setting_body()
    assert 'building new homes the way they can and' in body
  
  def test_setting_images(self):
    awards_page = AwardsPage(self.driver)
    images = awards_page.get_elements_setting_images()
    images_correct = False
    for i in range(len(images)):
      result = awards_page.javascript_image(images[i])
      if result:
        images_correct = True
      else:
        assert False
    assert images_correct
  
  def test_aside_body(self):
    awards_page = AwardsPage(self.driver)
    body = awards_page.get_text_aside_body()
    assert (
      'First Full Environmental Protection' in body[0] and
      'First 100' in body[1] and
      'First NET ZERO' in body[2]
    )
  
  def test_aside_button_1(self):
    awards_page = AwardsPage(self.driver)
    awards_page.close_cookies()
    awards_page.click_element_aside_button_1()
    assert 'ENERGY STAR' in self.driver.title

  def test_aside_button_2(self):
    awards_page = AwardsPage(self.driver)
    awards_page.close_cookies()
    awards_page.click_element_aside_button_2()
    assert 'Best Home Builders for Energy Efficient Homes | Meritage Homes' == self.driver.title
  
  def test_disclaimer(self):
    awards_page = AwardsPage(self.driver)
    disclaimer = awards_page.get_text_disclaimer_body()
    assert 'All of our homes built in California' in disclaimer
  
  def test_aside_ready_to_find_header(self, driver_settings):
    awards_page = AwardsPage(self.driver)
    header = awards_page.get_text_aside_ready_to_find_header()
    assert 'Ready to find your home' in header
  
  def test_aside_ready_to_find_body(self, driver_settings):
    awards_page = AwardsPage(self.driver)
    body = awards_page.get_text_aside_ready_to_find_body()
    assert 'ready to put our experience to work' in body
  
  def test_aside_ready_to_find_button_1(self, driver_settings):
    awards_page = AwardsPage(self.driver)
    awards_page.close_cookies()
    awards_page.click_element_aside_ready_to_find_button_1()
    assert 'Find a Home | Meritage Homes' == self.driver.title

  def test_aside_ready_to_find_button_2(self, driver_settings):
    awards_page = AwardsPage(self.driver)
    awards_page.close_cookies()
    awards_page.click_element_aside_ready_to_find_button_2()
    assert '' == self.driver.title