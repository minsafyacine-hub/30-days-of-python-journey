count = range(11)
for number in count:
    print(number)
n = 0
while n <= 10:
    print(n)
    n = n + 1

for number in range(10, -1, -1):
    print(number)  

countw = 10
while countw <= 0:
    print(countw)
    countw = countw - 1

for i in range(1, 9):
    print('#' * i) 

for l in range(8):
    for c in range(8):
        print('#', end=' ')
    print() 

for n in range(11):
    print(f"{n} * {n} = {n * n}") 

programming_languages = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for language in programming_languages:
    print(language)

qst_7 = range(101)
for even_number in range(101):
    if even_number % 2 == 0:
        print(even_number)

qst_8 = range(101)
for odd_number in range(101):
    if odd_number % 2 != 0:
        print(odd_number)

total_number = 0
for total_number in range(101):
    sum_numbers = total_number + number
print(f"The sum of all numbers if {sum_numbers}")

sum_evens = 0
sum_odds = 0
for number in range(101):
    if number % 2 == 0:
        sum_evens += number
    if number % 2 != 0:
        sum_odds += number
print(f"The sum of all evens is {sum_evens}. And the sum of all odds is {sum_odds}")

from data.countries import countries
from data.countries_data import countries_data

landcountry = []
for country in countries:
    if 'land' in country:
        landcountry.append(country)
print(landcountry)  

fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for fruit in fruits:
    reversed_fruits.insert(0, fruit)
print(reversed_fruits)

all_languages = []
for country in countries_data:
    for language in country['languages']:
        if language not in all_languages:
            all_languages.append(language)
print(all_languages) 

counts = {}
for country in countries_data:
    for language in country['languages']:
        if language in counts:
            counts[language] += 1
        else:
            counts[language] = 1
real_list = []
for language in counts:
    real_list.append((counts[language], ': ', language))
real_list.sort(reverse=True)
print(real_list[:10])

most_populated_country = []
for country in countries_data:
    most_populated_country.append((country['population'], country['name']) ) 
most_populated_country.sort(reverse=True)
print(most_populated_country[:10])




    


