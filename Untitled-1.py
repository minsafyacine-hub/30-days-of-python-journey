for i in range(11):
    print(i)

i = 0
while i <= 10:
    print(i)
    i += 1
 
for i in range(10, -1, -1):
    print(i)

n = 10
while n <= 0:
    print(i)
    i += 1 

for i in range(1, 9):
    print('#' * i)

for c in range(8):
    for l in range(8):
        print('#', end=' ') 
    print()

n = 0
for n in range(11):
    print(f"{n} * {n} = {n * n}")

p_l = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for language in p_l:
    print(language)

for i in range(101):
    if i % 2 == 0:
        print(i)

for i in range(101):
    if i % 2 != 0:
        print(i)

sum_evens = []
for i in range(101):
    sum_evens.append(i)
print(f"The sum of all numbers is {sum(sum_evens)}")

sum_evens = []
sum_odds = []
for i in range(101):
    if i % 2 == 0:
        sum_evens.append(i)
    else:
        sum_odds.append(i)
print(f"The sum of all evens is {sum(sum_evens)}. And the sum of all odds is {sum(sum_odds)}")

from data.countries import countries 

for country in countries:
    if 'land' in country:
        print(country)

fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for fruit in fruits:
    reversed_fruits.insert(0, fruit)
print(reversed_fruits)

from data.countries_data import countries_data

number_of_languages = []
for country in countries_data:
    for language in country['languages']:
        if language not in number_of_languages:
            number_of_languages.append(language)
print(len(number_of_languages))


counts = {}
for country in countries_data:
    for language in country['languages']:
        if language in counts:
            counts[language] += 1
        else:
            counts[language] = 1 
most_spoken_languages = []
for languages in counts:
    most_spoken_languages.append((counts[languages], languages))
most_spoken_languages.sort(reverse=True)
print(most_spoken_languages[:10]) 

most_populated_countries = []
for country in countries_data:
    nom = country['name']
    pop = country['population']
    most_populated_countries.append((pop, nom))
most_populated_countries.sort(reverse=True)
print(most_populated_countries[:10])
