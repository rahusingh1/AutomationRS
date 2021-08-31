from selenium import webdriver
import time

driver = webdriver.Chrome("/home/rahul/PycharmProjects/AutomationRS/drivers/chromedriver")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))

# select single checkbox by writing dynamically not hardcoded single checkbox
for checkbox in checkboxes:
    print(checkbox.get_attribute('value'))
    if checkbox.get_attribute('value') == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

# to select all the checkboxes
# for checkbox in checkboxes:
#     checkbox.click()
#     assert checkbox.is_selected()

driver.close()