"""
Test to read the temperature and choose the products

1) Launch Chrome driver
2) Navigate to weathershopper page
3) Read the temperature
4) Click on the desired product depending on the temperature
5) Open the product list page
6) Close the driver
"""
import time
from selenium import webdriver

# Create an instance of Chrome WebDriver
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Navigate to LinkedIn page
driver.get("https://weathershopper.pythonanywhere.com/")

# Get the temperature text input from web page 
temp  = driver.find_element_by_xpath("//span[@id='temperature']").text

# Filter out and read only the the digits form the string 
temp1 = int(''.join(filter(lambda i: i.isdigit(), temp)))

# Print the extracted digit
print (str(temp1))

# Condition to check weather to buy Moisturizers or Sunscreens depending on the temperature
# Buy a moisturizer if temperature is less than 19 degree celsius
# Buy a sunscreen if temperature is greather than 43 degree celsius
if temp1<19:
    button  = driver.find_element_by_xpath("//button[@class='btn btn-primary' and text()='Buy moisturizers']") 
    button.click()
    if(driver.find_element_by_xpath("//div[@class='row justify-content-center' and h2='Moisturizers']")):
        print ("Success: launched successfully")
    else:
        print ("Failed: page Title is incorrect")

elif temp1>34:
    button  = driver.find_element_by_xpath("//button[@class='btn btn-primary' and text()='Buy sunscreens']") 
    button.click()
    if(driver.find_element_by_xpath("//div[@class='row justify-content-center' and h2='Sunscreens']")):
        print ("Success: launched successfully")
    else:
        print ("Failed: page Title is incorrect")


# Pause the script to wait for page elements to load
time.sleep(5)

# Close the browser
driver.close()