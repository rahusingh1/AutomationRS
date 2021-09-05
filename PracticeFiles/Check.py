import time
from selenium import webdriver

driver = webdriver.Chrome("/home/rahul/PycharmProjects/AutomationRS/drivers/chromedriver")

driver.get("https://rahulshettyacademy.com/seleniumPractise/")

driver.find_element_by_class_name("search-keyword").send_keys("ber")
time.sleep(5)
products = driver.find_elements_by_xpath("//div[@class='products']/div")
print(len(products))

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
# traverse up using xpath, script: //div[@class='product-action']/button/parent::div/parent::div/h4
A = []
for button in buttons:
    A.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
print(A)
driver.close()
