# Step 1 - Create and run a Python file
print("*****Python Foundation Lab Started") # print function

#step 2 - Create variables and data types 
product = "Laptop" # string variable
quantity = 3
unit_price = 1200.50 # float variable
in_stock = True # boolean variable

print ("****** variable values ******")
print ("product:", product)
print ("quantity", quantity)
print ("unit_price", unit_price)
print ("in_stock", in_stock)

print("****** Variable data types ******")
print ("product:", product)
print ("quantity", quantity)
print ("unit_price", unit_price)
print ("in_stock", in_stock)

# Step 3 - Perform a sales calculation
total_sales = quantity * unit_price # calculate total sales
print("Product:", product)
print("Quantity:", quantity)
print("Unit Price:", unit_price)
print("Total Sales:", total_sales)

# Step 4 - Apply Conditional Statements 
if total_sales>=2000:
    print("Sales target achieved!")
else: 
    print("Sales target not achieved. Keep trying!")

#Step 5 - Process Multiple Sales using loop
sales = [1200, 850, 2400, 1750, 3200] # list of sales amounts
print("****** Processing Multiple Sales ******")
for sale in sales:
    if sale >= 2000:
        print(f"Sale amount {sale} meets the target!")
    else:
        print(f"Sale amount {sale} does not meet the target. Keep trying!")