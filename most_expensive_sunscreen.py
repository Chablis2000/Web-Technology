"""
Find the most expensive sunscreen and add it to the cart.
SCOPE:
1) Launch Chrome Driver
2) Navigate to Highest priced sunscreen 
3) Add that sunscreen to the cart
4) Open the cart
5) Check if the exact same sunscreen is added
6) Print the result
7) Close the browser

"""
from selenium import webdriver
import time

# Creating an instance of the web browser and navigating to the sunscreen page
driver = webdriver.Chrome()

# Maximize Browser Window
driver.maximize_window()

# Navigate to weathershopper's sunscreen Page
driver.get('https://weathershopper.pythonanywhere.com/sunscreen')

# Checking if the control lands on the right web page 
if driver.title=="The best moisturizers in the world!":
    print("Page found")

else:
    print("Invalid Page")
    driver.close()
    exit()

# Creating a list with prices of all sunscreen
sunscreen_prices=list()
prices_box=driver.find_elements_by_xpath('//div[@class="text-center col-4"]//descendant::p[contains(text(),"Price")]')
for i in prices_box:
    price=int(i.text.strip("Price: Rs. "))
    sunscreen_prices.append(price)
print("The prices of the sunscreens are ",sunscreen_prices)

# Finding the most expensive sunscreen
highest_price=max(sunscreen_prices)
print("The highest price is",highest_price)

# Adding to cart the sunscreen with maximun prize
add_btn=driver.find_element_by_xpath('//div[@class="text-center col-4"]//descendant::button[contains(@onclick,{})]'.format(highest_price))
add_btn.click()

# Clicking on cart button to check the product in cart
add_to_cart_btn=driver.find_element_by_xpath('//button[@class="thin-text nav-link"]')
add_to_cart_btn.click()

time.sleep(3)

# Check if the final cart total is equal to the highest prize and print Correct or Inncorrect Product

final_price=int(driver.find_element_by_xpath('//div[@class="row justify-content-center top-space-50"]//td[2]').text)
print("The price of the sunscreen in the cart is ",final_price)
if final_price==highest_price:
    print("Correct Product")
else:
    print("Incorrect Product")

# Close the web browser
driver.close()
