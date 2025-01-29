from datetime import date
from datetime import datetime

today = date.today()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

child_price = float(input("What is the price of a child's meal? "))
adult_price = float(input("What is the price of an adult's meal? "))
child_number = int(input("How many children are there? "))
adult_number = int(input("How many adults are there? "))
tax_rate = float(input("What is the sales tax rate? "))
tip = float(input("What is the tip amount? "))

child_total = (child_price * child_number)
adult_total = (adult_price * adult_number)
subtotal = child_total + adult_total + tip
tax = subtotal * (tax_rate / 100)
total = subtotal + tax

print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")

payment = float(input("What is the payment amount? "))
change = payment - total
print(f"Change: ${change:.2f}")

receipt = (f'''
            ----------------------------------------
            Date: {today}
            Time: {current_time}
            QTY of Child Meals: {child_number} Child Meals Price: ${child_total:.2f}
            QTY of Adult Meals: {adult_number} Adult Meals Price: ${adult_total:.2f}
            Subtotal: ${subtotal:.2f}
            Tax: ${tax:.2f}
            Tip: ${tip:.2f}
            Total: ${total:.2f}
            Payment: ${payment:.2f}
            Change: ${change:.2f}
''')

print(receipt)