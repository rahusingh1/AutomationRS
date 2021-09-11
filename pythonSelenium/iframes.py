from selenium import webdriver

driver = webdriver.Chrome("/home/rahul/PycharmProjects/AutomationRS/drivers/chromedriver")

driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("I am able to automate in frames.")

# to comes back to the html driver from frames.
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)

driver.close()