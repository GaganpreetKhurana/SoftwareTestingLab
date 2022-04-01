from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url= "index.html"
filepath = Path(url).resolve().as_uri()
driver.get(filepath)

# iterate unordered list
print("Unordered List Elements:")
for listElement in driver.find_elements(By.XPATH,"//ul[@id='unorderedList']//li"):
    print("    " + listElement.text)
print("Unordered List Elements printed\n")

# iterate ordered list
print("Ordered List Elements:")
for listElement in driver.find_elements(By.XPATH,"//ol[@id='orderedList']//li"):
    print("    " + listElement.text)
print("Ordered List Elements printed\n")

# selecting Data Structure from dropdown 
driver.find_element(By.ID,"slct").click()
driver.find_element(By.XPATH,"//select[@id='slct']//option[contains(text(),'Data Structure')]").click()
print("Data Structure selected from Dropdown\n")

# invoke javascript
driver.execute_script("alert('Script executed from Selenium')")
print("Javascript executed\n")

