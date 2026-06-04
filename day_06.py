empty_tuple = ()
brother = ('saad',)
sister = ('zineb',)
siblings = brother + sister
print(siblings)
print(len(siblings))
siblings = list(siblings) 
father_and_mother = ['fouzia', 'abdessamad']
family_members = siblings + father_and_mother
family_members = tuple(family_members)
print(family_members)
brother, sister, mother, father = family_members
fruits = ('apple', 'bannana', 'grappe',)
vegetables = ('cucumber', 'tomato', 'botato')
animal_products = ('food', 'toys', 'animalproducts')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
food_stuff_it = list(food_stuff_tp)
print(food_stuff_it)
mid = len(food_stuff_it) // 2
print(food_stuff_it[mid: mid+1])
print((food_stuff_it[:3]) + (food_stuff_it[-3:]))
del food_stuff_tp
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
