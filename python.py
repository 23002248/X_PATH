from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

# TC01 - Open registration page
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
driver.maximize_window()
time.sleep(2)

# TC02 - Locate username using Attribute XPath
username = driver.find_element(By.XPATH, "//input[@name='my-text']")
username.send_keys("Stephen Raj")

# TC03 - Enter password using Attribute XPath
password = driver.find_element(By.XPATH, "//input[@type='password']")
password.send_keys("Stephen@123")

# TC04 - Locate Submit using text()
submit = driver.find_element(By.XPATH, "//button[text()='Submit']")

# TC05 - Locate textbox dynamically using contains()
textbox = driver.find_element(By.XPATH, "//input[contains(@name,'my-text')]")

# TC06 - Locate element using starts-with()
start_element = driver.find_element(By.XPATH, "//input[starts-with(@name,'my-')]")

# TC07 - Find input using two attributes with and
two_attributes = driver.find_element(
    By.XPATH, "//input[@name='my-text' and @type='text']"
)

# TC08 - Find element using alternatives with or
alternative = driver.find_element(
    By.XPATH, "//input[@name='my-text' or @name='my-password']"
)

# TC09 - Find parent form
parent_form = driver.find_element(
    By.XPATH, "//input[@name='my-text']/parent::form"
)

# TC10 - Find form from input using ancestor
ancestor_form = driver.find_element(
    By.XPATH, "//input[@name='my-text']/ancestor::form"
)

# TC11 - Find child inputs
child_inputs = driver.find_elements(
    By.XPATH, "//form/child::input"
)

# TC12 - Find next element using following
following_element = driver.find_element(
    By.XPATH, "//input[@name='my-text']/following::input[1]"
)

# TC13 - Find checkbox
checkbox = driver.find_element(
    By.XPATH, "//input[@type='checkbox']"
)
checkbox.click()

# TC14 - Find radio button
radio = driver.find_element(
    By.XPATH, "//input[@type='radio']"
)
radio.click()

# TC15 - Select dropdown using XPath + Select
dropdown = driver.find_element(
    By.XPATH, "//select[@name='my-select']"
)
select = Select(dropdown)
select.select_by_visible_text("Two")

# TC16 - Find second textbox using XPath index
second_textbox = driver.find_element(
    By.XPATH, "(//input[@type='text'])[2]"
)

# TC17 - Verify submitted message
submit.click()
time.sleep(2)

message = driver.find_element(
    By.XPATH, "//h1[text()='Form submitted']"
)

print("TC17 - Submitted Message:", message.text)

# TC18 - Find all input fields
all_inputs = driver.find_elements(By.XPATH, "//input")

print("TC18 - Total input fields:", len(all_inputs))

# TC19 - Find dynamic element using contains()
dynamic_element = driver.find_element(
    By.XPATH, "//input[contains(@name,'my-')]"
)

print("TC19 - Dynamic element found successfully")

# TC20 - Complete registration automation
print("TC20 - Registration automation completed successfully")

time.sleep(3)

driver.quit()