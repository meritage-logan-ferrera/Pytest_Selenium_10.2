from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
from page_meritage_cares import MeritageCaresPage
from page_base import BasePage
import math
import pytest
import time

URL = 'https://cd-sit.meritageweb.dev/why-meritage/meritage-cares'

@pytest.mark.usefixtures("init__driver")
class BasicTest():
  pass

class Test_Meritage_Cares_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get(URL)
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)
  
  # Test whether correct text in main header
  def test_main_header(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    header = cares_page.get_text_main_header()
    assert 'The Meritage Cares Foundation' in header
  
  # Test whether correct text in main sub header
  def test_main_sub_header(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    body = cares_page.get_text_main_sub_header()
    assert 'Better Homes' in body
  
  # Test whether correct text in putting_mission header
  def test_putting_mission_header(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    header = cares_page.get_text_putting_our_mission_header()
    assert 'Putting Our Mission Into Action' in header
  
  # Test whether correct text in putting_mission body
  def test_putting_mission_body(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    body = cares_page.get_text_putting_our_mission_body()
    assert 'Meritage Cares is more than a slogan' in body
  
  # Test whether correct text in headers, bodies and images in the containers in the putting mission section
  @pytest.mark.parametrize('number', [0, 1, 2])
  def test_putting_mission_containers(self, number, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    header = cares_page.get_text_putting_our_mission_container_header(number)
    body = cares_page.get_text_putting_our_mission_container_body(number)
    image = cares_page.get_text_putting_our_mission_container_image(number)
    result = cares_page.javascript_image(image)
    match number:
      case 0:
        assert (
          'Giving to Veterans' in header and
          'Without our veterans' in body and
          result
        )
      case 1:
        assert (
          'Giving to Families' in header and
          'We support a variety of causes' in body and
          result
        )
      case 2:
        assert (
          'Giving to Children' in header and
          'We give to organizations that provide' in body and
          result
        )
 
  # Test whether the pdf button takes user to pdf file (in same tab)
  def test_pdf_button(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    cares_page.close_cookies()
    cares_page.click_element_pdf_button()
    assert 'Meritage_Cares.pdf' == self.driver.title
  
  # Test whether correct text in why_we_give header
  def test_why_we_give_header(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    header = cares_page.get_text_why_we_give_header()
    assert 'Why We Give' in header
  
  # Test whether correct text in why_we_give body
  def test_why_we_give_body(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    body = cares_page.get_text_why_we_give_body()
    assert 'The mission of Meritage Cares' in body
  
  # Test whether correct image in why_we_give
  def test_why_we_give_image(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    image = cares_page.get_element_why_we_give_image()
    result = cares_page.javascript_image(image)
    assert result
  
  # Test whether correct text in why_we_give disclaimer
  def test_why_we_give_disclaimer(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    disclaimer = cares_page.get_text_why_we_give_disclaimer()
    assert 'The Meritage Cares Foundation is' in disclaimer
  
  # Test whether correct text in feeding america header
  def test_feeding_america_header(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    header = cares_page.get_text_feeding_america_header()
    assert 'Feeding America' in header
  
  # Test whether correct text in feeding america body
  def test_feeding_america_body(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    body = cares_page.get_text_feeding_america_body()
    assert (
      'In 2020' in body[0].text and
      'We continue to work' in body[1].text and
      'feedingamerica.org' in body[2].text
    )
  
  # Test whether correct image in feeding america
  def test_feeding_america_image(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    image = cares_page.get_element_feeding_america_image()
    result = cares_page.javascript_image(image)
    assert result
  
  # Test whether correct text in arizona_housing_fund header
  def test_arizona_housing_fund_header(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    header = cares_page.get_text_arizona_housing_fund_header()
    assert 'Arizona Housing Fund' in header
  
  # Test whether correct text in arizona_housing_fund body
  def test_arizona_housing_fund_body(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    body = cares_page.get_text_arizona_housing_fund_body()
    assert (
      'We believe that everyone' in body[0].text and
      'arizonahousingfund.org' in body[1].text
    )
  
  # Test whether correct image in arizona_housing_fund
  def test_arizona_housing_fund_image(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    image = cares_page.get_element_arizona_housing_fund_image()
    result = cares_page.javascript_image(image)
    assert result
  
  # Test whether button in arizaon housing fund seciton takes user to correct page when clicked
  def test_arizona_housing_fund_play_button(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    cares_page.close_cookies()
    cares_page.click_element_arizona_housing_fund_play_button()
    youtube_overlay = cares_page.get_element_youtube_overlay()
    result = self.driver.execute_script("return arguments[0].style.display != 'none'", youtube_overlay)
    assert result
  
  # Test whether correct text in giving_milestones header
  def test_giving_milestones_header(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    header = cares_page.get_text_giving_milestones_header()
    assert 'Giving Milestones' in header
  
  # Test whether correct text in giving_milestones body
  def test_giving_milestones_body(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    body = cares_page.get_text_giving_milestones_body()
    assert 'In addition to gifting a mortgage' in body 
  
  # Test whether correct image in giving_milestones 
  def test_giving_milestones_image(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    image = cares_page.get_element_giving_milestones_image()
    result = cares_page.javascript_image(image)
    assert result
  
  # Test whether correct text in giving_milestones caption
  def test_giving_milestones_caption(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    caption = cares_page.get_text_giving_milestones_caption()
    assert 'Partnered with Operation Homefront' in caption
  
  # Test whether correct text in operation_homefront header
  def test_operation_homefront_header(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    header = cares_page.get_text_operation_homefront_header()
    assert 'Operation Homefront' in header
  
  # Test whether correct text in operation_homefront sub header
  def test_operation_homefront_sub_header(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    sub_header = cares_page.get_text_operation_homefront_sub_header()
    assert 'Building A Strong Foundation for Veteran' in sub_header
  
  # Test whether correct text in operation_homefront sub sub header
  def test_operation_homefront_sub_sub_header(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    sub_sub_header = cares_page.get_text_operation_homefront_sub_sub_header()
    assert 'Building up' in sub_sub_header
  
  # Test whether correct text in operation_homefront body
  def test_operation_homefront_body(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    body = cares_page.get_text_operation_homefront_body()
    assert 'They fought for the American dream' in body 
  
  # Test whether correct image in operation_homefront
  def test_operation_homefront_image(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    image = cares_page.get_element_operation_homefront_image()
    result = cares_page.javascript_image(image)
    assert result
  
  # Test whether the first button in operation_homefront naivgates to correct page when clicked
  def test_operation_homefront_button_1(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    cares_page.close_cookies()
    cares_page.click_element_operation_homefront_button_1()
    assert 'Operation Homefront | Meritage Homes' == self.driver.title
  
  #BROKEN LINK
  # Test whether the second button in operation_homefront naivgates to correct page when clicked
  def test_operation_homefront_button_2(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    cares_page.close_cookies()
    cares_page.click_element_operation_homefront_button_2()
    assert 'Page not found - Operation Homefront' == self.driver.title
  
  # Test whether correct text in american flag section quote
  def test_american_flag_quote(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    quote = cares_page.get_text_american_flag_quote()
    assert 'Supporting the communities' in quote
  
  # Test whether correct text in american flag section body
  def test_american_flag_body(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    body = cares_page.get_text_american_flag_body()
    assert 'Steven J. Hilton' in body 
  
  # Test whether correct text in where we give header
  def test_where_we_give_header(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    header = cares_page.get_text_where_we_give_header()
    assert 'Where we give' in header
  
  # Test whether correct text in where we give body
  def test_where_we_give_body(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    body = cares_page.get_text_where_we_give_body()
    assert 'From California to the Carolinas' in body 
  
  # Test whether all the correct text is in each of the state dropdowns
  @pytest.mark.parametrize('number', [0,1,2,3,4,5,6,7,8])
  def test_where_we_give_state_dropdowns(self, number, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    cares_page.close_cookies()
    cares_page.click_element_current_state(number)
    list_body = cares_page.get_elements_where_we_give_current_state_community_efforts(number)
    match number:
      case 0:
        assert (
          'Phoenix' == list_body[0].text and
          'Valley Kids Foundation' == list_body[1].text and
          '#Love Up Foundation' == list_body[2].text and
          'Boys & Girls Club of Greater Scottsdale' == list_body[3].text and
          'HonorHealth Foundation' == list_body[4].text and
          'New Life Center' == list_body[5].text and
          'Arizona Housing Fund' == list_body[6].text and
          'Tucson' == list_body[7].text and
          'Support Our Students' == list_body[8].text and
          "Ben's Bells, Inc." == list_body[9].text and
          'Operation Homefront - Holiday Meals for Military' == list_body[10].text and
          'Arizona Housing Fund' == list_body[11].text
        )
      case 1:
        assert (
          'Northern, CA' == list_body[0].text and
          'McHenry House Tracy Family Shelter' == list_body[1].text and
          'Shelter Providers of Sacramento' == list_body[2].text and
          'North Valley Community Foundation Missing' == list_body[3].text and
          'Southern, CA' == list_body[4].text and
          'Big Brothers/Big Sisters of Orange County, Inc' == list_body[5].text and
          'California Homebuilding Foundation' == list_body[6].text
        )
      case 2:
        assert (
          'Denver' == list_body[0].text and
          'Hope House Colorado' == list_body[1].text
        )
      case 3:
        assert (
          'Tampa' == list_body[0].text and
          'Meals on Wheels of Tampa' == list_body[1].text and
          "The Children's Home Society of Florida" == list_body[2].text and
          "Women's Resource Center of Tampa, Inc. " == list_body[3].text and
          'Orlando' == list_body[4].text and
          'Boys Town Central Florida, Inc.' == list_body[5].text and
          'Orlando Magic Youth Foundation, Inc.' == list_body[6].text and
          "St. Jude Children's Hospital" == list_body[7].text
        )
      case 4:
        assert (
          'Atlanta' == list_body[0].text and
          'Reflections of Trinity' == list_body[1].text and
          'First Baptist Church of Woodstock' == list_body[2].text
        )
      case 5:
        assert (
          'Charlotte' == list_body[0].text and
          'Ronald McDonald House of Charlotte' == list_body[1].text and
          'Carolina Defenders' == list_body[2].text and
          'Kids First of the Carolinas' == list_body[3].text and
          'Dream on 3 ' == list_body[4].text and
          'Raleigh' == list_body[5].text and
          'Habitat for Humanity of Durham' == list_body[6].text
        )
      case 6:
        assert (
          'Greenville' == list_body[0].text and
          'Ronald McDonald House Charities, Inc.' == list_body[1].text and
          'Harvest Hope Food Bank' == list_body[2].text and
          'Meyer Center for Special Children' == list_body[3].text and
          'Habitat for Humanity of Greenville County ' == list_body[4].text
        )
      case 7:
        assert (
          'Nashville' == list_body[0].text and
          'Open Table of Nashville, Inc. ' == list_body[1].text and
          'Nashville Rescue Mission' == list_body[2].text and
          'Monroe Harding' == list_body[3].text and
          'The Branch of Nashville' == list_body[4].text
        )
      case 8:
        assert (
          'Austin' == list_body[0].text and
          'Generation SERVE' == list_body[1].text and
          'Transformations By Austin Angels' == list_body[2].text and
          'Foster Angels of Central Texas' == list_body[3].text and
          'HomeAid Austin' == list_body[4].text and
          'Dallas/Ft. Worth' == list_body[5].text and
          'Salemanship Club Youth and Family Centers, Inc.' == list_body[6].text and
          'North Texas Food Bank' == list_body[7].text and
          'Big Brothers/Big Sisters Lane Star' == list_body[8].text and
          'Houston' == list_body[9].text and
          'Blessings in a Backpack, Inc.' == list_body[10].text and
          'East Fort Bend Human Needs Ministry, Inc.' == list_body[11].text and
          'Partners for Harris County Children Inc., dba Bear Be A Resource for CPS Kids' == list_body[12].text and
          'Shelter Providers of Houston, Inc.' == list_body[13].text and
          # empty p tag here so skip [14]
          'San Antonio' == list_body[15].text and
          ' Essilor Vision Foundation' == list_body[16].text and
          "The Academy oat Morgan's Wonderland" == list_body[17].text and
          "The Children's Bereavement Center of South Texas" == list_body[18].text and
          'Elf Louise Inc.' in list_body[19].text
        )
  
  # Test whether clicking the back to top button takes user all the way to the top of the page
  def test_where_we_give_scroll(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    html = cares_page.get_html()
    cares_page.close_cookies()
    cares_page.click_element_where_we_give_scroll_button()
    result = self.driver.execute_script("return arguments[0].scrollTop == 0", html)
    assert result
  
  # Test whether correct text in supporting_charities header
  def test_supporting_charities_header(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    header = cares_page.get_text_supporting_charities_header()
    assert 'Supporting charities' in header
  
  # Test whether correct text in supporting_charities body
  def test_supporting_charities_body(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    body = cares_page.get_text_supporting_charities_body()
    assert 'Interested in learning more about Meritage Cares' in body 
  
  # Test whether the first button in supporting_charities navigates to the correct page when clicked
  def test_supporting_charities_button_1(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    cares_page.close_cookies()
    cares_page.click_element_supporting_charities_button_1()
    assert 'About Meritage Homes | Meritage Homes' == self.driver.title
  
  # Test whether the second button in supporting_charities navigates to the correct page when clicked
  def test_supporting_charities_button_2(self, driver_settings):
    cares_page = MeritageCaresPage(self.driver)
    cares_page.close_cookies()
    cares_page.click_element_supporting_charities_button_2()
    assert '' == self.driver.title
  
  # FAILURE(S) ON SIT
  # 1. test_pdf_button opens the pdf file in a new tab and downloads it on the new solution. This does not happen on prod.....