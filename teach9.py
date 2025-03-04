def main():
    numbers = []
    print("Enter a list of numbers, type 0 when finished.")
    
    while True:
        num = int(input("Enter number: "))
        if num == 0:
            break
        numbers.append(num)
    
    if not numbers:
        print("No numbers were entered.")
        return
    
    total = sum(numbers)
    average = total / len(numbers)
    largest = max(numbers)
    
    print(f"The sum is: {total}")
    print(f"The average is: {average}")
    print(f"The largest number is: {largest}")
    
    positive_numbers = [num for num in numbers if num > 0]
    if positive_numbers:
        smallest_positive = min(positive_numbers)
        print(f"The smallest positive number is: {smallest_positive}")
    
    sorted_numbers = sorted(numbers)
    print("The sorted list is:")
    for num in sorted_numbers:
        print(num)

if __name__ == "__main__":
    main()
