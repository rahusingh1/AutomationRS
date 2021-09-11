from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome("/home/rahul/PycharmProjects/AutomationRS/drivers/chromedriver")

driver.get("https://www.rahulshettyacademy.com/angularpractice/")

driver.find_element_by_css_selector("a[href*='shop']").click()

products = driver.find_elements_by_xpath("//div[@class='card h-100']")
for product in products:
    productname = product.find_element_by_xpath("div/h4/a").text
    if productname == "Blackberry":
        product.find_element_by_xpath("div/button").click()

driver.find_element_by_css_selector("a.btn-primary").click()
assets = driver.find_element_by_link_text("Blackberry").text
assert assets == "Blackberry"

driver.find_element_by_css_selector("button.btn-success").click()
driver.find_element_by_id("country").send_keys("ind")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

driver.find_element_by_link_text("India").click()
driver.find_element_by_css_selector(".checkbox-primary").click()
driver.find_element_by_css_selector("input[type='submit']").click()

successmsg = driver.find_element_by_css_selector("div[class*='alert-success']").text
print(successmsg)
assert "Success!" in successmsg

driver.get_screenshot_as_file("screen.png")   # to get screenshot

driver.close()