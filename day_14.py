# map allows us to use a function on another iterable
# filter allows us to filter items from an iterable, for example we can define a function to filter evan number 
# from a list
# reduce is like map but it returns only one item

# higher order function is a function that accepts a function as a parameter or return a function
# closure is a function inside another function
# A decorator is an order given through @ to go with a function

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

[print(country) for country in countries]
[print(name) for name in names]
[print(number) for number in numbers]

print(list(map(lambda country: country.upper(), countries)))
print(list(map(lambda number: number ** 2, numbers)))
print(list(map(lambda name: name.upper(), names)))
def contain_land(country):
    return 'land' in country
print(list(filter(contain_land, countries)))
def six_characters(country):
    return len(country) == 6
print(list(filter(six_characters, countries)))
def six_letters_and_more(country):
    return len(country) >= 6
print(list(filter(six_letters_and_more, countries)))
def starting_with_E(country):
    return country[0] == 'E'
print(list(filter(starting_with_E, countries)))



def get_string_lists(lst):
    lalst = []
    for item in lst:
        if type(item) == str:
            lalst.append(item)
    return lalst

from functools import reduce
def sum_numbs(a, b):
    return a + b
summ = reduce(sum_numbs, numbers)

all_but_last = countries[:-1]
last_country = countries[-1]
def tatata(all_but_last, iterable):
    return f"{all_but_last}, {iterable}"
joined_list = reduce(tatata, all_but_last)
lemilist = f"{joined_list} and {last_country} are north European countries" 


from data.countries import countries
def categorize_countries(country):
    patterns = ['land', 'ia', 'island', 'stan']
    for p in patterns:
        if p in country:
            return True
    return False

def return_a_dictionnary(countries):
    dictionnary = {}
    for country in countries:
        x = country[0]
        if x in dictionnary:
            dictionnary[x] += 1
        else:
            dictionnary[x] = 1
    return dictionnary


def get_first_ten_countries(countries):
    return countries[:10]

def get_last_ten_countries(countries):
    return countries[-10:]

from data.countries_data import countries_data

sorted_by_name = sorted(countries_data, key = lambda x: x['name'])
sorted_by_capital = sorted(countries_data, key = lambda x: x['capital'])
sorted_by_population = sorted(countries_data, key = lambda x: x['population'])

all_languages = {}
for country in countries_data:
    for language in country['languages']:
        if language in all_languages:
            all_languages[language] += 1
        else:
            all_languages[language] = 1
all_languages = sorted(all_languages.items(), key = lambda l: l[1], reverse=True)
most_spoken_languages = all_languages[:10]

    
all_populations = sorted(countries_data, key = lambda p: p['population'], reverse=True)
most_ten_populated_countries = all_populations[:10]
