from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_base import BasePage
import time  

class ReviewsPage(BasePage):
  def get_text_main_header(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/header/div/div/h1")
  
  # Need to find a way to get image when it is hard coded as CSS style bacgkorund image. Same problem for the main image on the state pages
  def get_element_main_image(self):
    return self.driver.find_element(By.XPATH, "")
  
  # The section below contains a few different views that are dynamic:
  # 1. The default view
  # 2. The view when "Write a Review" is selected
  # 3. The view when the pencil icon is selected inside view 2
  def get_element_reviews_summary_section(self):
    return self.driver.find_element(By.XPATH, "/html/body/div[1]/div")

  ################# View 1 (default) Elements ######################
  # Get view 1 element, run tests on its children elements and on whether this is hidden or not depending on if the "Write a review" button was pressed. This is visible until that button is pressed.
  def get_element_reviews_summary_view_1(self):
    return self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]")

  def get_text_reviews_summary_header(self):
    reviews_summary = self.get_element_reviews_summary_view_1()
    return reviews_summary.find_element(By.TAG_NAME).text
  
  def get_elements_reviews_summary_rating_value(self):
    reviews_summary = self.get_element_reviews_summary_view_1()
    elements = reviews_summary.find_elements(By.CLASS_NAME, "ratingval")
    numbers = []
    for i, element in enumerate(elements):
      numbers[i] = element.text
    return numbers
  
  def get_elements_reviews_summary_stars(self):
    reviews_summary = self.get_element_reviews_summary_view_1()
    return reviews_summary.find_elements(By.CLASS_NAME, "starOn")
    # assert there are 5 stars
  
  def get_text_review_summary_rating(self):
    reviews_summary = self.get_element_reviews_summary_view_1()
    return reviews_summary.find_element(By.CLASS_NAME, "be-c-ratingval").text
    # assert is rational number?
  
  def get_elements_review_summary_rating_stars(self):
    reviews_summary = self.get_element_reviews_summary_view_1()
    return reviews_summary.find_elements(By.CLASS_NAME, "be-c-star")
    # assert there are 5 stars
  
  def get_text_review_summary_reviews_number(self):
    reviews_summary = self.get_element_reviews_summary_view_1()
    return reviews_summary.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div/div/div[2]/div/div[2]/div[2]")
    # assert reviews in string
  
  def click_element_review_summary_write_review_button(self):
    reviews_summary = self.get_element_reviews_summary_view_1()
    reviews_summary.find_element(By.ID, "btnWriteAReview")
    #clicking opens view 2
  
  ################## View 2 Elements #######################
  # Get view 2 element, run tests on its children elements and on whether this is hidden or not depending on if the "Write a review" button was pressed. This is hidden until that button is pressed.
  def get_element_review_summary_view_2(self):
    return self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]")
    # this becomes unhidden when write a review button is pressed

  def get_text_review_summary_view_2_header(self):
    view_2 = self.get_element_review_summary_view_2()
    return view_2.find_element(By.TAG_NAME, 'h2').text
  
  def get_text_review_summary_view_2_sub_header(self):
    view_2 = self.get_element_review_summary_view_2()
    return view_2.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div/div[1]').text
  
  def click_element_review_summary_view_2_google_button(self):
    original_window = self.driver.current_window_handle
    view_2 = self.get_element_review_summary_view_2()
    view_2.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div/div[2]/a[1]').click()
    self.new_tab(original_window)
    # clicking button opens a new tab

  def click_element_review_summary_view_2_pencil_button(self):
    view_2 = self.get_element_review_summary_view_2()
    view_2.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div/div[2]/a[2]").click()
    # switches to view 3

  ######################### View 3 Elements #############################
  # Get view 3 element, run tests on its children elements and on whether this is hidden or not depending on if the pencil button was pressed inside of view 2. This is hidden until thaose buttons are pressed.
  def get_element_review_summary_view_write_review_pencil_view(self):
    reviews_summary = self.get_element_reviews_summary_section()
    return reviews_summary.find_element(By.ID, "reviewFormWrapper")
    # unhidden after the write a review button AND then the pencil button is clicked
  

  

