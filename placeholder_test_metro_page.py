import pytest
from header_tests import Test_Header_Element_Visibility as test_header
from footer_tests import Test_Footer_Element_Visibility as test_footer
@pytest.mark.usefixtures("init__driver")
class BasicTest(test_footer, test_header):
  pass

class Test_Metro_Phoenix(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get('https://www.meritagehomes.com/state/az/phoenix')
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)
  
class Test_Metro_Tucson(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get('https://www.meritagehomes.com/state/az/tucson')
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)
  
class Test_Metro_Bay_Area(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get('https://www.meritagehomes.com/state/ca/bay-area')
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)

class Test_Metro_Bay_Area(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get('https://www.meritagehomes.com/state/ca/bay-area')
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)
  
class Test_Metro_Sacramento(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get('https://www.meritagehomes.com/state/ca/sacramento')
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)
  
class Test_Metro_Southern_CA(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get('https://www.meritagehomes.com/state/ca/southern-ca')
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)

class Test_Metro_Denver(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get('https://www.meritagehomes.com/state/co/denver')
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)

class Test_Metro_Orlando(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get('https://www.meritagehomes.com/state/fl/orlando')
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)

class Test_Metro_Tampa(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get('https://www.meritagehomes.com/state/fl/tampa')
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)

class Test_Metro_South_Florida(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get('https://www.meritagehomes.com/state/fl/south-florida')
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)

class Test_Metro_Atlanta(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get('https://www.meritagehomes.com/state/ga/atlanta')
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)

class Test_Metro_Charlotte(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get('https://www.meritagehomes.com/state/nc/charlotte')
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)

class Test_Metro_Raleigh(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get('https://www.meritagehomes.com/state/nc/raleigh')
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)

class Test_Metro_Greenville(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get('https://www.meritagehomes.com/state/sc/greenville')
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)

class Test_Metro_York_County(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get('https://www.meritagehomes.com/state/sc/york-county')
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)

class Test_Metro_Myrtle_Beach(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get('https://www.meritagehomes.com/state/sc/myrtle-beach')
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)

class Test_Metro_Nashville(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get('https://www.meritagehomes.com/state/tn/nashville')
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)

class Test_Metro_Austin(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get('https://www.meritagehomes.com/state/tx/austin')
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)

class Test_Metro_Dallas_Ft_Worth(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get('https://www.meritagehomes.com/state/tx/dallasft-worth')
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)

class Test_Metro_Houston(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get('https://www.meritagehomes.com/state/tx/houston')
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)

class Test_Metro_San_Antonio(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get('https://www.meritagehomes.com/state/tx/san-antonio')
    self.driver.set_window_position(0,0)
    self.driver.set_window_size(1920,1080)