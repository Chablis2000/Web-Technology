"""
 Add two moisturizers to the cart according to the conditions given.
 SCOPE:
 1) Launch Chrome Driver.
 2) Add moisterizers to the cart according using the given conditions
     (i) Select the least expensive mositurizer that contains Aloe and
     (ii) Select the least expensive moisturizer that contains Almond.
 3) Make a list of the products to be added.
 4) Click on Cart.
 5) Check if all the moisturizers are added correctly by comparing list of products in the cart with the products to be added.
 6) Close the browser.
"""

from selenium import webdriver
import time

# Creating an instance of the web browser and navigating to the Shopping page
driver = webdriver.Chrome()

# Maximize Browser Window
driver.maximize_window()

# Navigate to weathershopper's Moisturizer Page
driver.get('https://weathershopper.pythonanywhere.com/moisturizer')

# Checking if the control lands on the right web page 
if driver.title=="The best moisturizers in the world!":
    print("Page found")

else:
    print("Invalid Page")
    driver.close()
    exit()

# Pause the script to wait for page elements to load
time.sleep(3)

# Creating a list of all moisturizers
list_moisturizer=driver.find_elements_by_xpath('//div[@class="text-center col-4"]')

# A List of products which are added into the cart
products_added=[]

# The products containing Aloe
print("\n Moisturizers containing Aloe are :\t")
aloe_moist_list=[]
for i in list_moisturizer:
    try:
        current_element=i.find_element_by_xpath('.//p[contains(text(),"Aloe")]')
        price_element=i.find_element_by_xpath('.//p[contains(text(),"Price")]').text
        price=int(price_element.strip("Price : Rs. "))
        print("     ",current_element.text,"  :  ",price)
        aloe_moist_list.append([i,price])
    except Exception as e:
        continue

# Finding Aloe moisturizer with minimum price
first_min_price=1000
for i,j in aloe_moist_list:
    if j<first_min_price:
        first_min_price=j
        first_product=i
print("Moisturizer containing Aloe added to cart : \n ",first_product.find_element_by_xpath('.//p[contains(text(),"Aloe")]').text, "\n and cost ",first_product.find_element_by_xpath('.//p[contains(text(),"Price")]').text)
products_added.append(first_product.find_element_by_xpath('.//p[contains(text(),"Aloe")]').text)

# Adding the first product to the cart to the cart
first_product_add=first_product.find_element_by_xpath('.//button[text()="Add"]')
first_product_add.click()

# Finding moisturizers with almond and thier prices 
print("\nMoisturizers with Almond are :\n")
almond_list=[]
for i in list_moisturizer:
    try:
        current_element=i.find_element_by_xpath('.//p[contains(text(),"Almond")]')
        price_element=i.find_element_by_xpath('.//p[contains(text(),"Price")]').text
        price=int(price_element.strip("Price : Rs. "))
        print("     ",current_element.text,"    ",price)
        almond_list.append([i,price])
    except Exception as e:
        continue

# Finding the least expensive moisturizer that contains almond
second_min_price=1000
for i,j in almond_list:
    if j<second_min_price:
        second_min_price=j
        second_product=i
print("\nMoisturizer containing Almond added to cart :\n ",second_product.find_element_by_xpath('.//p[contains(text(),"Almond")]').text, "\n and cost ",second_product.find_element_by_xpath('.//p[contains(text(),"Price")]').text)

# Adding second product to the cart
products_added.append(second_product.find_element_by_xpath('.//p[contains(text(),"Almond")]').text)
second_product_add=second_product.find_element_by_xpath('.//button[text()="Add"]')
second_product_add.click()

# Clicking on cart button to check if the correct moisturizers are added
cart_button=driver.find_element_by_xpath('//button[@class="thin-text nav-link"]')
cart_button.click()

# Finding products in the cart
cart_items=driver.find_elements_by_xpath('//tbody/tr/td[1]')
cart_products=[]
for element in cart_items:
    cart_products.append(element.text)
print("\n Products in the cart are :\n")
print("\n".join(cart_products))

# Pause the script to wait for page elements to load
time.sleep(3)

# Checking if the products are addedcorrectly 
if products_added==cart_products:
    print("\n\n  Successfully added the products")
else:
    print("Failed to add products")

#Close the browser
driver.close()