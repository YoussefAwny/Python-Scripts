from selenium import webdriver

driver = webdriver.Chrome()
driver.get("file:///D:/Learning%20Engineering/Python%20Automation%20and%20testing/Ex_Files_Python_Automation_Testing/Exercise%20Files/CH02/html_code_02.html")
login_form_absolute = driver.find_element_by_xpath("/html/body/form[1]")
login_form_relative = driver.find_element_by_xpath("//form[1]")
login_form_id = driver.find_element_by_xpath("//form[@id='loginForm']")
print("My login form is:")
print(login_form_absolute)
print(login_form_relative)
print(login_form_id)
driver.close()
