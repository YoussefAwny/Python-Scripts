from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select 
import time

driver = webdriver.Chrome()
driver.get("https://wiki.python.org/moin/FrontPage")

elem = driver.find_element_by_id("searchinput")
elem.clear()
elem.send_keys("Beginner")
elem.send_keys(Keys.RETURN)
time.sleep(8)

action_select = Select(driver.find_element_by_xpath("/html/body/div[2]/div[3]/ul/li[5]/form/div/select"))
action_select.select_by_index(1)
time.sleep(8)


driver.close()
