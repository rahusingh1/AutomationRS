from selenium import webdriver

driver = webdriver.Chrome("/home/rahul/PycharmProjects/AutomationRS/drivers/chromedriver")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

assert driver.find_element_by_id("displayed-text").is_displayed() # assert is always asks for true to pass
driver.find_element_by_css_selector("#hide-textbox").click()
# here we use negation because we expect false and not of false is true
assert not driver.find_element_by_id("displayed-text").is_displayed()

driver.close()