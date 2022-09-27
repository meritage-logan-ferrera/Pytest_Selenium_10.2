from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_base import BasePage
import time  

class HomeFinancingPage(BasePage):
  def get_text_main_header(self):
    return self.driver.find_element(By.XPATH, '/html/body/header/div/div/h1').text
  
  def get_text_main_body(self):
    return self.driver.find_element(By.XPATH, '/html/body/header/div/div/p').text
  
  def click_element_main_button(self):
    html = self.get_html()
    self.driver.find_element(By.XPATH, '/html/body/header/div/div/a').click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_element_section_articles(self):
    return self.driver.find_element(By.CLASS_NAME, 'resource-center')

  def get_text_section_articles_header(self):
    articles_section = self.get_element_section_articles()
    return self.get_text_section_header(articles_section)

  def get_text_section_articles_body(self):
    articles_section = self.get_element_section_articles()
    return self.get_text_section_body(articles_section)
  
  def get_element_articles_container(self):
    articles_section = self.get_element_section_articles()
    return articles_section.find_element(By.CLASS_NAME, 'medium-uncollapse.small-collapse.row.align-center')
  
  def get_elements_active_articles(self):
    articles_container = self.get_element_articles_container()
    all_articles = articles_container.find_elements(By.XPATH, './div')
    active_articles = []
    for i in range(len(all_articles)):
      if all_articles[i].value_of_css_property('display') != 'none':
        active_articles.append(all_articles[i])
    return active_articles

  def get_text_article_header(self, number):
    active_articles = self.get_elements_active_articles()
    return active_articles[number].find_element(By.TAG_NAME, 'h3').text
  
  def click_element_article_button(self, number):
    html = self.get_html()
    active_articles = self.get_elements_active_articles()
    active_articles[number].find_element(By.XPATH, './/div[2]/h3/a').click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))

  def get_text_new_page_header(self):
    return self.driver.find_element(By.XPATH, '/html/body/header/div/div/h1').text

  def get_text_article_article(self, number):
    active_articles = self.get_elements_active_articles()
    return active_articles[number].find_element(By.TAG_NAME, 'span').text
  
  def get_element_article_image(self, number):
    active_articles = self.get_elements_active_articles()
    return active_articles[number].find_element(By.TAG_NAME, 'img')
  
  def click_element_show_more_button(self):
    articles_section = self.get_element_section_articles()
    articles_section.find_element(By.CLASS_NAME, 'button.button--blue').click()
  
  def get_element_section_related_content(self):
    return self.driver.find_element(By.CLASS_NAME, 'related-content.background--gray   ')
  
  def get_text_related_header(self):
    related_section = self.get_element_section_related_content()
    return self.get_text_section_header(related_section)
  
  def get_text_related_body(self):
    related_section = self.get_element_section_related_content()
    return self.get_text_section_body(related_section)
  
  def get_elements_related_articles(self):
    related_section = self.get_element_section_related_content()
    return related_section.find_elements(By.TAG_NAME, 'article')
  
  def get_text_related_article_header(self, number):
    articles = self.get_elements_related_articles()
    return articles[number].find_element(By.TAG_NAME, 'h3').text
  
  def get_text_related_article_body(self, number):
    articles = self.get_elements_related_articles()
    return articles[number].find_element(By.TAG_NAME, 'p').text
  
  def click_element_related_article_button(self, number):
    html = self.get_html()
    articles = self.get_elements_related_articles()
    articles[number].find_element(By.TAG_NAME, 'a').click()
    if number != 2: # Third article button doesnt do anythign
      WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_element_aside(self):
    return self.driver.find_element(By.TAG_NAME, "aside")

  def get_text_aside_header(self):
    aside = self.get_element_aside()
    header = aside.find_element(By.TAG_NAME, 'h2')
    return header.text
  
  def get_text_aside_sub_header(self):
    aside = self.get_element_aside()
    sub_header = aside.find_element(By.TAG_NAME, 'p')
    return sub_header.text
  
  def click_element_aside_button_1(self):
    html = self.get_html()
    aside = self.get_element_aside()
    aside.find_element(By.XPATH, "/html/body/main/aside/div/div/div[2]/a[1]").click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def click_element_aside_button_2(self):
    html = self.get_html()
    aside = self.get_element_aside()
    aside.find_element(By.XPATH, "/html/body/main/aside/div/div/div[2]/a[2]").click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))