from page_why_meritage import WhyMeritagePage
from page_base import BasePage
from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
import pytest

URL = 'https://www.meritagehomes.com/why-meritage'

@pytest.mark.usefixtures("init__driver")
class BasicTest():
  pass

class Test_Main_Page(BasicTest):
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
    assert "Why Meritage" in sub_header
  
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
    assert "Whether this your first home" in sub_header

  # Test that button in article 1 navigates to correct page
  def test_article_1_button(self, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    why_page.click_element_article_1_button()
    assert "Best Home Builders for Energy Efficient Homes | Meritage Homes" == self.driver.title
  
  # Test that the drop down containers have the correct image and header
  @pytest.mark.parametrize('drop_down', ['1', '2', '3', '4'])
  def test_section_1_image(self, drop_down, driver_settings):
    why_page = WhyMeritagePage(self.driver)
    image = why_page.get_element_section_1_drop_down_container_image(drop_down)
    header = why_page.get_element_section_1_drop_down_container_header(drop_down)
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
  @pytest.mark.tab
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
        assert "Invest in yout new home with confidence" in header
      case 3:
        assert "Life in a Meritage Home" in header
      