from selenium import webdriver

driver = webdriver.Chrome("/home/rahul/PycharmProjects/AutomationRS/drivers/chromedriver")
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("rahul")
driver.find_element_by_css_selector("input[type='submit']").click()

message = driver.find_element_by_css_selector("[class*='alert-success']").text
# syntax to check sub string from main string
assert "Success" in message
# syntax to check full string
#assert message == "Success! The Form has been submitted successfully!."
driver.close()