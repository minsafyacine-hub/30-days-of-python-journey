import string
import random

def random_user_id():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=6))

def user_id_gen_by_user():
    characters = string.ascii_letters + string.digits
    number_of_characters = int(input('number of characters :'))
    number_of_IDs = int(input('number of IDs :'))
    lists = []
    for i in range(number_of_IDs):
        mots = ''.join(random.choices(characters, k=number_of_characters))
        lists.append(mots)
    return '\n'.join(lists)


def rgb_color_gen():
    from random import random, randint
    a = randint(0,255)
    b = randint(0, 255)
    c = randint(0, 255)
    return f"rgb({a},{b},{c})"

def list_of_hexa_colors(x):
    hexadecimal = 'abcdef0123456789'
    lists = []
    for i in range(x):
        hexa = '#' + ''.join(random.choices(hexadecimal, k=6))
        lists.append(hexa)
    return lists

def list_of_rgb_colors(x):
    lalist = []
    for i in range(x):
        lalist.append(rgb_color_gen())
    return lalist
    
def generate_colors(x, y):
    if x == 'hexa':
        return list_of_hexa_colors(y)
    elif x == 'rgb':
        return list_of_rgb_colors(y)
    else:
        return 'none'

def shuffle_list(lst):
    random.shuffle(lst)
    return lst 

def seven_random_numbers():
    return random.sample(range(10), k=7)