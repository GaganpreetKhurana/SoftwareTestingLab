from selenium import webdriver
from selenium.webdriver.common.by import By

# firefox driver object
driver = webdriver.Firefox()
# data to be filled
url = "https://www.facebook.com"
email = "softwareTestingLab@pec.edu.in"  # incorrect username
password = "softwareLabTesting@332"  # correct password

# open url
driver.get(url)
# print in console
print("URL: " + driver.current_url)
print("Email: " + email)
print("Password: "+password)

# fill data
driver.find_element(By.ID, "email").send_keys(email)
driver.find_element(By.ID, "pass").send_keys(password)
driver.save_screenshot('question2_FilledData.png')
# submit
driver.find_element(By.NAME, "login").click()
driver.save_screenshot('question2_UnableToLogin.png')
