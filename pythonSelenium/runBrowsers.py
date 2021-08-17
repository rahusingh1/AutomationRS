from selenium import webdriver

#driver = webdriver.Chrome(executable_path="/home/rahul/PycharmProjects/AutomationRS/drivers/chromedriver")
driver = webdriver.Firefox(executable_path="/home/rahul/PycharmProjects/AutomationRS/drivers/geckodriver")
# to maximize the window
driver.maximize_window()
#get() is the method to hit the url in the automated browser.
driver.get("https://www.rahulshettyacademy.com")

print(driver.title) # get title of the page.

#to know wheather you landed on correct webpage or not use following method.
print(driver.current_url)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# to minimize the window
driver.minimize_window()
# you can come to the previous page using the following method
driver.back()
# to refresh the complete screen just like reload the page
driver.refresh()
driver.close() # close only current window.
driver.quit() # close all windows of the browser.
#you can use the debugger to check steps one by one by running as debugger mode after clicking the line.