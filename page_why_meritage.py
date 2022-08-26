from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_base import BasePage  

class WhyMeritagePage(BasePage):
  def get_text_header(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/header/div[1]/div/div/div/h1").text
  
  def get_text_sub_header(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/header/div[1]/div/div/div/span").text

  def click_element_play_button(self):
    self.driver.find_element(By.XPATH, "/html/body/main/header/div[1]/div/div/div/h1").click()
  
  def get_element_youtube_overlay(self):
    return self.driver.find_element(By.XPATH, "/html/body/div[4]")

  def get_element_article_1(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/article[1]")
  
  def get_element_article_1_image(self):
    article_1 = self.get_element_article_1()
    return article_1.find_element(By.XPATH, "/html/body/main/article[1]/div/div[2]/div/img")

  def get_text_article_1_header(self):
    article_1 = self.get_element_article_1()
    return article_1.find_element(By.XPATH, "/html/body/main/article[1]/header/div/h2").text

  def get_text_article_1_text(self):
    article_1 = self.get_element_article_1()
    return article_1.find_element(By.XPATH, "/html/body/main/article[1]/div/div[1]/p[1]")
  
  def click_element_article_1_button(self):
    html = BasePage(self.driver).get_html()
    article_1 = self.get_element_article_1()
    button = article_1.find_element(By.XPATH, "/html/body/main/article[1]/div/div[1]/p[2]/a")
    button.click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_element_section_1(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/section")
  
  def get_element_section_1_drop_down_container(self, number):
    section_1 = self.get_element_section_1()
    return section_1.find_element(By.XPATH, f"/html/body/main/section/div/div[2]/div/ul[1]/li[{number}]")
  
  def get_element_section_1_drop_down_container_image(self, number):
    container = self.get_element_section_1_drop_down_container(number)
    return container.find_element(By.TAG_NAME, "img")
  
  def get_element_section_1_drop_down_container_header(self, number):
    container = self.get_element_section_1_drop_down_container(number)
    return container.find_element(By.TAG_NAME, "span")
  
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
    return tab.find_element(By.TAG_NAME, "h2").text
  
  def get_elements_section_1_responsive_tab_body(self, number):
    tab = self.get_element_section_1_responsive_tab(number)
    return tab.find_elements(By.TAG_NAME, "p")
  
  def click_element_section_1_responsive_tab_button(self, number):
    html = BasePage(self.driver).get_html()
    tab = self.get_element_section_1_responsive_tab(number)
    tab.find_element(By.CLASS_NAME, "button.button--blue").click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_element_section_1_responsive_tab_image(self, number):
    tab = self.get_element_section_1_responsive_tab(number)
    return tab.find_element(By.TAG_NAME, "img")
  
  # Need to write code similar to this from now on it is much easier
  def get_elements_chat_articles(self):
    return self.driver.find_elements(By.ID, "chat") # change to contains class = thing
  
  def get_text_article_chat_header(self, number):
    chat_articles = self.get_elements_chat_articles()
    header = chat_articles[number].find_element(By.TAG_NAME, "h2")
    return header.text

  def get_text_article_chat_sub_header(self, number):
    chat_articles = self.get_elements_chat_articles()
    sub_header = chat_articles[number].find_element(By.TAG_NAME, "p")
    return sub_header.text
  
  def get_text_article_chat_image(self, number):
    chat_articles = self.get_elements_chat_articles()
    return chat_articles[number].find_element(By.TAG_NAME, "img")
  
  def click_element_article_chat_button(self, number):
    chat_articles = self.get_elements_chat_articles()
    chat_articles[number].find_element(By.CLASS_NAME, "button.button--blue")