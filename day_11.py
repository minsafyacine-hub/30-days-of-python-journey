def add_two_numbers(x, y):
    z = x + y
    return(z)

def area_of_circle(r):
    pi = 3.14
    z = pi * r**2
    return(z)

def add_all_nums(*x):
    for num in x:
        if not isinstance(num, (int, float)):
            return('The sumation cannot be done')
        return(sum(x))
    
def convert_celsius_to_fahrenheit(x):
    z = (x * 9/5) + 32
    return(f"{z} °F")

def check_season(z):
    z = z.capitalize()
    if z in ('September', 'October', 'November'):
        return('The season is Autumn')
    elif z in ('December', 'January', 'February'):
        return('The season is Winter')
    elif z in ('March', 'April', 'May'):
        return('The season is  Spring')
    elif z in ('June', 'July', 'August'):
        return('The season is Summer')
    else:
        return('Please enter a proper month in English')
    
def calculate_slope(a, b, c):
    x = (c - b) / a
    return(x)

def solve_quadratic_eqn(a, b, c):
    y = ((b**2) - 4 * a * c)
    if y < 0:
        return('this equation has no solutions')
    elif y == 0:
        z = -b / 2 * a
        return(z)
    elif y > 0:
        x1 = (-b + y**0.5) / 2*a
        x2 = (-b - y**0.5) / 2*a
        return(x1, x2)
    else:
        return('Enter proper numbers')

def print_list(lst):
    for i in lst:
        print(i)
    
def reverse_list(lit):
    resultat = []
    for i in lit:
        resultat.insert(0, i) 
    return(resultat)

def capitalize_list_items(list):
    maj_list = []
    for i in list:
        maj_list.append(i.capitalize())
    return(maj_list)

def add_item(lst, itm):
    lst.append(itm)
    return(lst)

def remove_item(x, lst):
    if x in lst:
        lst.remove(x)
    return(lst)

def sum_of_numbers(x):
    if not isinstance(x, (int, float)):
        return('The summation cannot be done')
    else:
        return(sum(range(x + 1)))
        
def sum_of_odds(x):
    if isinstance(x, (int, float)):
        total = 0
        for i in range(x + 1):
            if i % 2 != 0:
                total += i
        return(total)
    
def sum_of_evens(x):
    if isinstance(x, (int, float)):
        total = 0
        for i in range(x + 1):
            if i % 2 == 0:
                total += i
        return(total)
    
def evens_and_odds(x):
    evens = 0
    odds = 0
    for i in range(x + 1):
        if i % 2 != 0:
            odds += 1
        else:
            evens += 1
    return(f"The number of odds are {odds}.\n The number of evens are {evens}")
        
def factorial(x):
    if x == 0 or x == 1:
        return(1)
    else:
        return(x * factorial(x - 1)) 
    
def is_empty(x):
    if not x:
        return('The parameter is empty')
    else:
        return('The parameter is not empty')
        
def calculate_mean(list):
    x = sum(list) / len(list)
    return(x)
def calculate_mediane(lst):
    lst.sort() 
    n = len(lst)
    mid = n // 2 
    if n % 2 == 0:
        return (lst[mid - 1] + lst[mid]) / 2
    else:
        return lst[mid]
def calculate_mode(list):
    return(max(set(list), key=list.count))
def calculate_range(list):
    return(max(list) - min(list))
def calculate_variance(list):
    moy = sum(list) / len(list)
    x = sum((i - moy)**2 for i in list) / len(list)
    return(x)
def calculate_std(list):
    return(calculate_variance(list) ** 0.5) 

def greet(name="Guest"):
    return(f"Hello, {name}")

def show_arg(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
def is_prime(x):
    if x < 2:
        return('False')
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return('False')
        return('True')


def unique_items(list):
    return len(list) == len(set(list))
        
def same_data_type(list):
    if not list:
        return True
    first_type = list[0]
    for i in list:
        if i == first_type:
            return('True')
        return('False')
        
def valid_python_variable(x):
    if x.isidentifier():
        return('True')
    else:
        return('False')
    
from data.countries_data import countries

def most_spoken_languages(list):
    msl = []
    for country in countries:
        for language in country['languages']:
            msl.append(language)
    msl.sort(reverse = True)
    return(msl[:10])

def most_populated_countries(list):
    mpc = []
    for country in countries:
        mpc.append(country['population'])
    mpc.sort(reverse=True)
    return(mpc[:10])


