# to get the title we use driver.title

# program to print title of the page

from selenium import webdriver

driver = webdriver.Firefox()

url= "https://www.pec.ac.in"
driver.get(url)
print("URL: " + url)
print("Title: "+ driver.title)
