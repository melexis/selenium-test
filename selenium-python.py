# To install the Python client library:
# pip install -U selenium

# Import the Selenium 2 namespace (aka "webdriver")
from selenium import webdriver


# Google Chrome 
#driver = webdriver.Chrome()

# Firefox 
#driver = webdriver.Firefox()

# Remote
fp = webdriver.FirefoxProfile()
# set something on the profile...
#driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.FIREFOX, browser_profile=fp)
driver = webdriver.Remote(command_executor="http://hudson2-test.colo.elex.be:4444/wd/hub",
	desired_capabilities=webdriver.DesiredCapabilities.FIREFOX, 
	browser_profile=fp)

# ------------------------------
# The actual test scenario: Test the codepad.org code execution service.

# Go to codepad.org
driver.get('http://codepad.org')

# Select the Python language option
python_link = driver.find_elements_by_xpath("//input[@name='lang' and @value='Python']")[0]
python_link.click()

# Enter some text!
text_area = driver.find_element_by_id('textarea')
text_area.send_keys("print 'Hello,' + ' World!'")

# Submit the form!
submit_button = driver.find_element_by_name('submit')
submit_button.click()

# Make this an actual test. Isn't Python beautiful?
assert "Hello, World!" in driver.page_source

# Close the browser!
driver.quit()