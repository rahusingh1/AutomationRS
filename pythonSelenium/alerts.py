from selenium import webdriver

driver = webdriver.Chrome("/home/rahul/PycharmProjects/AutomationRS/drivers/chromedriver")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
values = "rahul"
driver.find_element_by_css_selector("#name").send_keys(values)
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
atext = alert.text
print(atext)
assert values in atext
alert.accept() # to accept the alert

driver.find_element_by_css_selector("#name").send_keys("singh")
driver.find_element_by_id("confirmbtn").click()
alert.dismiss() # to dismiss the alert or cancel it.

driver.close()