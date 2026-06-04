def add_two_numbers(x, y):
    z = x + y
    return(z)

def area_of_circle(r):
    pi = 3.14
    z = pi * r**2
    return(z)

def add_all_nums(x, y):
    z = x + y
    if float(x) and float(y):
        return(z)
    else:
        return('The sumation cannot be done')
    
def convert_celsius_to_fahrenheit(x):
    z = (x * 9/5) + 32
    return(f"{z} °F")

def check_season(z):
    if z in ('Septembre', 'October', 'November'):
        return('The season is Automn')
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
    x = input('Enter value for x')
    y = a*x**2 + b * x + c
    return(y)

def print_list(list):
    la_list = []
    for i in list:
        la_list.append(i)
    return(la_list)
    
def reverse_list(list):
    resultat = []
    for i in list:
        resultat.insert(i, 0) 
    return(resultat)

def capitalize_list_items(list):
    maj_list = []
    for i in list:
        maj_list.append(i.upper())
    return(maj_list)

def add_item(x):
    listp = []
    for i in listp:
        listp.append(x)
    return(listp)

def remove_item(x):
    la_liste = []
    for i in la_liste:
        la_liste.pop(x)
    return(la_liste)

def sum_of_numbers(x):
    for i in range(x):
        if float(i):
            return(sum(range(x)))
        else:
            return('The summation cannot be done')
        
def sum_of_odds(x):
    if float(x):
        for i in range(x):
            if i % 2 != 0:
                sum(i)
            else:
                i
        return(range(x))
    
def sum_of_evens(x):
    if float(x):
        for i in range(x):
            if i % 2 == 0:
                sum(i)
            else:
                i 
        return(range(x))
    
def evens_and_odds(x):
    for i in x:
        if i % 2 != 0:
            i += 1
            return(f"The number off evens are {i}")
        else:
            i = 1
            return(f"The number off odds are {i}")
        
def factorial(x):
    if x == 0 or x == 1:
        return(x)
    else:
        return(x * (x - 1)) 
    
def is_empty():
    for i in ():
        if i in ():
            return('The parameter is not empty')
        else:
            return('The parameter is empty')
        
def calculate_mean(list):
    for i in list:
        x = sum(list) / len(list)
    return(x)
def calculate_mediane(list):
    for i in list:
        mid = list[len(list) // 2] 
        x = mid / len(list)
    return(x)
def calculate_mode(list):
    return(max(list))
def calculate_range(list):
    return(len(list))
def calculate_variance(list):
    for i in list:
        x = sum(i - i**2) / len(list)
    return(x)
def calculate_std(list):
    for i in list:
        x = (sum(i - i**2) / len(list))**0.5
    return(x)

def greet(x):
    if x in ():
        return(f"Hello, {x}")
    else:
        return('Hellon, Guest')

def show_arg(x, y, z):
    w = (f"name : {x}, age : {y}, city : {z}")
    return(w)
    
print(show_arg('yacine', 20, 'pontoise'))