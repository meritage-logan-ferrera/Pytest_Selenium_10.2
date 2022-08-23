from curses import window
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import selenium.webdriver.common.keys
from selenium.webdriver.common.by import By
import time

class BasePage(object):
  MAIN_NAV_ELEMENTS = ('homes', 'why-meritage', 'buyer-resources', 'my-home')
  STATES = ('az', 'ca', 'co', 'fl', 'ga', 'nc', 'sc', 'tn', 'tx', 'map')
  WHY_MERITAGE_NAV_ELEMENTS = ('why-meritage', 'testimonials', 'reviews', 'energy-efficiency', 'how-we-design', 'how-we-build', 'awards')
  BUYER_RESOURCES_NAV_ELEMENTS = ('buyer-resources', 'homebuying', 'home-financing', 'energy-efficiency', 'home-design')
  TOP_BAR_ELEMENTS = ('myaccount', 'agents', 'contact')
  
  def __init__(self, driver):
    self.driver = driver
  
  def get_html(self): # get the DOM of the current page, use when testing links and navigation
    return self.driver.find_element(By.TAG_NAME, 'html')
  
  def get_title(self):
    return self.driver.title
  
  def close_cookies(self):
    cookies_bottom_banner = self.driver.find_element(By.ID, "onetrust-banner-sdk")
    WebDriverWait(self.driver, timeout=5).until(EC.visibility_of(cookies_bottom_banner))
    result = self.driver.execute_script("return arguments[0].style.display != \"none\"", cookies_bottom_banner)
    if result:
      close_cookies = self.driver.find_element(By.XPATH, "//*[@id='onetrust-close-btn-container']/a")
      WebDriverWait(self.driver, timeout=5).until(EC.element_to_be_clickable(close_cookies))
      close_cookies.click()
      WebDriverWait(self.driver, timeout=5).until(EC.invisibility_of_element(cookies_bottom_banner))

  def header_get_element_meritage_image_container(self):
    return self.driver.find_element(By.CSS_SELECTOR, "body > nav > div.row.full-width.diff.nav--bottom > div > a > div.logo--dark")

  def header_get_element_meritage_image_translucent(self):
    return self.driver.find_element(By.CSS_SELECTOR, ".logo--dark > img:nth-child(1)")

  def header_get_element_search_button(self):
    return self.driver.find_element(By.CSS_SELECTOR, "#button--search")

  def header_get_element_site_search_overlay(self):
    return self.driver.find_element(By.CSS_SELECTOR, "#site-search--overlay")
  
  def header_click_search_button(self):
    self.header_get_element_search_button().click()

  def header_get_element_top_bar_info(self, element):
    return self.driver.find_element(By.XPATH, f"//a[@href='/{element}']")
  
  def header_click_top_bar_element(self, element):
    html = self.get_html()
    header_top_bar_element = self.header_get_element_top_bar_info(element)
    header_top_bar_element.click()
    WebDriverWait(self.driver, timeout=15).until(EC.staleness_of(html))
  
  def header_get_element_header_main(self, element):
    return self.driver.find_element(By.XPATH, f"//a[@href='/{element}']")

  def header_click_main_element(self, element):
    html = self.get_html()
    header_main_element = self.header_get_element_header_main(element)
    header_main_element.click()
    WebDriverWait(self.driver, timeout=15).until(EC.staleness_of(html)) # wait until the entire old webpage is not present until we assert for the title of the new page

  def header_get_element_header_level2(self, level1_element, level2_element):
    level1 = self.header_get_element_header_main(level1_element)
    if level1_element != level2_element:
      if level1_element == 'homes':
        if level2_element == 'map':
          return level1.find_element(By.XPATH, f"//a[@href='/{level1_element}']")
        else:
          return level1.find_element(By.XPATH, f"//a[@href='/state/{level2_element}']")
      else:
        return level1.find_element(By.XPATH, f"//a[@href='/{level1_element}/{level2_element}']")
    else:
      return level1.find_element(By.XPATH, f"//a[@href='/{level1_element}']")

  def header_click_level2_element(self, level1_element, level2_element):
    html = self.get_html()
    header_main_element = self.header_get_element_header_main(level1_element)
    header_level2_element = self.header_get_element_header_level2(level1_element, level2_element)
    
    action = ActionChains(self.driver)
    action.move_to_element(header_main_element).move_by_offset(0, 50).move_to_element(header_level2_element).click().perform()
    WebDriverWait(self.driver, timeout=15).until(EC.staleness_of(html))
    if self.driver.title == '':
      time.sleep(5) # Firefox takes longer to load the title for some reason
    
  def footer_get_element_footer(self):
    return self.driver.find_element(By.XPATH, "/html/body/footer")
  
  def footer_get_element_company_nav_block(self):
    return self.driver.find_element(By.XPATH, "/html/body/footer/div[1]/div/div/div[1]")

  def footer_get_element_contact_nav_block(self):
    return self.driver.find_element(By.XPATH, "/html/body/footer/div[1]/div/div/div[2]")
  
  def footer_click_element_company_element(self, element):
    if element != '5':
      html = self.get_html()
      contact_block = self.footer_get_element_company_nav_block() 
      contact_block.find_element(By.XPATH, f"/html/body/footer/div[1]/div/div/div[1]/ul/li[{element}]/a").click()
      WebDriverWait(self.driver, timeout=15).until(EC.staleness_of(html))
    else: # Clicking the fith element opens the window in a new tab
      original_window = self.driver.current_window_handle
      contact_block = self.footer_get_element_company_nav_block() 
      contact_block.find_element(By.XPATH, f"/html/body/footer/div[1]/div/div/div[1]/ul/li[{element}]/a").click()
      WebDriverWait(self.driver, timeout=3).until(EC.number_of_windows_to_be(2))
      for window_handle in self.driver.window_handles:
        if window_handle != original_window:
          self.driver.switch_to.window(window_handle)
          break
    if self.driver.title == '':
      time.sleep(3)
    
  def footer_click_element_contact_element(self, element):
    html = self.get_html()
    contact_block = self.footer_get_element_contact_nav_block() 
    contact_block.find_element(By.XPATH, f"/html/body/footer/div[1]/div/div/div[2]/ul/li[{element}]/a").click()
    WebDriverWait(self.driver, timeout=15).until(EC.staleness_of(html))
  
  def footer_get_element_optin_signup(self):
    return self.driver.find_element(By.XPATH, "/html/body/footer/div[1]/div/div/div[4]/div")
  
  def footer_get_element_email_form_input(self):
    return self.driver.find_element(By.ID, "footer-open-modal-email")
  
  def footer_get_element_email_form_enter(self):
    return self.driver.find_element(By.ID, "footer-open-modal-trigger")
  
  def footer_get_element_email_form_error_image(self):
    return self.driver.find_element(By.XPATH, "/html/body/footer/div[1]/div/div/div[4]/div/form/div[1]/div[2]")
  
  def footer_get_element_error_message(self):
    return self.driver.find_element(By.XPATH, "/html/body/footer/div[1]/div/div/div[4]/div/form/div[2]")
  
  def footer_enter_keys_email_form_input(self):
    email_input = self.footer_get_element_email_form_input()
    email_input.send_keys('NotAValidEmail')
  
  def footer_click_element_email_form_enter(self):
    email_enter = self.footer_get_element_email_form_enter()
    email_enter.click()
  
  def footer_get_element_socials(self):
    return self.driver.find_element(By.XPATH, "/html/body/footer/div[1]/div/div/div[5]/div[2]")
  
  def footer_click_element_social_media_link(self, element):
    original_window = self.driver.current_window_handle
    socials = self.footer_get_element_socials()
    social_media_link = socials.find_element(By.XPATH, f"/html/body/footer/div[1]/div/div/div[5]/div[2]/a[{element}]")  
    social_media_link.click()
    WebDriverWait(self.driver, timeout=3).until(EC.number_of_windows_to_be(2))
    for window_handle in self.driver.window_handles:
      if window_handle != original_window:
        self.driver.switch_to.window(window_handle)
        break
    if self.driver.title == '':
      time.sleep(3)
  
  def footer_click_element_privacy_policy_links(self, element):
    original_window = self.driver.current_window_handle
    privacy_element = self.driver.find_element(By.XPATH, f"/html/body/footer/div[2]/div/div/div[1]/div[1]/ul/li[{element}]/a")
    privacy_element.click()
    if element == '4': # My Meritage Portal opens in a new tab
      WebDriverWait(self.driver, timeout=3).until(EC.number_of_windows_to_be(2))
      for window_handle in self.driver.window_handles:
        if window_handle != original_window:
          self.driver.switch_to.window(window_handle)
          break
      if self.driver.title == '':
        time.sleep(3)
      
  def footer_get_element_uncollapsable_disclaimer(self):
    return self.driver.find_element(By.XPATH, "/html/body/footer/div[2]/div/div/div[2]/div/div/p[1]")
  
  def footer_get_text_uncollapsable_disclaimer(self):
    uncollapse_disclaimer = self.footer_get_element_uncollapsable_disclaimer()
    return uncollapse_disclaimer.text
  
  def footer_get_element_read_more(self):
    return self.driver.find_element(By.ID, "FooterReadMore")
  
  def footer_click_element_read_more(self):
    read_more = self.footer_get_element_read_more()
    read_more.click()
  
  def footer_get_element_read_more_wrapper(self):
    return self.driver.find_element(By.ID, "FooterReadMoreWrapper")
  
  def footer_get_element_green_read_more_button(self):
    return self.driver.find_element(By.ID, "ot-sdk-btn")
  
  def footer_click_element_green_read_more_button(self):
    green_read_more = self.footer_get_element_green_read_more_button()
    green_read_more.click()
  
  def footer_get_element_onetrust_overlay_on_green_press(self):
    return self.driver.find_element(By.ID, "onetrust-pc-sdk")
  
  def footer_get_element_eho_image(self):
    return self.driver.find_element(By.XPATH, "/html/body/footer/div[2]/div/div/div[1]/div[2]/ul/li[1]/img")
  
  def footer_get_element_energy_star_image(self):
    return self.driver.find_element(By.XPATH, "/html/body/footer/div[2]/div/div/div[1]/div[2]/ul/li[2]/img")
  
class MainPage(BasePage):
  def get_element_meritage_video(self):
    return self.driver.find_element(By.XPATH, "/html/body/header/div[3]/video")
  
  def get_text_life_built_better(self):
    life_built_better = self.driver.find_element(By.XPATH, "/html/body/header/div[1]/div/div/div/h1")
    return life_built_better.text
  
  def get_text_let_us_find(self):
    let_us_find = self.driver.find_element(By.XPATH, "/html/body/header/div[1]/div/div/div/p")
    return let_us_find.text

  def get_element_scroll_down_arrow(self):
    return self.driver.find_element(By.XPATH, "/html/body/header/div[2]/a/img")
    
  def click_element_scroll_down_arrow(self):
    scroll_down_arrow = self.get_element_scroll_down_arrow()
    scroll_down_arrow.click()
  
  def get_element_aside_1(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/aside[1]")

  def get_element_save_the_rate_image(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/div/div/div/div/div/ul/li/figure/img")
  
  def get_text_aside_1_save_the_rate_h2(self):
    aside_1 = self.get_element_aside_1()
    save_the_rate = aside_1.find_element(By.XPATH, "/html/body/main/aside[1]/div/div/div[1]/h2")
    return save_the_rate.text
  
  def click_element_aside_1_save_the_rate_button(self):
    aside_1 = self.get_element_aside_1()
    save_the_rate_button = aside_1.find_element(By.XPATH, "/html/body/main/aside[1]/div/div/div[2]/a")
    save_the_rate_button.click()
  
  def get_element_article_1_not_all_new(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/article[1]")
    # arguments[0].clientHeight > 0

  def get_element_article_1_video_image(self):
    article_1 = self.get_element_article_1_not_all_new()
    return article_1.find_element(By.XPATH, "/html/body/main/article[1]/div/div[2]/div/img")

  def click_element_article_1_play_button(self):
    article_1 = self.get_element_article_1_not_all_new()
    play_button = article_1.find_element(By.XPATH, "/html/body/main/article[1]/div/div[2]/div/div/a/i")
    play_button.click()

  def get_element_article_1_video_overlay(self):
    article_1 = self.get_element_article_1_not_all_new()
    return article_1.find_element(By.XPATH, "/html/body/div[4]")
  
  def get_text_article_1_header(self):
    article_1 = self.get_element_article_1_not_all_new()
    return article_1.find_element(By.XPATH, "/html/body/main/article[1]/div/div[1]/h4").text
  
  def get_text_article_1_subtext(self):
    article_1 = self.get_element_article_1_not_all_new()
    return article_1.find_element(By.XPATH, "/html/body/main/article[1]/div/div[1]/p[1]").text
  
  def get_element_article_2_communities(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/article[2]")
  
  def get_text_article_2_header(self):
    article_2 = self.get_element_article_2_communities()
    return article_2.find_element(By.XPATH, "/html/body/main/article[2]/div/div/div[1]/div/h2").text
  
  def get_text_article_2_subtext(self):
    article_2 = self.get_element_article_2_communities()
    return article_2.find_element(By.XPATH, "/html/body/main/article[2]/div/div/div[1]/div/p").text
  
  def get_element_article_2_state_container(self, row, column):
    article_2 = self.get_element_article_2_communities()
    return article_2.find_element(By.XPATH, f"/html/body/main/article[2]/div/div/div[{row}]/div[{column}]")
  # For now not checking dymanic elements of these containers
  
  def click_element_article_2_state_container_button(self, row, column):
    button = self.driver.find_element(By.XPATH, f"/html/body/main/article[2]/div/div/div[{row}]/div[{column}]/div[1]/div/a")
    button.click()

  def get_element_article_3_military(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/article[3]")
  
  def click_element_article_3_a_look_back(self):
    html = BasePage(self.driver).get_html()
    article_3 = self.get_element_article_3_military()
    a_look_back_container = article_3.find_element(By.XPATH, "/html/body/main/article[3]/div/div[1]/div/div[1]")
    a_look_back_container.click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def click_element_article_3_frame_signing(self):
    html = BasePage(self.driver).get_html()
    article_3 = self.get_element_article_3_military()
    frame_signing_container = article_3.find_element(By.XPATH, "/html/body/main/article[3]/div/div[1]/div/div[2]")
    frame_signing_container.click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_text_article_3_header(self):
    article_3 = self.get_element_article_3_military()
    return article_3.find_element(By.XPATH, "/html/body/main/article[3]/div/div[2]/p/span").text

  def click_element_article_3_button(self):
    article_3 = self.get_element_article_3_military()
    article_3_button = article_3.find_element(By.XPATH, "/html/body/main/article[3]/div/div[2]/a")
    article_3_button.click()
  
  def get_element_article_4_expect_more(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/article[4]")
  
  def get_text_article_4_header(self):
    article_4 = self.get_element_article_4_expect_more()
    return article_4.find_element(By.XPATH, "/html/body/main/article[4]/div/div/div[1]/div/h2").text
  
  def get_text_article_4_subtext(self):
    article_4 = self.get_element_article_4_expect_more()
    return article_4.find_element(By.XPATH, "/html/body/main/article[4]/div/div/div[1]/div/p").text
  
  def get_element_article_4_container(self, element):
    article_4 = self.get_element_article_4_expect_more()
    return article_4.find_element(By.XPATH, f"/html/body/main/article[4]/div/div/div[2]/div[{element}]")

  def get_element_article_4_container_image(self, element):
    container = self.get_element_article_4_container(element)
    return container.find_element(By.TAG_NAME, "img")
  
  def get_text_article_4_container_pre_heading(self, element):
    container = self.get_element_article_4_container(element)
    return container.find_element(By.CLASS_NAME, "pre-heading").text

  def get_text_article_4_container_header(self, element):
    container = self.get_element_article_4_container(element)
    return container.find_element(By.TAG_NAME, "h3").text
  
  def get_text_article_4_container_description(self, element):
    container = self.get_element_article_4_container(element)
    return container.find_element(By.TAG_NAME, "p").text
  
  def click_element_article_4_button(self):
    article_4_button = self.driver.find_element(By.XPATH, "/html/body/main/article[4]/div/div/div[3]/div/a")
    article_4_button.click()

  def get_element_article_5_welcome_home(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/article[5]")
  
  def get_element_article_5_image_carousel(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/article[5]/div/div[1]")
  
  def get_element_article_5_image_in_carousel(self, number):
    carousel = self.get_element_article_5_image_carousel()
    return carousel.find_element(By.XPATH, f"//div[@data-slide='{number}']")

  def get_text_article_5_header(self):
    article_5 = self.get_element_article_5_welcome_home()
    return article_5.find_element(By.TAG_NAME, "h2").text
  
  def get_element_article_5_orbit_container(self):
    article_5 = self.get_element_article_5_welcome_home()
    return article_5.find_element(By.CLASS_NAME, "orbit-container")
  
  def get_element_article_5_orbit_slide(self, number):
    orbit_container = self.get_element_article_5_orbit_container()
    return orbit_container.find_element(By.XPATH, f"//li[@data-slide='{number}']")
  
  def get_element_article_5_current_orbit_slide(self):
    orbit_container = self.get_element_article_5_orbit_container()
    return orbit_container.find_element(By.CLASS_NAME, "orbit-slide.is-active")
  
  def click_element_article_5_orbit_video(self, number):
    orbit_slide = self.get_element_article_5_orbit_slide(number)
    orbit_video = orbit_slide.find_element(By.CLASS_NAME, "video-trigger.plain")
    orbit_video.click()
  
  # Need to find out how the site knows which youtube video to put in the overlay between the different slides
  def get_element_article_5_youtube_overlay(self):
    return self.driver.find_element(By.XPATH, "/html/body/div[4]")
  
  # Used in test_orbit_slides_text uses get_element_article_5_current_orbit_slide NOT get_element_article_5_orbit_slide
  def get_text_article_5_container_quote(self, number):
    active_slide = self.get_element_article_5_current_orbit_slide()
    return active_slide.find_element(By.CLASS_NAME, "orbit-slide--quote").text
  
  # Used in test_orbit_slides_text. Uses get_element_article_5_current_orbit_slide NOT get_element_article_5_orbit_slide
  def get_text_article_5_container_attribution(self, number):
    active_slide = self.get_element_article_5_current_orbit_slide()
    return active_slide.find_element(By.CLASS_NAME, "orbit-slide--attribution").text

  def click_element_article_5_right_button(self):
    right_button = self.driver.find_element(By.XPATH, "/html/body/main/article[5]/div/div[2]/div/div[3]/button")
    right_button.click()

  def get_element_article_6_awards(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/article[6]")
  
  def get_element_article_6_header(self):
    article_6 = self.get_element_article_6_awards()
    return article_6.find_element(By.TAG_NAME, "h2")
  
  def get_element_article_6_partner_image(self):
    article_6 = self.get_element_article_6_awards()
    return article_6.find_element(By.XPATH, "/div/div/div[2]/div[1]/img")
  
  def get_element_article_6_avid_image(self):
    article_6 = self.get_element_article_6_awards()
    return article_6.find_element(By.XPATH, "/div/div/div[2]/div[2]/img")

  def get_element_article_7_search_smarter(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/article[7]")

  def get_element_article_7_h2(self):
    article_7 = self.get_element_article_7_search_smarter()
    return article_7.find_element(By.TAG_NAME, "h2")

  def get_element_article_7_image_container_1(self):
    article_7 = self.get_element_article_7_search_smarter()
    return article_7.find_element(By.XPATH, "/div/div[2]/div/div[1]")

  def get_element_article_7_image_container_2(self):
    article_7 = self.get_element_article_7_search_smarter()
    return article_7.find_element(By.XPATH, "/div/div[2]/div/div[2]")
  
  # Should I paramaterize the above two functions into one???
  def get_text_article_7_image_container_header(self):
    container = self.get_element_article_7_image_container_1()
    return container.find_element(By.TAG_NAME, "h4")

  def click_element_article_7_image_container_1(self):
    self.get_element_article_7_image_container_1().click()

  def click_element_article_7_image_container_2(self):
    self.get_element_article_7_image_container_2().click()
  
  def click_element_article_7_button(self):
    article_7 = self.get_element_article_7_search_smarter()
    article_7.find_element(By.XPATH, "/div/div[1]/a")

  def get_element_aside_2_ready_to_find(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/aside[2]")
  
  def get_element_aside_2_header(self):
    aside_2 = self.get_element_aside_2_ready_to_find()
    return aside_2.find_element(By.TAG_NAME, "h2")
  
  def get_element_aside_2_subtext(self):
    aside_2 = self.get_element_aside_2_ready_to_find()
    return aside_2.find_element(By.TAG_NAME, "p")
  
  def click_element_aside_2_button(self):
    aside_2 = self.get_element_aside_2_ready_to_find()
    button = aside_2.find_element(By.TAG_NAME, "a")
    button.click()

class MetroPage(BasePage):
  def placeholder(self):
    return 'placeholder'
  




