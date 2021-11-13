# import web driver from selenium for automate the WhatsApp message
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import time

# this imports the name_input.py file which takes user input
import name_input

msg = input("Enter the Message :")
# 1.creating an obect to open chrome, 2.And paste the path of chrome driver
browser = webdriver.Chrome(r'C:\Users\Dell\Downloads\chromedriver_win32\chromedriver.exe')
browser.maximize_window()

# passing the url
browser.get('https://web.whatsapp.com/')

# calling groups list present in name_input.py file through reference
for group in name_input.groups:
    
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
    name_xpath = f'//span[@dir="auto"][@title="{group}"]'     #f is used since it is a dynamic colonomal
    name_title = browser.find_element_by_xpath(name_xpath)
    name_title.click()

    time.sleep(2)

    # selecting the msg box for the writing process
    input_xpath = '//div[@contenteditable="true"][@data-tab="9"]'
    input_box = browser.find_element_by_xpath(input_xpath)
   
    pyperclip.copy(msg)
    # This function paste the text-message as it is
    input_box.send_keys(Keys.CONTROL + "v")
    input_box.send_keys(Keys.ENTER)
    
    time.sleep(15)
