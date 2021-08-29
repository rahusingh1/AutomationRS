from selenium import webdriver

driver = webdriver.Chrome("/home/rahul/PycharmProjects/AutomationRS/drivers/chromedriver")

driver.get("https://www.rahulshettyacademy.com/angularpractice/")

#driver.find_element_by_name("name").send_keys("Rahul")
# css selector
driver.find_element_by_css_selector("input[name='name']").send_keys("Rahul1")
driver.find_element_by_name("email").send_keys("rahul@mail.com")
driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_xpath("//input[@type='submit']").click()
print(driver.find_element_by_class_name("alert-success").text)
# Custom created Regular expressions for css and xpath
print(driver.find_element_by_css_selector("[class*='alert-success']").text) # css
print(driver.find_element_by_xpath("//*[contains(@class,'alert-success')]").text) # xpath
driver.get("https://login.salesforce.com/?locale=in")
# generate css locator from id attribute
driver.find_element_by_css_selector("[id='username']").send_keys("rahul_")
driver.find_element_by_css_selector("[id='username']").clear() # to clear entered text.
driver.find_element_by_css_selector("#username").send_keys("Test1")
driver.find_element_by_css_selector(".password").send_keys("Singh")
driver.find_element_by_link_text("Forgot Your Password?").click()
# Xpath based on text Syntax: //tagname[text()='xyz']
driver.find_element_by_name("cancel").click()
driver.find_element_by_xpath("//label[text()='Remember me']").click()
# Traversing tags of xpath and css
driver.find_element_by_xpath("//div[@id='usernamegroup']/label")
driver.find_element_by_css_selector("div[id='usernamegroup'] label")
# multi traversal of xpath and css
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text) # it print username
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(4)").text) #print password

driver.close()