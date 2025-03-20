import csv
file_path = "life-expectancy.csv"

lowest_life = float('inf')
highest_life = float('-inf')
lowest_country = ""
highest_country = ""
lowest_year = 0
highest_year = 0
year_data = {}

with open(file_path, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    
    for row in reader:
        try:
            country = row[0]
            year = int(row[2])
            life_expectancy = float(row[3])
            
            if life_expectancy < lowest_life:
                lowest_life = life_expectancy
                lowest_year = year
                lowest_country = country
            
            if life_expectancy > highest_life:
                highest_life = life_expectancy
                highest_year = year
                highest_country = country
            
            if year not in year_data:
                year_data[year] = []
            year_data[year].append((country, life_expectancy))
        except ValueError:
            continue

print("The overall max life expectancy is:", highest_life, "from", highest_country, "in", highest_year)
print("The overall min life expectancy is:", lowest_life, "from", lowest_country, "in", lowest_year)

year_of_interest = int(input("Enter the year of interest: "))
if year_of_interest in year_data:
    entries = year_data[year_of_interest]
    total_life_expectancy = sum(life for _, life in entries)
    avg_life_expectancy = total_life_expectancy / len(entries)
    min_country, min_life = min(entries, key=lambda x: x[1])
    max_country, max_life = max(entries, key=lambda x: x[1])
    
    print("For the year", year_of_interest, ":")
    print("The average life expectancy was", round(avg_life_expectancy, 2))
    print("Max:", max_life, "in", max_country)
    print("Min:", min_life, "in", min_country)
else:
    print("No data available for", year_of_interest)
