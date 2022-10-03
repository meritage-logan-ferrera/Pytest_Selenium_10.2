from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_base import BasePage  

class CommunityPage(BasePage):
  def get_element_image_carousel(self):
    return self.driver.find_element(By.XPATH, ".//div[contains(@class,'carousel-hero')]")
  
  def click_element_next_arrow(self):
    carousel_section = self.get_element_image_carousel()
    carousel_section.find_element(By.CLASS_NAME, 'orbit-next.slick-arrow').click()
  
  def get_elements_carousel_slides(self):
    carousel_section = self.get_element_image_carousel()
    slides = carousel_section.find_elements(By.XPATH, ".//li[contains(@class, 'slick-slide') and not(contains(@class, 'slick-cloned'))]")
    return slides
  
  def get_element_current_slide(self):
    carousel_section = self.get_element_image_carousel()
    return carousel_section.find_element(By.XPATH, ".//li[contains(@class, 'is-active')]")
  
  def get_element_slide_number(self, number):
    carousel_section = self.get_element_image_carousel()
    slides = self.get_elements_carousel_slides()
    return slides[number]
  
  def get_element_compare(self):
    carousel_section = self.get_element_image_carousel()
    return carousel_section.find_element(By.CLASS_NAME, 'trigger-compare.top.has-tip')
  
  def get_element_heart(self):
    carousel_section = self.get_element_image_carousel()
    return carousel_section.find_element(By.CLASS_NAME, 'add-community-favorite')
  
  def get_element_article(self):
    return self.driver.find_element(By.CLASS_NAME, 'small-12.medium-10.large-8.column.text-center')
  
  def get_text_main_header(self):
    article = self.get_element_article()
    return article.find_element(By.TAG_NAME, 'h1').text
  
  def get_text_main_body(self):
    article = self.get_element_article()
    return article.find_element(By.TAG_NAME, 'p').text
  
  def get_element_aside(self):
    return self.driver.find_element(By.CLASS_NAME, 'multi-column-info.has-dividers')
  
  def get_text_aside(self):
    aside = self.get_element_aside()
    return aside.text
  
  def get_element_brochure(self):
    return self.driver.find_element(By.XPATH, "//div[@class='small-12 columns text-center']/a")
  
  def get_element_section_tabs(self):
    return self.driver.find_element(By.CLASS_NAME, 'tabbed-accordion    ')
  
  def get_text_tabs_header(self):
    tabs_section = self.get_element_section_tabs()
    return tabs_section.find_element(By.TAG_NAME, 'h2').text
  
  def get_text_tabs_body(self):
    tabs_section = self.get_element_section_tabs()
    return tabs_section.find_element(By.TAG_NAME, 'p').text
  
  def get_elements_tabs(self):
    tabs_section = self.get_element_section_tabs()
    tabs_container = tabs_section.find_element(By.XPATH, ".//ul[contains(@id, 'tab-container')]")
    return tabs_container.find_elements(By.TAG_NAME, 'li')
  
  def get_element_tab_image(self, number):
    tabs = self.get_elements_tabs()
    return tabs[number].find_element(By.TAG_NAME, 'img')
    # test with naturalWidth not width since width includes width if alt text is displayed
  
  def get_text_tab_name(self, number):
    tabs = self.get_elements_tabs()
    return tabs[number].find_element(By.TAG_NAME, 'span').text
  
  def click_element_tab(self, number):
    tabs = self.get_elements_tabs()
    tabs[number].click()

  def get_element_active_info_tab(self, number):
    tabs_section = self.get_element_section_tabs()
    info_tab_container = tabs_section.find_element(By.CLASS_NAME, 'responsive-tabs.tabs-content')
    return info_tab_container.find_element(By.XPATH, f".//li[{number}]")
  
  def get_element_info_tab_overview(self):
    return self.get_element_active_info_tab(1)
  
  def get_text_community_address(self):
    overview_info_tab = self.get_element_info_tab_overview()
    return overview_info_tab.find_element(By.XPATH, ".//p[@v-if='community']").text
    # string includes mroe than just a comma
  
  def get_element_directions_link(self):
    overview_info_tab = self.get_element_info_tab_overview()
    return overview_info_tab.find_element(By.XPATH, './/div/section/div/div/div[2]/div/div[1]/a')
  
  def get_text_below_directions(self):
    overview_info_tab = self.get_element_info_tab_overview()
    return overview_info_tab.find_element(By.XPATH, './/div/section/div/div/div[2]/div/div[1]/p[2]').text
    #assert string is not empty

  def get_text_hoa(self):
    overview_info_tab = self.get_element_info_tab_overview()
    return overview_info_tab.find_element(By.XPATH, './/div/section/div/div/div[2]/div/div[1]/div[1]/div[1]/strong')
  
  def get_text_tax_rate(self):
    overview_info_tab = self.get_element_info_tab_overview()
    return overview_info_tab.find_element(By.XPATH, './/div/section/div/div/div[2]/div/div[1]/div[1]/div[2]/strong')
  
  def get_text_hoa_dynamic(self):
    overview_info_tab = self.get_element_info_tab_overview()
    return overview_info_tab.find_element(By.XPATH, './/div/section/div/div/div[2]/div/div[1]/div[2]/div[1]/p')
  
  def get_text_tax_rate_dynamic(self):
    overview_info_tab = self.get_element_info_tab_overview()
    return overview_info_tab.find_element(By.XPATH, './/div/section/div/div/div[2]/div/div[1]/div[2]/div[2]/p')
  
  def get_text_sales_counselors(self):
    overview_info_tab = self.get_element_info_tab_overview()
    return overview_info_tab.find_element(By.XPATH, './/div/section/div/div/div[2]/div/div[2]/strong')
  
  def get_element_info_tab_our_floorplans(self):
    return self.get_element_active_info_tab(2)
  
  def get_elements_floorplans(self):
    floorplans_info_tab = self.get_element_info_tab_our_floorplans()
    floorplans_container = floorplans_info_tab.find_element(By.XPATH, './/div/section/div[2]')
    return floorplans_container.find_elements(By.XPATH, './div')
  
  def get_element_floorplan_image(self, number):
    floorplans = self.get_elements_floorplans()
    return floorplans[number].find_element(By.TAG_NAME, 'img')
  
  def get_text_floorplan_snipe_overlay(self, number):
    floorplans = self.get_elements_floorplans()
    return floorplans[number].find_element(By.TAG_NAME, 'span').text
    # assert != ''
  
  def get_element_floorplan_name(self, number):
    floorplans = self.get_elements_floorplans()
    return floorplans[number].find_element(By.XPATH, ".//a[contains(@href, '/state')]")
  
  def get_text_floorplan_name(self, number):
    name_element = self.get_element_floorplan_name(number)
    return name_element.text

  def click_element_floorplan_name(self, number):
    html = self.get_html()
    name_element = self.get_element_floorplan_name(number)
    name_element.click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))
  
  def get_element_info_tab_qmis(self):
    return self.get_element_active_info_tab(3)
  
  def get_elements_qmis(self):
    qmis_info_tab = self.get_element_info_tab_qmis()
    qmis_container = qmis_info_tab.find_element(By.XPATH, './/div/section/div[2]')
    return qmis_container.find_elements(By.XPATH, './div')
  
  def get_element_qmi_image(self, number):
    qmis = self.get_elements_qmis()
    return qmis[number].find_element(By.TAG_NAME, 'img')
  
  def get_element_qmi_name(self, number):
    qmis = self.get_elements_qmis()
    return qmis[number].find_element(By.XPATH, ".//a[contains(@href, '/state')]")
  
  def get_text_qmi_plan(self, number):
    qmis = self.get_elements_qmis()
    plan_number = qmis[number].find_element(By.CLASS_NAME, 'plan-number')
    return plan_number.text
  
  # This is getting the element inside of the specfic QMI page and breaks the page object model.
  def get_new_page_qmi_plan_number(self):
    article = self.get_section_by_aria_label('article', 'overview B article')
    return article.find_element(By.TAG_NAME, 'p').text

  def click_element_qmi_name(self, number):
    html = self.get_html()
    name_element = self.get_element_qmi_name(number)
    name_element.click()
    WebDriverWait(self.driver, timeout=3).until(EC.staleness_of(html))

  def get_element_info_tab_community(self):
    return self.get_element_active_info_tab(4)

  def get_elements_community_rows(self):
    communities_info_tab = self.get_element_info_tab_community()
    return communities_info_tab.find_elements(By.TAG_NAME, 'article')
  
  def get_element_row_image(self, number):
    rows = self.get_elements_community_rows()
    return rows[number].find_element(By.TAG_NAME, 'img')
    
  def get_element_info_tab_homesite(self):
    return self.get_element_active_info_tab(5)
  
  def check_clickable_homesite_button(self):
    homesite_info_tab = self.get_element_info_tab_homesite()
    button = homesite_info_tab.find_element(By.XPATH, './/div/section/a')
    return self.button_is_clickable(button)
  
  def get_element_iframe(self):
    homesite_info_tab = self.get_element_info_tab_homesite()
    return homesite_info_tab.find_element(By.XPATH, './/div/section/iframe')

  def get_element_info_tab_video(self):
    return self.get_element_active_info_tab(6)

  def get_element_video_iframe(self):
    video_info_tab = self.get_element_info_tab_video()
    return video_info_tab.find_element(By.TAG_NAME, 'iframe')

  def get_aside_stay_up_to_date(self):
    return self.get_section_by_aria_label('aside', 'Interest list sign up form')
  
  def click_element_homebuyer_button(self):
    stay_section = self.get_aside_stay_up_to_date()
    stay_section.find_element(By.XPATH, './/div[1]/div/form/div[1]/div/div[1]/label')
  
  def click_element_agent_button(self):
    stay_section = self.get_aside_stay_up_to_date()
    stay_section.find_element(By.XPATH, './/div[1]/div/form/div[1]/div/div[2]/label')
  
  def check_aside_button_clickable(self):
    stay_section = self.get_aside_stay_up_to_date()
    button = stay_section.find_element(By.XPATH, './/div[1]/div/form/div[3]/div[4]/button')
    return self.button_is_clickable(button)
