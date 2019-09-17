"""
Learn to click a button with Selenium

DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2

AUTHOR: Avinash Shetty
Contact: avinash@qxf2.com

SCOPE:
1) Launch Chrome driver
2) Navigate to LinkedIn page
3) Find the Sign in button and click on it
4) Find the Email id text field and Enter your Email id
5) Find the Password field and Enter your Password
6) Find the Sign in button and click on it
7) Check for page title
8) Close the driver
"""
import time
from selenium import webdriver

# Create an instance of Chrome WebDriver
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Navigate to LinkedIn page
driver.get("https://in.linkedin.com")

# KEY POINT: Locate the button and click on it 
button  = driver.find_element_by_xpath("//a[@class='nav__button-secondary']") 
button.click()

# Find the email field using xpath without id
email = driver.find_element_by_xpath("//input[@id='username']")
email.send_keys('Enter your email')

password = driver.find_element_by_xpath("//input[@id='password']")
password.send_keys('Enter your Password')

button  = driver.find_element_by_xpath("//button[@class='btn__primary--large from__button--floating']") 
button.click()

# Pause the script to wait for page elements to load
time.sleep(10)

if(driver.title=="(2) LinkedIn"):
    print ("Success: LinkedIn launched successfully")
else:
    print ("Failed: LinkedIn page Title is incorrect")

# Close the browser
driver.close()


