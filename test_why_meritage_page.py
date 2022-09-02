from page_why_meritage import WhyMeritagePage
from page_base import BasePage
from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
import pytest

URL = 'https://www.meritagehomes.com/why-meritage'

@pytest.mark.usefixtures("init__driver")
class BasicTest():
  pass

class Test_Why_Meritage_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get(URL)
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)
  
   # Test that the youtube video pops up after clicking the play button
  def test_overlay_on_play(self, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    why_page.click_element_play_button()
    youtube_overlay = why_page.get_element_youtube_overlay()
    result = self.driver.execute_script("return arguments[0].style.display != \"none\"", youtube_overlay)
    assert result
  
  # Test that main header displays the correct text
  def test_header(self, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    header = why_page.get_text_header()
    assert "Why Meritage" in header
  
  # Test that the correct text is displayed in the main sub-header
  def test_sub_header(self, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    sub_header = why_page.get_text_sub_header()
    assert "We believe that every family" in sub_header
  
  # Test that the image is displayed in article 1
  def test_article_1_image(self, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    image = why_page.get_element_article_1_image()
    result = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", image)
    assert result
  
  # Test that the correct header in article 1
  def test_article_1_header(self, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    header = why_page.get_text_article_1_header()
    assert "Explore Life" in header

  # Test that the correct sub-header in article 1
  def test_article_1_sub_header(self, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    sub_header = why_page.get_text_article_1_text()
    assert "Whether this is your first home" in sub_header

  # Test that button in article 1 navigates to correct page
  def test_article_1_button(self, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    why_page.close_cookies()
    why_page.click_element_article_1_button()
    assert "Best Home Builders for Energy Efficient Homes | Meritage Homes" == self.driver.title
  
  # Test that the drop down containers have the correct image and header
  @pytest.mark.parametrize('drop_down', ['1', '2', '3', '4'])
  def test_section_1_tabs(self, drop_down, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    image = why_page.get_element_section_1_drop_down_container_image(drop_down)
    header = why_page.get_text_section_1_drop_down_container_header(drop_down)
    result = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", image)
    header_bool = False
    match drop_down:
      case '1':
        if "More Savings" in header:
          header_bool = True
      case '2':
        if "Better Health" in header:
          header_bool = True
      case '3':
        if "Real Comfort" in header:
          header_bool = True
      case '4':
        if "Peace of Mind" in header:
          header_bool = True
      
    assert header_bool and result
  
  # Test that the drop down containers open the correct tabs when clicked and that all the information within the respective tabs are correct (correct tab displayed on click, header, body text, image, button navigation). This can be seperated into 5 tests in the future if needed...
  @pytest.mark.parametrize('tab', ['1', '2', '3', '4'])
  def test_section_1_tab_everything(self, tab, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    why_page.close_cookies()
    why_page.click_element_section_1_drop_down(tab)
    current_tab = why_page.get_element_section_1_responsive_tab(tab)
    tab_header = why_page.get_text_section_1_responsive_tab_header(tab)
    tab_body = why_page.get_elements_section_1_responsive_tab_body(tab)
    tab_image = why_page.get_element_section_1_responsive_tab_image(tab)
    
    # SUB TEST 1 for correct tab displayed on click:
    correct_tab =self.driver.execute_script("return arguments[0].classList.contains(\"is-active\")", current_tab) 
    
    # SUB TEST 2 for image:
    correct_image = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", tab_image)
    
    tab_header_bool = False
    tab_body_bool = False
    
    # SUB TESTS 3 & 4 for header and body in tab:
    match tab:
      case '1':
        if "More Savings" in tab_header:
          tab_header_bool = True
        if "Because" in tab_body[1].text and "Experience" in tab_body[2].text and "Water" in tab_body[3].text and "Advanced" in tab_body[4].text and "UV" in tab_body[5].text and "Climate" in tab_body[6].text:
          tab_body_bool = True
      case '2':
        if "Better Health" in tab_header:
          tab_header_bool = True
        if "Because" in tab_body[1].text and "Experience" in tab_body[2].text and "Fresh Air" in tab_body[3].text and "Health" in tab_body[4].text and "High" in tab_body[5].text and "Healthier" in tab_body[6].text:
          tab_body_bool = True
      case '3':
        if "Real Comfort" in tab_header:
          tab_header_bool = True
        if "Because" in tab_body[1].text and "Experience" in tab_body[2].text and "Temperature" in tab_body[3].text and "All" in tab_body[4].text and "Noise" in tab_body[5].text:
          tab_body_bool = True
      case '4':
        if "Peace of Mind" in tab_header:
          tab_header_bool = True
        if "Because" in tab_body[1].text and "Experience" in tab_body[2].text and "Smarter" in tab_body[3].text and "Experience" in tab_body[4].text and "Higher" in tab_body[5].text and "Proven" in tab_body[6].text:
          tab_body_bool = True
    
    why_page.click_element_section_1_responsive_tab_button(tab)
    button_nav_bool = False
    
    # SUB TEST 5 for button navigation to correct page:
    if "Best Home Builders for Energy Efficient Homes | Meritage Homes" == self.driver.title:
      button_nav_bool = True
    
    assert correct_tab and tab_header_bool and tab_body_bool and correct_image and button_nav_bool, "Tab text: " + tab_header + "; " + tab_body[0].text + "; " + tab_body[1].text + "; " + tab_body[2].text + "; " + tab_body[3].text + "; " + tab_body[4].text + "; " + tab_body[5].text
  
  # Test that all the chat articles sections on the page have the correct headers
  @pytest.mark.parametrize('chat_article', [0, 1, 2, 3])
  def test_chat_articles_header(self, chat_article, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    header = why_page.get_text_article_chat_header(chat_article)
    match chat_article:
      case 0:
        assert "How we design" in header
      case 1:
        assert "How we build" in header
      case 2:
        assert "Invest in your new home with confidence" in header
      case 3:
        assert "Life in a Meritage Home" in header
      

  # Test that all the chat articles sections on the page have the correct sub_headers
  @pytest.mark.parametrize('chat_article', [0, 1, 2, 3])
  def test_chat_articles_sub_header(self, chat_article, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    sub_header = why_page.get_text_article_chat_sub_header(chat_article)
    match chat_article:
      case 0:
        assert "help you make your house a home" in sub_header
      case 1:
        assert "breaking new ground" in sub_header
      case 2:
        assert "rest until a home that allows" in sub_header
      case 3:
        assert "Handing over the keys is just the beginning" in sub_header
  
  # Test that the images show up in the similar sections
  @pytest.mark.parametrize('chat_article', [0, 1, 2, 3])
  def test_chat_articles_image(self, chat_article, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    image = why_page.get_element_article_chat_image(chat_article)
    result = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", image)
    assert result

  # Test that the buttons on the sections from "how we design" to "life in a meritage home" navigate to the correct page when clicked
  @pytest.mark.parametrize('chat_article', [0, 1, 2, 3])
  def test_chat_articles_button_nav(self, chat_article, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    why_page.close_cookies()
    why_page.click_element_article_chat_button(chat_article)
    match chat_article:
      case 0:
        assert "How We Design | Meritage Homes" == self.driver.title
      case 1:
        assert "How We Build New Home Communities | Meritage Homes" == self.driver.title
      case 2:
        assert "Home Buying Experience | Meritage Homes" == self.driver.title
      case 3:
        assert "Meritage Homes Testimonials | Meritage Homes" == self.driver.title
  
  # Test that the correct text is displayed in the main header for the Meritage Cares section
  def test_article_6_header_1(self, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    header = why_page.get_text_article_6_header_1()
    assert "Meritage Cares" in header
  
  # Test that the correct text is displayed in the main sub_header for the Meritage Cares section
  def test_article_6_sub_header_1(self, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    sub_header = why_page.get_text_article_6_sub_header_1()
    assert "committed to building better homes and stronger communities" in sub_header
  
  # Test that the correct text is displayed in the second header for the Meritage Cares section
  def test_article_6_header_2(self, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    header = why_page.get_text_article_6_header_2()
    assert "More than 30 years of building strong communities" in header
  
  # Test that the correct text is displayed in the second sub_header for the Meritage Cares section
  def test_article_6_sub_header_2(self, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    sub_header = why_page.get_text_article_6_sub_header_2()
    assert "Supporting communities through giving is a cornerstone" in sub_header
  
  # Test that the correct image is displayed in the Meritage Cares section
  def test_article_6_image(self, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    image = why_page.get_element_article_6_image()
    result = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", image)
    assert result

  # Test that the button in the meritage homes section navigates to correct page on click
  def test_article_6_button(self, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    why_page.close_cookies()
    why_page.click_element_article_6_button()
    assert "Meritage Cares: Operation Homefront | Meritage Homes" == self.driver.title
  
  # Test that the correct text appears in article 7 header
  def test_article_7_header(self, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    header = why_page.get_text_article_7_header()
    assert "A real confidence builder" in header
  
  # Test that the correct text appears in article 7 sub_header
  def test_article_7_sub_header(self, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    sub_header = why_page.get_text_article_7_sub_header()
    assert "We work every day to make sure our homes" in sub_header
  
  # Test that the correct text appears in article 7 list elements
  def test_article_7_list(self, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    list = why_page.get_elements_article_7_list()
    list_1 = list[0].text
    list_2 = list[1].text
    list_3 = list[2].text
    assert "2022" in list_1 and "2020" in list_2 and "2015" in list_3
  
  # Test that the button in article 7 section navigates to correct page on click
  def test_article_7_button(self, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    why_page.close_cookies()
    why_page.click_element_article_7_button()
    assert "Meritage Homes Awards and Accolades | Meritage Homes" == self.driver.title
  
  # Test that the correct image is displayed in the "A real confidence builder" section
  def test_article_7_image(self, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    image = why_page.get_element_article_7_image()
    result = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", image)
    assert result

  # Test that the correct text appears in article 8 header
  def test_article_8_header(self, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    header = why_page.get_text_article_8_header()
    assert "Of all the things we" in header
  
# Test that the correct text appears in article 8 sub_header
  def test_article_8_sub_header(self, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    sub_header = why_page.get_text_article_8_sub_header()
    assert "Every day we strive to deliver a Life" in sub_header
  
  # Test that the button in article 8 section navigates to correct page on click
  def test_article_8_button(self, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    why_page.close_cookies()
    why_page.click_element_article_8_button()
    assert "2021 Avid Awards | Meritage Homes" == self.driver.title
  
  # Test that the correct image is displayed in the AVID section
  def test_article_8_image(self, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    image = why_page.get_element_article_8_image()
    result = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", image)
    assert result
    
  # Test that the correct text appears in aside header
  def test_aside_header(self, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    header = why_page.get_text_aside_header()
    assert "Ready to make your move" in header
  
  # Test that the correct text appears in aside sub_header
  def test_aside_sub_header(self, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    sub_header = why_page.get_text_aside_sub_header()
    assert "Whether you just need" in sub_header

  # Test that the first button in aside section navigates to correct page on click
  def test_aside_button_1(self, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    why_page.close_cookies()
    why_page.click_element_aside_button_1()
    assert "Find a Home | Meritage Homes" == self.driver.title
  
  # Test that the second button in aside section navigates to correct page on click
  def test_aside_button_2(self, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    why_page.close_cookies()
    why_page.click_element_aside_button_2()
    assert "" == self.driver.title
