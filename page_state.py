from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_base import BasePage


class StatePage(BasePage):
  def get_element_breadcrumbs_house(self):
    return self.driver.find_element(By.CLASS_NAME, "fa.fa-home")

  def get_text_breadcrumbs_header(self):
    header = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/nav/ul/li[2]/span")
    return header.text
  
  def get_text_state_header(self):
    header = self.driver.find_element(By.XPATH, "/html/body/header/div[1]/div/div[1]/div/h1")
    return header.text
  
  def get_text_state_sub_header(self):
    sub_header = self.driver.find_element(By.XPATH, "/html/body/header/div[1]/div/div[1]/div/p")
    return sub_header.text
  
  def get_text_scroll_down_arrow(self):
    arrow_text = self.driver.find_element(By.XPATH, "/html/body/header/div[2]/p")
    return arrow_text.text
  
  def get_element_scroll_down_arrow(self):
    return self.driver.find_element(By.XPATH, "/html/body/header/div[2]/a")
    
  def click_element_scroll_down_arrow(self):
    scroll_down_arrow = self.get_element_scroll_down_arrow()
    scroll_down_arrow.click()
  
  def get_element_aside(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/aside[1]")
  
  def get_text_aside_header(self):
    aside = self.get_element_aside()
    header = aside.find_element(By.TAG_NAME, "h2")
    return header.text

  def get_text_aside_sub_header(self):
    aside = self.get_element_aside()
    sub_header = aside.find_element(By.CSS_SELECTOR, "p:nth-child(3)")
    return sub_header.text

  def get_element_metro_div(self, number):
    return self.driver.find_element(By.XPATH, f"/html/body/main/div[{number}]")
  
  def get_text_metro_header(self, number):
    metro_div = self.get_element_metro_div(number)
    header = metro_div.find_element(By.TAG_NAME, "h3")
    return header.text
  
  def get_element_metro_header(self, number):
    metro_div = self.get_element_metro_div(number)
    return metro_div.find_element(By.TAG_NAME, 'a')
  
  def get_text_metro_cities_build(self, number):
    metro_div = self.get_element_metro_div(number)
    cities_build = metro_div.find_element(By.XPATH, "(.//p[@class='community--description'])[1]")
    return cities_build.text
  
  def get_text_metro_city_areas(self, number):
    metro_div = self.get_element_metro_div(number)
    city_areas = metro_div.find_element(By.XPATH, "(.//p[@class='community--description'])[2]")
    return city_areas.text
  
  def get_text_metro_stats(self, number):
    metro_div = self.get_element_metro_div(number)
    return metro_div.find_element(By.CLASS_NAME, 'community--community-count').text

  def get_element_metro_button(self, number):
    metro_div = self.get_element_metro_div(number)
    button = metro_div.find_element(By.CLASS_NAME, 'button.button--black.view')
    return button
  
  def click_element_metro_button(self, number):
    button = self.get_element_metro_button(number)
    html = self.get_html()
    button.click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def click_element_metro_next_arrow(self, number):
    metro_div = self.get_element_metro_div(number)
    arrow = metro_div.find_element(By.CLASS_NAME, 'orbit-next.slick-arrow')
    self.driver.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -350)", arrow)
    arrow.click()

  def get_element_metro_current_slide(self, number):
    metro_div = self.get_element_metro_div(number)
    return metro_div.find_element(By.XPATH, ".//li[contains(@class, 'slick-current')]")
  
  def get_element_metro_current_slide_image(self, number):
    current_slide = self.get_element_metro_current_slide(number)
    return current_slide.find_element(By.TAG_NAME, 'img')
  
  def get_element_section_metro_testimonial(self, number):
    return self.driver.find_element(By.XPATH, f"(.//article[@class='testimonial'])[{number}]")
  
  def get_text_testimonial_header(self, number):
    testimonial_section = self.get_element_section_metro_testimonial(number)
    return self.get_text_section_header(testimonial_section)

  def get_text_testimonial_quote(self, number):
    testimonial_section = self.get_element_section_metro_testimonial(number)
    return testimonial_section.find_element(By.TAG_NAME, 'blockquote').text

  def get_text_testimonial_attribution(self, number):
    testimonial_section = self.get_element_section_metro_testimonial(number)
    return testimonial_section.find_element(By.CLASS_NAME, 'attribution').text
  
  def get_element_section_why_meritage(self):
    return self.get_section_by_aria_label('article', 'Why Meritage Homes')
  
  def get_text_why_meritage_header(self):
    why_section = self.get_element_section_why_meritage()
    return why_section.find_element(By.TAG_NAME, 'h4').text
  
  def get_text_why_meritage_body(self):
    why_section = self.get_element_section_why_meritage()
    return self.get_text_section_body(why_section)
  
  def get_element_why_meritage_image(self):
    why_section = self.get_element_section_why_meritage()
    return self.get_element_section_placeholder_image(why_section)
  
  def click_element_why_meritage_button(self):
    html = self.get_html()
    why_section = self.get_element_section_why_meritage()
    self.click_element_section_button(why_section)
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
    
  def get_element_aside_know_state(self, current_state):
    return self.get_section_by_aria_label('aside', f'Want to get to know {current_state} better?')
  
  def get_text_aside_know_state_header(self, current_state):
    aside_know_state = self.get_element_aside_know_state(current_state)
    return self.get_text_section_header(aside_know_state)

  def get_text_aside_know_state_body(self, current_state):
    aside_know_state = self.get_element_aside_know_state(current_state)
    return self.get_text_section_body(aside_know_state)
  
  def click_element_aside_know_state_button_1(self, current_state):
    html = self.get_html()
    aside_know_state = self.get_element_aside_know_state(current_state)
    aside_know_state.find_element(By.XPATH, './/div/div/div[2]/a[1]').click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))

  def click_element_aside_know_state_button_2(self, current_state):
    html = self.get_html()
    aside_know_state = self.get_element_aside_know_state(current_state)
    aside_know_state.find_element(By.XPATH, './/div/div/div[2]/a[2]').click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))

  def get_text_aside_know_state_number(self, current_state):
    aside_know_state = self.get_element_aside_know_state(current_state)
    return aside_know_state.find_element(By.XPATH, './/div/div/div[3]').text
