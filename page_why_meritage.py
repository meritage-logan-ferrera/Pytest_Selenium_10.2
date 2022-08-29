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
    return article_1.find_element(By.XPATH, "/html/body/main/article[1]/div/div[1]/p[1]").text
  
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
  
  def get_element_chat_articles(self, number):
    return self.driver.find_element(By.CSS_SELECTOR, f'article.large-two-column:nth-child({number + 4})')
  
  def get_text_article_chat_header(self, number):
    chat_article = self.get_element_chat_articles(number)
    header = chat_article.find_element(By.TAG_NAME, "h2")
    return header.text

  def get_text_article_chat_sub_header(self, number):
    chat_article = self.get_element_chat_articles(number)
    sub_header = chat_article.find_element(By.CSS_SELECTOR, 'div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > p:nth-child(3)')
    return sub_header.text

  def get_element_article_chat_image(self, number):
    chat_article = self.get_element_chat_articles(number)
    return chat_article.find_element(By.TAG_NAME, "img")
  
  def click_element_article_chat_button(self, number):
    html = BasePage(self.driver).get_html()
    chat_article = self.get_element_chat_articles(number)
    button = chat_article.find_element(By.CLASS_NAME, "button.button--blue")
    button.click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_element_article_6_meritage_cares(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/article[6]')
  
  def get_text_article_6_header_1(self):
    article_6 = self.get_element_article_6_meritage_cares()
    return article_6.find_element(By.TAG_NAME, 'h2').text
  
  def get_text_article_6_sub_header_1(self):
    article_6 = self.get_element_article_6_meritage_cares()
    return article_6.find_element(By.CSS_SELECTOR, 'header:nth-child(1) > div:nth-child(1) > p:nth-child(2)').text

  def get_text_article_6_header_2(self):
    article_6 = self.get_element_article_6_meritage_cares()
    return article_6.find_element(By.TAG_NAME, 'h4').text
  
  def get_text_article_6_sub_header_2(self):
    article_6 = self.get_element_article_6_meritage_cares()
    return article_6.find_element(By.CSS_SELECTOR, 'div:nth-child(2) > div:nth-child(1) > p:nth-child(2)').text
  
  def get_element_article_6_image(self):
    article_6 = self.get_element_article_6_meritage_cares()
    return article_6.find_element(By.TAG_NAME, 'img')
  
  def click_element_article_6_button(self):
    html = BasePage(self.driver).get_html()
    article_6 = self.get_element_article_6_meritage_cares()
    article_6.find_element(By.TAG_NAME, 'a').click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_element_article_7(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/article[7]')
  
  def get_text_article_7_header(self):
    article_7 = self.get_element_article_7()
    header = article_7.find_element(By.TAG_NAME, 'h2')
    return header.text
  
  def get_text_article_7_sub_header(self):
    article_7 = self.get_element_article_7()
    sub_header = article_7.find_element(By.CSS_SELECTOR, 'div:nth-child(2) > div:nth-child(1) > p:nth-child(2)')
    return sub_header.text
  
  def get_elements_article_7_list(self):
    article_7 = self.get_element_article_7()
    return article_7.find_elements(By.TAG_NAME, 'li')
  
  def click_element_article_7_button(self):
    html = BasePage(self.driver).get_html()
    article_7 = self.get_element_article_7()
    button = article_7.find_element(By.TAG_NAME, 'a')
    button.click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_element_article_7_image(self):
    article_7 = self.get_element_article_7()
    return article_7.find_element(By.TAG_NAME, 'img')
  
  def get_element_article_8(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/article[8]')

  def get_text_article_8_header(self):
    article_8 = self.get_element_article_8()
    header = article_8.find_element(By.TAG_NAME, 'h4')
    return header.text
  
  def get_text_article_8_sub_header(self):
    article_8 = self.get_element_article_8()
    sub_header = article_8.find_element(By.CSS_SELECTOR, 'div:nth-child(1) > div:nth-child(1) > p:nth-child(2)')
    return sub_header.text
  
  def click_element_article_8_button(self):
    html = BasePage(self.driver).get_html()
    article_8 = self.get_element_article_8()
    button = article_8.find_element(By.TAG_NAME, 'a')
    button.click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))

  def get_element_article_8_image(self):
    article_8 = self.get_element_article_8()
    return article_8.find_element(By.TAG_NAME, 'img')
  
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
    aside = self.get_element_aside()
    aside.find_element(By.XPATH, "/html/body/main/aside/div/div/div[2]/a[1]").click()
  
  def click_element_aside_button_2(self):
    aside = self.get_element_aside()
    aside.find_element(By.XPATH, "/html/body/main/aside/div/div/div[2]/a[2]").click()
  
  # I can definitely cut some of this code down by using some common functions. Will begin to do this for later pages. I will add the functions ot BasePage.