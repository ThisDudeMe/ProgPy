initial_population = 26000
birthRate = 0.007 
deathRate = 0.006 
immigrants = 325
emigrants = 300

year = int(input("Enter the year: "))

for _ in range(year - 2022):
    population_growth = (initial_population * birthRate) - (initial_population * deathRate) + immigrants - emigrants
    initial_population += population_growth

print("Estimated population at the beginning of {year}: {initial_population} inhabitants")
