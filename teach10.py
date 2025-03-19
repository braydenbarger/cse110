account_names = []
account_balances = []

print("Enter the names and balances of bank accounts (type: quit when done)")
while True:
    name = input("What is the name of this account? ")
    if name.lower() == "quit":
        break
    balance = float(input("What is the balance? "))
    account_names.append(name)
    account_balances.append(balance)

total_balance = sum(account_balances)
average_balance = total_balance / len(account_balances) if account_balances else 0

print("Account Information:")
for i in range(len(account_names)):
    print(f"{i}. {account_names[i]} - ${account_balances[i]:.2f}")

print(f"Total: ${total_balance:.2f}")
print(f"Average: ${average_balance:.2f}")

if account_balances:
    max_balance = max(account_balances)
    max_index = account_balances.index(max_balance)
    print(f"Highest balance: {account_names[max_index]} - ${max_balance:.2f}")

while True:
    update = input("Do you want to update an account? (yes/no) ").lower()
    if update != "yes":
        break
    
    index = int(input("What account index do you want to update? "))
    if 0 <= index < len(account_names):
        new_balance = float(input("What is the new amount? "))
        account_balances[index] = new_balance
    
    print("Account Information:")
    for i in range(len(account_names)):
        print(f"{i}. {account_names[i]} - ${account_balances[i]:.2f}")
