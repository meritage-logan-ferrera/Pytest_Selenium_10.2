#Run Selenium tests in parallel with Python for Selenium Python tutorial
from appium.options.android import UiAutomator2Options
from appium import webdriver as appium_webdriver
from selenium import webdriver
import pytest

@pytest.fixture(params=["firefox", "chrome", "edge"], scope="class")
def init__driver(request):
  url = "http://localhost:4444/wd/hub"
  
  if request.param == "firefox":
    browser_options = webdriver.FirefoxOptions()
  if request.param == "chrome":
    browser_options = webdriver.ChromeOptions()
    browser_options.platform_name = "LINUX"
    # We use the below when we are doing normal selenium tests not on the grid
    ##################################################################################
    # web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    ##################################################################################
  if request.param == "edge":
    browser_options = webdriver.EdgeOptions()

  web_driver = webdriver.Remote(
      command_executor = url,
      options=browser_options
    ) 
  request.cls.driver = web_driver
  yield
  web_driver.quit()

@pytest.fixture(scope="class")
def driver_android_init(request):
  url = "http://localhost:4444/wd/hub"
  
  appium_options = UiAutomator2Options()
  appium_options.platform_name = "Android"
  appium_options.device_name = "emulator-5556"
  appium_options.automation_name = "UIAutomator2"
  appium_options.avd = "Nexus_5_API_30"
  appium_options.new_command_timeout = "200"
  appium_options.set_capability("browserName", "Chrome")
  web_driver = appium_webdriver.Remote(
    url, 
    options=appium_options
  )
  request.cls.driver = web_driver
  yield
  web_driver.quit()