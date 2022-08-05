#Run Selenium tests in parallel with Python for Selenium Python tutorial
from re import S
from dotenv import load_dotenv
import pytest
import os

from selenium import webdriver
load_dotenv()
@pytest.fixture(scope="class")
def driver_chrome_init(request):
    url = "http://localhost:4444/wd/hub"
    browser_options = webdriver.ChromeOptions()
    #browser_options.headless = True
    #web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    web_driver = webdriver.Remote(
      command_executor = url,
      options = browser_options
    )
    request.cls.driver = web_driver
    yield
    web_driver.quit()
    
@pytest.fixture(scope="class")
def driver_firefox_init(request):
    os.environ["Path"] += os.pathsep + 'C:\\Users\\logan.ferrera\\Desktop\\geckodriver-v0.27.0-win64\\geckodriver.exe'
    url = "http://localhost:4444/wd/hub"
    browser_options = webdriver.FirefoxOptions()
    web_driver = webdriver.Remote(
      command_executor = url,
      options=browser_options
    )
    request.cls.driver = web_driver
    yield
    web_driver.quit()
  
@pytest.fixture(scope="class")
def driver_edge_init(request):
  url = "http://localhost:4444/wd/hub"
  browser_options = webdriver.EdgeOptions()
  #browser_options.headless = True
  #web_driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager.install()))
  web_driver = webdriver.Remote(
    command_executor = url,
    options = browser_options,
  )
  request.cls.driver = web_driver
  yield
  web_driver.quit()