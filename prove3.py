child_price = float(input("What is the price of a child's meal? "))
adult_price = float(input("What is the price of an adult's meal? "))
child_number = int(input("How many children are there? "))
adult_number = int(input("How many adults are there? "))
tax_rate = float(input("What is the sales tax rate? "))
tip = float(input("What is the tip amount? "))

subtotal = (child_price * child_number) + (adult_price * adult_number) + tip
tax = subtotal * (tax_rate / 100)
total = subtotal + tax

print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")

payment = float(input("What is the payment amount? "))
change = payment - total
print(f"Change: ${change:.2f}")