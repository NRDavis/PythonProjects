import os
from selenium import webdriver
from time import sleep


os.system("clear")
print("Launching Chrome...")

# we launch the browser and setup our driver
driver = webdriver.Chrome(os.getcwd()+"/chromedriver")  	# /home/nathan/Documents/pythonResources/scripts/
driver.get("https://quotes.freerealtime.com/") 


# we navigate to our test stock
stock_symbol = driver.find_element_by_id("edit-symbol")
stock_symbol.send_keys("TSLA")              # we use tesla stock as a proxy
search_button = driver.find_element_by_id("edit-submit")
search_button.click()

price = driver.find_element_by_class_name("qmod-data-point qmod-textr").text         #   qmod-data-point qmod-textr          qmod-last
print("Stock price:\t\t"+price)



# This script works for identifying stock prices and obtaining updated data



