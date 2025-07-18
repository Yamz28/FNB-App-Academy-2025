
#Create a shopping cart programme that will continuously ask the user for a food product and the price of that product
#Have an exit clause if the user wishes to stop adding things to their cart
#At the end show the food items and the total cost to the user

shopping_cart = {}
while True:
    item = input("Enter a food product (or type 'exit' to finish):")
    if item.lower() == 'exit' :
        break
    price = float(input(f"Enter the price of {item}:"))
    shopping_cart[item] = price
    
#Show the items and total cost
total_cost = sum(shopping_cart.values())
print("Your shopping cart contains:")
for item, price in shopping_cart.items():
    print(f"{item}: R{price:.2f}")
print(f"Total cost: R{total_cost:.2f}")