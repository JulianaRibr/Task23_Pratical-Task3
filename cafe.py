# This code demonstrates how to create some dictionaries to 
# do a stock control in a hypothetical Cafe.


import math # Provides access to the mathematical functions.

print("<<Cafe Menu:>>\n")

# Create a Menu as a list.
menu = [
    'Coffee',
    'Tea',
    'English breakfast',
    'Sparkling Water',
    'Soft Drink',
    'Cheese bread',
    'Chocolate Cake',
    'Mince Pie',
    'Cupcake',
    'Pop Corn'
    ] 
print(menu)
print("\nThis is the today' Cafe Stock:")
print("")

# Create a dictionary to record the items of the Cafe stock.
stock = {
     'Coffee': 10,
     'Tea': 30,
     'English Breakfast': 25,
     'Sparkling Water': 20,
     'Soft Drink': 25,
     'Cheese Bread': 55,
     'Chocolate Cake': 15,
     'Mince Pie': 35,
     'Cupcake': 20,
     'Pop Corn': 12
     }
print(stock)

# This block of code allows the user to update the stock.
answer = input("\nWould you like to do any stock update?")

if answer == "yes":
    while True:
        item = input("\nPlease, enter the item to update:")
        if not item in stock:
            print("Please enter an item from the Menu")
        else:
            try:
                new_quantity = int(input("Please, enter the new quantity of the item:"))
                stock[item] = new_quantity
                print("\nThe new stock is:\n")
                print(stock)
                break
            except ValueError:
                print("Enter an integer number.")

# Create a dictionary to record the items' prices of the Cafe stock.
price = {
    'Coffee': 4.40,
    'Tea': 6.25,
    'English Breakfast': 25,
    'Sparkling Water': 4.20,
    'Soft Drink': 5,
    'Cheese Bread': 3.25,
    'Chocolate Cake': 7.50,
    'Mince Pie': 8,
    'Cupcake': 5,
    'Pop Corn': 2
    }

print("\n<<Item value in the Stock>>")    

# This dict holds the pre-computed total values for each item in the stock.
# Based on a dict compreehension example found on Stack Overflow.
item_value = {key: stock[key] * price[key] for key in stock} 
print(item_value)
print("")

# Print the final value, with the total value of the stock, with the relative items updated.
total_stock = [sum(item_value.values())]
print(f"Today', total stock worth in the Cafe is {total_stock}!")
