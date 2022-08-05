#Run Selenium tests in parallel with Python for Selenium Python tutorial
from re import S
from dotenv import load_dotenv
import pytest
import os
import selenium.webdriver.firefox.service as service1
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.remote.remote_connection import RemoteConnection
import sys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

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
    web_driver.close()
    
@pytest.fixture(scope="class")
def driver_firefox_init(request):
    os.environ["Path"] += os.pathsep + 'C:\\Users\\logan.ferrera\\Desktop\\geckodriver-v0.27.0-win64\\geckodriver.exe'
    url = "http://localhost:4444/wd/hub"
    browser_options = webdriver.FirefoxOptions()
    #browser_options.accept_insecure_certs = False
    #browser_options.set_capability("browserName", "firefox")
    browser_options.set_capability("browserVersion", 102.0)
    #browser_options.set_capability("os", "Windows")
    #browser_options.set_capability("osVersion", "10")
    browser_options.set_capability("marionette", True)
    #browser_options.binary_location = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
    #browser_options.default_capabilities
    # browser_options.BrowserExecutableLocation = "/usr/bin/firefox" https://github.com/SeleniumHQ/selenium/issues/4498
    #browser_options.headless = True
    #binary1 = FirefoxBinary("C:/Program Files/Mozilla Firefox")
    # browser_options.binary_location = "C:/Users/logan.ferrera/AppData/Local/Programs/Python/Python310/geckodriver.exe"
    #browser_options.binary = binary1
    #web_driver = webdriver.Firefox(service=Service(GeckoDriverManager.install()))
    #service = service1.Service('C:/Users/logan.ferrera/AppData/Local/Programs/Python/Python310/geckodriver.exe')
    #service.start()
    #capabilities = {'firefox.binary': "C:/Users/logan.ferrera/AppData/Local/Programs/Python/Python310/geckodriver.exe"}
    web_driver = webdriver.Remote(
      command_executor = url,
      options=browser_options
    )
    request.cls.driver = web_driver
    yield
    web_driver.close()
  
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
  web_driver.close()