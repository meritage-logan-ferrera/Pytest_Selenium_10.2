from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_base import BasePage
import time  

class NewsroomPage(BasePage):
  def get_text_main_header(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/header/div/div/h1').text
  
  def get_element_article_media_resources(self):
    return self.get_section_by_aria_label('article', 'Media Resources')
  
  def get_text_media_resources_header(self):
    media_section = self.get_element_article_media_resources()
    return self.get_text_section_header(media_section)
  
  def get_text_media_resources_body(self):
    media_section = self.get_element_article_media_resources()
    return media_section.find_element(By.TAG_NAME, 'span').text
  
  def get_element_article_download(self):
    return self.get_section_by_aria_label('article', 'Download the media kit.')
  
  def get_text_download_header(self):
    download_section = self.get_element_article_download()
    return self.get_text_section_header(download_section)
  
  def get_text_download_body(self):
    download_section = self.get_element_article_download()
    body_elements = download_section.find_elements(By.TAG_NAME, 'p')
    body_text = []
    for i in range(len(body_elements)):
      body_text.append(body_elements[i].text)
    return body_text
  
  def get_element_download_image(self):
    download_section = self.get_element_article_download()
    return self.get_element_section_placeholder_image(download_section)
  
  def click_element_download_button(self):
    original_window = self.driver.current_window_handle
    download_section = self.get_element_article_download()
    self.click_element_section_button(download_section)
    self.new_tab(original_window)
  
  def get_element_article_latest(self):
    return self.get_section_by_aria_label('article', 'See the latest Meritage news.')

  def get_text_latest_header(self):
    latest_section = self.get_element_article_latest()
    return self.get_text_section_header(latest_section)
  
  def get_text_latest_body(self):
    latest_section = self.get_element_article_latest()
    return latest_section.find_element(By.TAG_NAME, 'span').text
  
  def get_element_latest_image(self):
    latest_section = self.get_element_article_latest()
    return self.get_element_section_placeholder_image(latest_section)
  
  def click_element_latest_button(self):
    original_window = self.driver.current_window_handle
    latest_section = self.get_element_article_latest()
    self.click_element_section_button(latest_section)
    self.new_tab(original_window)
  
  def get_element_article_headlines(self):
    return self.get_section_by_aria_label('article', 'See Meritage in the headlines.')

  def get_text_headlines_header(self):
    headlines_section = self.get_element_article_headlines()
    return self.get_text_section_header(headlines_section)
  
  def get_text_headlines_body(self):
    headlines_section = self.get_element_article_headlines()
    return headlines_section.find_element(By.TAG_NAME, 'span').text
  
  def get_element_headlines_image(self):
    headlines_section = self.get_element_article_headlines()
    return self.get_element_section_placeholder_image(headlines_section)
  
  def click_element_headlines_button(self):
    html = self.get_html()
    headlines_section = self.get_element_article_headlines()
    self.click_element_section_button(headlines_section)
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_element_article_logos(self):
    return self.get_section_by_aria_label('article', 'Find images & logos.')

  def get_text_logos_header(self):
    logos_section = self.get_element_article_logos()
    return self.get_text_section_header(logos_section)
  
  def get_text_logos_body(self):
    logos_section = self.get_element_article_logos()
    return logos_section.find_element(By.XPATH, './/div/div/div/div[1]/p[2]').text
  
  def get_element_logos_image(self):
    logos_section = self.get_element_article_logos()
    return self.get_element_section_placeholder_image(logos_section)

  def get_element_aside_answer_questions(self):
    return self.get_section_by_aria_label('aside', 'We’re here to help answer your questions.')
  
  def get_text_answer_questions_header(self):
    answer_questions_section = self.get_element_aside_answer_questions()
    return self.get_text_section_header(answer_questions_section)
  
  def get_text_answer_questions_body(self):
    answer_questions_section = self.get_element_aside_answer_questions()
    return answer_questions_section.find_element(By.XPATH, './/div/div/div[1]').text
  
  def click_element_answer_questions_button(self):
    html = self.get_html()
    answer_questions_section = self.get_element_aside_answer_questions()
    self.click_element_section_button(answer_questions_section)
    WebDriverWait(self.driver, timeout=5).until(EC.staleness_of(html))
  