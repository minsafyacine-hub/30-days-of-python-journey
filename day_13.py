numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers = [number for number in numbers if number <= 0]

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_of_lists = [number for list in list_of_lists for number in list]

list_comprehension = [(i, 1, i, i ** 2, i ** 3, i ** 4, i ** 5, i ** 6) for i in range(11)]

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries = [[sub[0].upper(), sub[0].upper()[0:3], sub[1].upper()] for item in countries for sub in item] 

countries = [{'country': sub[0].upper(), 'city': sub[1].upper()} for item in countries for sub in item]

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
names = [f"{name[0]} {name[1]}" for item in names for name in item]

solve_a_slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)