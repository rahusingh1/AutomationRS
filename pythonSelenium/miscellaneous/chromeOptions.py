from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome("/home/rahul/PycharmProjects/AutomationRS/drivers/chromedriver", options=chrome_options)

driver.get("https://www.rahulshettyacademy.com/angularpractice/")

print(driver.title)

driver.close()
