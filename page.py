from argparse import Action
from curses import window
from email import header
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
    WebDriverWait(self.driver, timeout=2).until(EC.visibility_of(cookies_bottom_banner))
    result = self.driver.execute_script("return arguments[0].style.display != \"none\"", cookies_bottom_banner)
    if result:
      close_cookies = self.driver.find_element(By.XPATH, "//*[@id='onetrust-close-btn-container']/a")
      WebDriverWait(self.driver, timeout=2).until(EC.element_to_be_clickable(close_cookies))
      close_cookies.click()
      WebDriverWait(self.driver, timeout=2).until(EC.invisibility_of_element(cookies_bottom_banner))

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


class MetroPage(BasePage): 
  def placeholder(self):
    return 'placeholder'
  

class MainPage(BasePage):
  def click_state(self, state):
    html = self.get_html()
    state_selected = self.driver.find_element(By.XPATH, f"//a[@href='/state/{state}']")
    state_selected.click()
    WebDriverWait(self.driver, timeout=15).until(EC.staleness_of(html)) 
#     return TexasPage(self.driver)

# class TexasPage(BasePage):
#   def something(self):
#     print("temp")

