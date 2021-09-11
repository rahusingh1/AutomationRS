from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("/home/rahul/PycharmProjects/AutomationRS/drivers/chromedriver")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)
action.move_to_element(driver.find_element_by_id("mousehover")).perform()  #mouse hover

childmenu = driver.find_element_by_link_text("Top")  #action on child menu
action.move_to_element(childmenu).click().perform()

#double click actions and context click that is right click
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)
action.context_click(driver.find_element_by_id("double-click")).perform()  # for right click
action.double_click(driver.find_element_by_id("double-click")).perform()   # for double click

alert = driver.switch_to.alert
print(alert.text)
assert "You double clicked me!!!, You got to be kidding me" == alert.text
alert.accept()

driver.close()
