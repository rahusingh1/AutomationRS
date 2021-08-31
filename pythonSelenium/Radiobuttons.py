from selenium import webdriver

driver = webdriver.Chrome("/home/rahul/PycharmProjects/AutomationRS/drivers/chromedriver")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

radiobuttons = driver.find_elements_by_name("radioButton")
radiobuttons[1].click()
assert radiobuttons[1].is_selected()

driver.close()