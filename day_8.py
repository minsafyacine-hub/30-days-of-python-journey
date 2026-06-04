dog = {}
dog['name'] = 'rex'
dog['color'] = 'black'
dog['breed'] = 'malinois'
dog['legs'] = 4
dog['age'] = 20
print(dog)
student_dictionary = {
    'first_name' : 'yacine',
    'last_name' : 'minsaf',
    'gender' : 'man',
    'age' : 20,
    'marital_status' : 'single',
    'skills' : ['nada'],
    'country' : 'france',
    'city' : 'pontoise'
}
print(len(student_dictionary))
print(student_dictionary['skills'])
print(type(student_dictionary['skills'])) 
student_dictionary['skills'].append('rien')
student_dictionary['skills'].append('nothing') 
print(student_dictionary['skills'])
print(list(student_dictionary.keys()))
print(type(student_dictionary)) 
print(student_dictionary.values())
print(student_dictionary.items())
print(student_dictionary.pop('skills'))
del dog



dog = {}
dog['name'] = 'rex'
dog['color'] = 'black'
dog['breed'] = 'malinois'
dog['legs'] = 4
dog['age'] = 20
student_dictionary = {
    'first_name' : 'yacine',
    'last_name' : 'minsaf',
    'gender' : 'man',
    'age' : 20,
    'marital_status' : 'single',
    'skills' : ['rien'],
    'country' : 'france',
    'city' : 'pontoise'
}
print(len(student_dictionary))
print(student_dictionary['skills']) 
print(type(student_dictionary))
student_dictionary['skills'].append('nada')
student_dictionary['skills'].append('nothing')
print(list(student_dictionary.keys()))
print(list(student_dictionary.values()))
print(list(student_dictionary.items()))
print(student_dictionary.pop('skills'))
del dog