child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))
sales_tax_rate = float(input("What is the sales tax rate? "))

subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults)

sales_tax = subtotal * (sales_tax_rate / 100)

total = subtotal + sales_tax

print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")