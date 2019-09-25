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

#Check the title of the page
if(driver.title =="The best moisturizers in the world!"):
    print("Loaded page Successfully")
else:
    print("Error Loading Page")

# Get the temperature text input from web page 
temp  = driver.find_element_by_xpath("//span[@id='temperature']").text

# Filter out and read only the the digits form the string 
temp1 = int(''.join(filter(lambda i: i.isdigit(), temp)))

#Check the product heading
def check_page(product,page):
    if product == page:
        print("Correct Product Heading")
    else:
        print("Inncorrect Product Heading")

# Condition to check weather to buy Moisturizers or Sunscreens depending on the temperature
# Buy a moisturizer if temperature is less than 19 degree celsius
# Buy a sunscreen if temperature is greather than 43 degree celsius
if temp1<19:
    product = 'Moisturizers'
    moist_button  = driver.find_element_by_xpath("//button[@class='btn btn-primary' and text()='Buy moisturizers']") 
    moist_button.click()
    moist_page = driver.find_element_by_xpath("//h2").text
    check_page(product,moist_page)

elif temp1>34:
    product = 'Sunscreens'
    sun_button  = driver.find_element_by_xpath("//button[@class='btn btn-primary' and text()='Buy sunscreens']") 
    sun_button.click()
    sun_page = driver.find_element_by_xpath("//h2").text
    check_page(product,sun_page)

# Pause the script to wait for page elements to load
time.sleep(5)

# Close the browser
driver.close()