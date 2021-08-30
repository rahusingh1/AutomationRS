from selenium import webdriver
import time

driver = webdriver.Chrome("/home/rahul/PycharmProjects/AutomationRS/drivers/chromedriver")

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(2) # it give the options to load so next locator can locate it.
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break
print(driver.find_element_by_id("autosuggest").text) # it print nothing because value not load in DOM
Scountry = driver.find_element_by_id("autosuggest").get_attribute('value')
print(Scountry)
assert Scountry == "India"

driver.close()