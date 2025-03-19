items = []
prices = []
quantity = []

print("Welcome to the Shopping Cart Program!")

while True:
    print("Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    
    choice = input("Please enter an action: ")

    if choice == "1":
        item_name = input("What item would you like to add? ")
        item_price = float(input(f"What is the price of '{item_name}'? "))
        item_quantity = int(input(f"How many '{item_name}s' would you like to add? "))
        
        items.append(item_name)
        prices.append(item_price)
        quantity.append(item_quantity)
        
        print(f"'{item_name}' (x{item_quantity}) has been added to the cart.")

    elif choice == "2":
        print("The contents of the shopping cart are:")
        for i in range(len(items)):
            total_item_price = prices[i] * quantity[i]
            print(f"{i + 1}. {items[i]} - ${prices[i]:.2f} x {quantity[i]} = ${total_item_price:.2f}")

    elif choice == "3":
        try:
            item_index = int(input("Which item would you like to remove? ")) - 1
            if item_index >= 0 and item_index < len(items):
                del items[item_index]
                del prices[item_index]
                del quantity[item_index]
                print("Item removed.")
            else:
                print("Sorry, that is not a valid item number.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":
        total_price = sum(prices[i] * quantity[i] for i in range(len(items)))
        print(f"The total price of the items in the shopping cart is ${total_price:.2f}")

    elif choice == "5":
        print("Thank you. Goodbye.")
        break

    else:
        print("Invalid choice, please select a valid option.")
