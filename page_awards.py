from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChainsdefec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_base import BasePage
import time  

class AwardsPage(BasePage):
  def get_text_main_header(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/header/div/div/h1')
    