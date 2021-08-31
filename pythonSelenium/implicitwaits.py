import time

from selenium import webdriver

driver = webdriver.Chrome("/home/rahul/PycharmProjects/AutomationRS/drivers/chromedriver")

driver.get("https://rahulshettyacademy.com/seleniumPractise/")
# implicit wait
driver.implicitly_wait(5)

driver.find_element_by_css_selector(".search-keyword").send_keys("ber")
time.sleep(2)
products = driver.find_elements_by_xpath("//div[@class='products']/div")
count = len(products)
print(count)
assert count == 3

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    button.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
message = driver.find_element_by_css_selector(".promoInfo").text
print(message)
assert message == "Code applied ..!"
driver.close()