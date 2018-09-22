from selenium import webdriver

driver = webdriver.Chrome()
driver.get("file:///D:/Learning%20Engineering/Python%20Automation%20and%20testing/Ex_Files_Python_Automation_Testing/Exercise%20Files/CH02/html_code_02.html")
login_form = driver.find_element_by_id('loginForm')
print("My login form elemet is:")
print(login_form)
driver.close()
