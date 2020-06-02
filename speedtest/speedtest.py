import os
from selenium import webdriver
from time import sleep

os.system("clear")
print("Launching Chrome...")
# we must copy the chromedriver file into our local directory
driver = webdriver.Chrome(os.getcwd()+"/chromedriver")                                # open Firefox 
driver.get("https://www.speedtest.net/")                # connecting to speedtest by ookla

go_button = driver.find_element_by_link_text("GO")  # we find the go button
go_button.click()                                                    # we click the go button, start test


os.system("clear")
print("Obtaining data...")

# we wait 50 seconds before checking items
sleep(50)      
# we scrap the following item from the webpage
upload = driver.find_element_by_class_name("result-data-large.number.result-data-value.upload-speed").text
download = driver.find_element_by_class_name("result-data-large.number.result-data-value.download-speed").text
ping = driver.find_element_by_class_name("result-data-large.number.result-data-value.ping-speed").text

os.system("clear")
print("Automated Speed Test by Ookla Data:")
print("Ping:\t\t"+ping+"\nDownload:\t"+download+"\nUpload:\t\t"+upload)
