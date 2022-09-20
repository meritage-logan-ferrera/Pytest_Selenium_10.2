from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_base import BasePage
import time  

class HowWeBuildPage(BasePage):
  def get_text_main_header(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/header/div/div/h1').text
    
  def get_text_main_sub_header(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/header/div/div').text
  
  def get_element_article_successful(self):
    return self.get_section_by_aria_label('article', 'A successful build involves two key components.')
  
  def get_text_successful_header(self):
    successful_section = self.get_element_article_successful()
    return self.get_text_section_header(successful_section)
  
  def get_element_article_successful_div_column(self, number):
    successful_section = self.get_element_article_successful()
    return successful_section.find_element(By.XPATH, f"(.//div[@class='column'])[{number}]")
  
  def get_element_successful_div_column_image(self, number):
    column = self.get_element_article_successful_div_column(number)
    return self.get_element_section_placeholder_image(column)
  
  def get_text_successful_div_column_header(self, number):
    column = self.get_element_article_successful_div_column(number)
    return column.find_element(By.TAG_NAME, 'h3').text
  
  def get_text_successful_div_column_body(self, number):
    column = self.get_element_article_successful_div_column(number)
    return self.get_text_section_body(column)
  
  def get_element_section_1(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/section")
  
  def get_text_section_1_header(self):
    section_1 = self.get_element_section_1()
    return self.get_text_section_header(section_1)
  
  def get_text_section_1_sub_header(self):
    section_1 = self.get_element_section_1()
    return section_1.find_element(By.XPATH, './/div/div[1]/div/p').text
  
  def get_element_section_1_drop_down_container(self, number):
    section_1 = self.get_element_section_1()
    return section_1.find_element(By.XPATH, f"/html/body/main/section/div/div[2]/div/ul[1]/li[{number}]")
  
  def get_element_section_1_drop_down_container_image(self, number):
    container = self.get_element_section_1_drop_down_container(number)
    return container.find_element(By.TAG_NAME, "img")
  
  def get_text_section_1_drop_down_container_header(self, number):
    container = self.get_element_section_1_drop_down_container(number)
    return container.find_element(By.TAG_NAME, "span").text
  
  def click_element_section_1_drop_down(self, number):
    container = self.get_element_section_1_drop_down_container(number)
    container.click()
  
  def get_element_section_1_responsive_tabs(self):
    section_1 = self.get_element_section_1()
    return section_1.find_element(By.XPATH, "/html/body/main/section/div/div[2]/div/ul[2]")
  
  def get_element_section_1_responsive_tab(self, number):
    tabs_container = self.get_element_section_1_responsive_tabs()
    return tabs_container.find_element(By.ID, f"tab-{number}-title")
    # classlist is-active

  def get_text_section_1_responsive_tab_header(self, number):
    tab = self.get_element_section_1_responsive_tab(number)
    return tab.find_element(By.TAG_NAME, "h4").text
  
  def get_elements_section_1_responsive_tab_body(self, number):
    tab = self.get_element_section_1_responsive_tab(number)
    return tab.find_elements(By.TAG_NAME, "p")
  
  def get_element_section_1_responsive_tab_image(self, number):
    tab = self.get_element_section_1_responsive_tab(number)
    return tab.find_element(By.TAG_NAME, "img")
  
  def get_element_section_pro_tip(self):
    return self.get_section_by_aria_label('article', 'How we build Testimonial')
  
  def get_element_pro_tip_current_slide(self):
    tip_section = self.get_element_section_pro_tip()
    return tip_section.find_element(By.XPATH, ".//li[contains(@class, 'slick-current')]")
  
  def get_text_pro_tip_header(self):
    current_slide = self.get_element_pro_tip_current_slide()
    return current_slide.find_element(By.TAG_NAME, 'h2').text
  
  def get_text_pro_tip_body(self):
    current_slide = self.get_element_pro_tip_current_slide()
    return current_slide.text
  
  def click_element_next_arrow(self):
    tip_section = self.get_element_section_pro_tip()
    tip_section.find_element(By.XPATH, './/div/div/ul/button[2]').click()
  
  def get_element_article_quality_of_your_home(self):
    return self.driver.find_element(By.ID, 'how-we-build')
  
  def get_text_quality_header(self):
    quality_section = self.get_element_article_quality_of_your_home()
    return self.get_text_section_header(quality_section)
  
  def get_elements_quality_body(self):
    quality_section = self.get_element_article_quality_of_your_home()
    return quality_section.find_elements(By.TAG_NAME, 'p')
  
  def get_element_section_slider(self):
    return self.driver.find_element(By.ID, 'how-we-build-slider')
  
  def get_element_slider(self):
    slider_section = self.get_element_section_slider()
    return slider_section.find_element(By.CLASS_NAME, 'irs-slider.single')
  
  def slide_to_slide(self, slide_number):
    slider = self.get_element_slider()
    self.driver.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(9, -750)", slider)
    slide_amount = 115*(slide_number - 1) 
    action = ActionChains(self.driver)
    action.move_to_element(slider).pause(.5).click_and_hold(slider).pause(.5).move_by_offset(slide_amount, 0).release().perform()
  
  def get_element_active_image_slide(self):
    slider_section = self.get_element_section_slider()
    slider_image_section = slider_section.find_element(By.ID, 'orbit-hwb')
    return slider_image_section.find_element(By.XPATH, ".//li[contains(@class, 'is-active')]")

  def get_element_active_slide_content(self):
    slider_section = self.get_element_section_slider()
    slider_content = slider_section.find_element(By.ID, 'orbit-hwb-content')
    return slider_content.find_element(By.XPATH, ".//li[contains(@class, 'is-active')]")
  
  def get_element_active_slide_image(self):
    active_image_slide = self.get_element_active_image_slide()
    return active_image_slide.find_element(By.TAG_NAME, 'img')

  def get_text_active_slide_sub_header(self):
    active_slide =self.get_element_active_slide_content()
    return active_slide.find_element(By.CLASS_NAME, 'slide-sub-title').text
  
  def get_text_active_slide_header(self):
    active_slide =self.get_element_active_slide_content()
    return active_slide.find_element(By.CLASS_NAME, 'slide-title').text

  def get_elements_active_slide_body(self):
    active_slide =self.get_element_active_slide_content()
    return active_slide.find_elements(By.TAG_NAME, 'p')
  
  def get_text_active_slide_optional_content_header(self):
    active_slide =self.get_element_active_slide_content()
    return active_slide.find_element(By.TAG_NAME, 'h3').text
  
  def click_element_active_slide_optional_button(self):
    html = self.get_html()
    active_slide =self.get_element_active_slide_content()
    active_slide.find_element(By.TAG_NAME, 'a').click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_element_article_mymeritage_portal(self):
    return self.get_section_by_aria_label('article', 'The MyMeritage portal: creating a personalized information center.')
  
  def get_text_mymeritage_header(self):
    mymeritage_section = self.get_element_article_mymeritage_portal()
    return self.get_text_section_header(mymeritage_section)
  
  def get_text_mymeritage_body(self):
    mymeritage_section = self.get_element_article_mymeritage_portal()
    return self.get_text_section_body(mymeritage_section)
  
  def get_elements_mymeritage_list(self):
    mymeritage_section = self.get_element_article_mymeritage_portal()
    return mymeritage_section.find_elements(By.TAG_NAME, 'li')
  
  def get_element_mymeritage_image(self):
    mymeritage_section = self.get_element_article_mymeritage_portal()
    return self.get_element_section_placeholder_image(mymeritage_section)
  
  def get_element_article_buy_your_home(self):
    return self.get_section_by_aria_label('aside', 'Buy your home with confidence.')
  
  def get_text_buy_your_home_header(self):
    buy_section = self.get_element_article_buy_your_home()
    return self.get_text_section_header(buy_section)
  
  def get_text_buy_your_home_body(self):
    buy_section = self.get_element_article_buy_your_home()
    return buy_section.find_element(By.CLASS_NAME, 'cta--content').text
  
  def click_element_buy_your_home_button(self):
    html = self.get_html()
    buy_section = self.get_element_article_buy_your_home()
    self.click_element_section_button(buy_section)
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_element_aside_ready_to_move(self):
    return self.get_section_by_aria_label('aside', 'Ready to make your move?')
  
  def get_text_aside_ready_to_move_header(self):
    aside_ready_to_move = self.get_element_aside_ready_to_move()
    return self.get_text_section_header(aside_ready_to_move)

  def get_text_aside_ready_to_move_body(self):
    aside_ready_to_move = self.get_element_aside_ready_to_move()
    return self.get_text_section_body(aside_ready_to_move)
  
  def click_element_aside_ready_to_move_button_1(self):
    html = self.get_html()
    aside_ready_to_move = self.get_element_aside_ready_to_move()
    aside_ready_to_move.find_element(By.XPATH, './/div/div/div[2]/a[1]').click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))

  def click_element_aside_ready_to_move_button_2(self):
    html = self.get_html()
    aside_ready_to_move = self.get_element_aside_ready_to_move()
    aside_ready_to_move.find_element(By.XPATH, './/div/div/div[2]/a[2]').click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))

  def get_text_aside_ready_to_move_number(self):
    aside_ready_to_move = self.get_element_aside_ready_to_move()
    return aside_ready_to_move.find_element(By.XPATH, './/div/div/div[3]').text