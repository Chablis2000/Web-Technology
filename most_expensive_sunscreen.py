"""
Test to read the temperature and choose the products

1) Launch Chrome driver
2) Navigate to weathershopper page
3) Read the temperature
4) Click on the desired product depending on the temperature
5) Open the product list page
6) Close the driver
"""
from selenium import webdriver
import time

# Creating an instance of the web browser and navigating to the Moisturizer page
driver = webdriver.Chrome()

# Maximize Browser Window
driver.maximize_window()

# Navigate to weathershopper's Moisturizer Page
driver.get('https://weathershopper.pythonanywhere.com/sunscreen')

# Checking if the control lands on the right web page 
if driver.title=="The best moisturizers in the world!":
    print("Page found")

else:
    print("Invalid Page")
    driver.close()
    exit()

# Creating a list with prizes of all moistirizers
moisturizer_prices=list()
prices_box=driver.find_elements_by_xpath('//div[@class="text-center col-4"]//descendant::p[contains(text(),"Price")]')
for i in prices_box:
    price=int(i.text.strip("Price: Rs. "))
    moisturizer_prices.append(price)
print("The prices of the moisturizers are ",moisturizer_prices)

# Finding the most expensive moisturizer
highest_price=max(moisturizer_prices)
print("The highest price is",highest_price)

# Adding to cart the moisturizer with maximun prize
add_btn=driver.find_element_by_xpath('//div[@class="text-center col-4"]//descendant::button[contains(@onclick,{})]'.format(highest_price))
add_btn.click()

# Clicking on cart button to check the product in cart
add_to_cart_btn=driver.find_element_by_xpath('//button[@class="thin-text nav-link"]')
add_to_cart_btn.click()

time.sleep(3)

# Check if the final cart total is equal to the highest prize and print Correct or Inncorrect Product

final_price=int(driver.find_element_by_xpath('//div[@class="row justify-content-center top-space-50"]//td[2]').text)
print("The price of the moisturizer in the cart is ",final_price)
if final_price==highest_price:
    print("Correct Product")
else:
    print("Inncorrect Product")

# Close the web browser
driver.close()
