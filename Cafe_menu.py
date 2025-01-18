# Cafe Management system

menu = {
    'pizza' : 5,
    'burger': 6,
    'pasta' : 7,
    'waffle' : 10,
    'coffee' : 3
}

print("WELCOME TO THE GREAT EUROPE CAFE")
print("MENU:")
for item,price in menu.items(): # item and price are new variable
    print(f"{item.capitalize()} = {price} Eur")

amount_total = 0
total_orders = 0

while True:
    order = input("What would you like to order? (Type 'Bill' to finish): ").strip().lower()

    if (order.lower() == "bill"):
        print(f"\nYou placed {total_orders} orders.")
        print(f"Your SWEET total order amount is {amount_total} Eur")
        break
    elif order in menu:
        total_orders += 1
        amount_total += menu[order]
        print(f"{order.capitalize()} added to your order. Current total: {amount_total} Eur")
    else:
        print(f"This item is not available in this cafe. Please choose an item from the menu.")