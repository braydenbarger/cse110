print("Welcome to the Shopping Cart Program!")
cart = []

while True:
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Quit")
    
    choice = input("Please enter an action: ")
    
    if choice == "1":
        item = input("What item would you like to add? ")
        cart.append(item)
        print(f"'{item}' has been added to the cart.")
    elif choice == "2":
        if not cart:
            print("The shopping cart is empty.")
        else:
            print("The contents of the shopping cart are:")
            for item in cart:
                print(item)
    elif choice == "3":
        print("Thank you. Goodbye.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
