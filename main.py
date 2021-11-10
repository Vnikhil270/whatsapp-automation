# import web driver from selenium for automate the WhatsApp message
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pyperclip
import time

# 1.creating an obect to open chrome, 2.And paste the path of chrome driver
browser = webdriver.Chrome(r'C:\Users\Dell\Downloads\chromedriver_win32\chromedriver.exe')
browser.maximize_window()

# passing the url
browser.get('https://web.whatsapp.com/')

with open("groups.txt", "r", encoding="utf8") as f:
    groups =[group.strip() for group in f.readlines()]

groups = []
 
# number of people/groups as input
n = int(input("Enter number of group-name/person you want to send message : "))
 
# iterating till the range
for i in range(0, n):
    ele = input()
 
    groups.append(ele) # adding the element
    
msg = input("Enter the Message :")

for group in groups:
    
    # searching the search box present in whatsapp page
    search_xpath = '//div[@role="textbox"][@contenteditable="true"][@data-tab="3"]'
   
    #salenium's waits function is used until the browser loads whatsaapp
    search_input = WebDriverWait(browser, 500).until(EC.presence_of_element_located((By.XPATH, search_xpath)))

    # pyperclip is used to copy the anything as it is i.e it can be special charecter or emoji
    pyperclip.copy(group)
    # This function paste the group-name/user-name as it is
    
    search_input.send_keys(Keys.CONTROL + "v")
    
    time.sleep(2)

    # getting and opening the name of the person or group 
    name_xpath = f'//span[@title="{group}"]'     #f is used since it is a dynamic colonomal
    name_title = browser.find_element_by_xpath(name_xpath)
    name_title.click()

    time.sleep(2)

    # selecting the msg box for the writing process
    input_xpath = '//div[@contenteditable="true"][@data-tab="1"]'
    input_box = browser.find_element_by_xpath(input_xpath)
   
    pyperclip.copy(msg)
    # This function paste the text-message as it is
    input_box.send_keys(Keys.CONTROL + Keys.v)
    input_box.send_keys(Keys.ENTER)
    
