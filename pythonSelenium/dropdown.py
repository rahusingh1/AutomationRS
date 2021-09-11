from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("/home/rahul/PycharmProjects/AutomationRS/drivers/chromedriver")

driver.get("https://www.rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("rahul")

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1")) #only use if tag name is select
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
#dropdown.select_by_value("M") # it works only if the value is present in that tag.

driver.find_element_by_css_selector("input[type='submit']").click()

driver.close()
