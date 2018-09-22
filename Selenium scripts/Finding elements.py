from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.seleniumhq.org/")
element = driver.find_element_by_id("q")
print(" the element by id q is ")
print(element)

element = driver.find_element_by_name("q")
print(" the element by name q is ")
print(element)

heading_xpath = driver.find_element_by_xpath("//*[@id='mainContent']/h2[1]")
print(" the element heading what is selenium ")
print(heading_xpath)

element = driver.find_element_by_class_name("selenium-sponsors")
print(" the element by class is ")
print(element)
driver.close()
