from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_base import BasePage  

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
    header = article_2.find_element(By.XPATH, "/html/body/main/article[2]/div/div/div[1]/div/h2")
    return header.text
  
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
    header = article_3.find_element(By.XPATH, "/html/body/main/article[3]/div/div[2]/p/span")
    return header.text

  def click_element_article_3_button(self):
    article_3 = self.get_element_article_3_military()
    article_3_button = article_3.find_element(By.XPATH, "/html/body/main/article[3]/div/div[2]/a")
    article_3_button.click()
  
  def get_element_article_4_expect_more(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/article[4]")
  
  def get_text_article_4_header(self):
    article_4 = self.get_element_article_4_expect_more()
    header = article_4.find_element(By.XPATH, "/html/body/main/article[4]/div/div/div[1]/div/h2")
    return header.text
  
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
    header = container.find_element(By.TAG_NAME, "h3")
    return header.text
  
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
    return carousel.find_element(By.XPATH, f"//div[@data-slide='{number}']/img")

  def get_text_article_5_header(self):
    article_5 = self.get_element_article_5_welcome_home()
    header = article_5.find_element(By.XPATH, "/html/body/main/article[5]/div/div[2]/div/div[2]/h2")
    return header.text
  
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
    header = article_6.find_element(By.TAG_NAME, "h2")
    return header.text

  def get_element_article_6_partner_image(self):
    article_6 = self.get_element_article_6_awards()
    return article_6.find_element(By.XPATH, "/html/body/main/article[6]/div/div/div[2]/div[1]/img")
  
  def get_element_article_6_avid_image(self):
    article_6 = self.get_element_article_6_awards()
    return article_6.find_element(By.XPATH, "/html/body/main/article[6]/div/div/div[2]/div[2]/img")

  def get_element_article_7_search_smarter(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/article[7]")

  def get_text_article_7_header(self):
    article_7 = self.get_element_article_7_search_smarter()
    header = article_7.find_element(By.TAG_NAME, "h2")
    return header.text

  def get_element_article_7_image_container_1(self):
    article_7 = self.get_element_article_7_search_smarter()
    return article_7.find_element(By.XPATH, "/html/body/main/article[7]/div/div[2]/div/div[1]")

  def get_element_article_7_image_container_2(self):
    article_7 = self.get_element_article_7_search_smarter()
    return article_7.find_element(By.XPATH, "/html/body/main/article[7]/div/div[2]/div/div[2]")
  
  # Should I paramaterize the above two functions into one???
  def get_text_article_7_image_container_1_header(self):
    container = self.get_element_article_7_image_container_1()
    header = container.find_element(By.TAG_NAME, "h4")
    return header.text

  def get_text_article_7_image_container_2_header(self):
    container = self.get_element_article_7_image_container_2()
    header = container.find_element(By.TAG_NAME, "h4")
    return header.text

  def click_element_article_7_image_container_1(self):
    html = BasePage(self.driver).get_html()
    image_container_1 = self.get_element_article_7_image_container_1()
    image_container_1.click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))

  def click_element_article_7_image_container_2(self):
    html = BasePage(self.driver).get_html()
    image_container_2 = self.get_element_article_7_image_container_2()
    image_container_2.click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def click_element_article_7_button(self):
    html = BasePage(self.driver).get_html()
    article_7 = self.get_element_article_7_search_smarter()
    button = article_7.find_element(By.XPATH, "/html/body/main/article[7]/div/div[1]/a")
    button.click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))

  def get_element_aside_2_ready_to_find(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/aside[2]")
  
  def get_text_aside_2_header(self):
    aside_2 = self.get_element_aside_2_ready_to_find()
    header = aside_2.find_element(By.TAG_NAME, "h2")
    return header.text
  
  def get_text_aside_2_subtext(self):
    aside_2 = self.get_element_aside_2_ready_to_find()
    header = aside_2.find_element(By.TAG_NAME, "p")
    return header.text

  def click_element_aside_2_button(self):
    html = BasePage(self.driver).get_html()
    aside_2 = self.get_element_aside_2_ready_to_find()
    button = aside_2.find_element(By.TAG_NAME, "a")
    button.click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
