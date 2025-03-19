file_path = "life-expectancy.csv"

lowest_life_expectancy = float('inf')
highest_life_expectancy = float('-inf')

with open(file_path, "r", encoding="utf-8") as file:
    next(file)

    for line in file:
        parts = line.strip().split(",")
        
        country = parts[0]
        year = int(parts[2])
        life_expectancy = float(parts[3])

        if life_expectancy < lowest_life_expectancy:
            lowest_life_expectancy = life_expectancy
        
        if life_expectancy > highest_life_expectancy:
            highest_life_expectancy = life_expectancy

print(f"Lowest life expectancy in dataset: {lowest_life_expectancy}")
print(f"Highest life expectancy in dataset: {highest_life_expectancy}")
