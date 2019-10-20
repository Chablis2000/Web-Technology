"""
Find all the sunscreens and add it to the cart.
SCOPE:
1) Launch Chrome Driver
2) Navigate to Sunscreens page
3) Read the prices of all the sunscreens in the page
4) Add all the sunscreens to the cart
5) Open the cart
6) Check if all the sunscreens are added
7) Print the result
8) Close the browser

"""
from selenium import webdriver
import time

# Creating an instance of the web browser and navigating to the sunscreen page
driver = webdriver.Chrome()

# Maximize Browser Window
driver.maximize_window()

# Navigate to weathershopper's sunscreen Page
driver.get('https://weathershopper.pythonanywhere.com/sunscreen')

# Checking if we landed on the right web page 
if driver.title=="The best moisturizers in the world!":
    print("Page found")

else:
    print("Invalid Page")
    driver.close()
    exit()

#Reading the prices of all the sunscreens in the webpage and Creating a list with prices of all sunscreens
sunscreen_prices=list()
prices_box=driver.find_elements_by_xpath('//div[@class="text-center col-4"]//descendant::p[contains(text(),"Price")]')
for i in prices_box:
    price=int(i.text.strip("Price: Rs. "))
    sunscreen_prices.append(price)
print("The prices of the sunscreens are ",sunscreen_prices)

# Reading the prices from the list and adding all the sunscreens to the cart
cost= sunscreen_prices
for i in range(len(cost)):
    product_price=cost[i]
    add_btn=driver.find_element_by_xpath('//div[@class="text-center col-4"]//descendant::button[contains(@onclick,{})]'.format(product_price))
    add_btn.click()

# Clicking on cart button to check the product in cart
add_to_cart_btn=driver.find_element_by_xpath('//button[@class="thin-text nav-link"]')
add_to_cart_btn.click()

# Pause the script to wait for page elements to load
time.sleep(5)

# Close the web browser
driver.close()
