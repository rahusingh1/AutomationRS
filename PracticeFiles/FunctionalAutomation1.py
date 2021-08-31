# Validate whether products selected in page1 are showing in page 2 check page.
import time
from selenium import webdriver

driver = webdriver.Chrome("/home/rahul/PycharmProjects/AutomationRS/drivers/chromedriver")

driver.get("https://rahulshettyacademy.com/seleniumPractise/")

driver.find_element_by_class_name("search-keyword").send_keys("ber")
time.sleep(5)
products = driver.find_elements_by_xpath("//div[@class='products']/div")
print(len(products))
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    button.click()

items = driver.find_elements_by_xpath("//h4[@class='product-name']")
for item in items:
    print(item.text)

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

lists = driver.find_elements_by_xpath("//p[@class='product-name']")
for list1 in lists:
    print(list1.text)

#assert lists == items

driver.close()