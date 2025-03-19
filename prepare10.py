shopping_list = []

print("Please enter the items of the shopping list (type: quit to finish):")
while True:
    item = input("Item: ")
    if item.lower() == "quit":
        break
    shopping_list.append(item)

print("The shopping list is:")
for item in shopping_list:
    print(item)

print("The shopping list with indexes is:")
for i in range(len(shopping_list)):
    print(f"{i}. {shopping_list[i]}")

index = int(input("Which item would you like to change? "))
new_item = input("What is the new item? ")

if 0 <= index < len(shopping_list):
    shopping_list[index] = new_item
else:
    print("Invalid index. No changes made.")

print("The shopping list with indexes is:")
for i in range(len(shopping_list)):
    print(f"{i}. {shopping_list[i]}")