import time
from selenium import webdriver

driver = webdriver.Chrome("/home/rahul/PycharmProjects/AutomationRS/drivers/chromedriver")
driver.get("https://www.rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("hello")
print(driver.find_element_by_name("name").text) # not print anything
print(driver.find_element_by_name("name").get_attribute("value"))  # print the entered text by script

# fully accessed by the javascript DOM/document, execute_script give access to js to enter js code in argument and
# access the element and get data or perform action.
print(driver.execute_script("return document.getElementsByName('name')[0].value"))

shopbutton = driver.find_element_by_css_selector("a[href*='shop']")

driver.execute_script("arguments[0].click();", shopbutton)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(1)
driver.close()