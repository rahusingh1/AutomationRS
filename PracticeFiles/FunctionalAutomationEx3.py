# Validate whether products selected in page1 are showing in page 2 check page.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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
print("ListA: ", A)
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(3)

lists = driver.find_elements_by_xpath("//p[@class='product-name']")
#lists = driver.find_elements_by_css_selector("p.product-name")
B = []
for veg in lists:
    B.append(veg.text)
    print(veg.text)
print("ListB: ", B)

assert A == B

Before = driver.find_element_by_css_selector(".discountAmt").text
print(Before)

driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

After = driver.find_element_by_css_selector(".discountAmt").text
print(After)

assert Before > After

#sum of products in checkout page matches with total amount
amounts = driver.find_elements_by_xpath("//tr/td[5]/p")
sum = 0
for amount in amounts:
    sum = sum + int(amount.text)
print(sum)

total = int(driver.find_element_by_class_name("totAmt").text)
print(total)

assert sum == total

driver.close()
