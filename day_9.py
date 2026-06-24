age = int(input("Enter your age"))
if age >= 18:
    print("You are old enough to drive")
else:
    print(f"You need {18 - age} more years to learn to drive")

my_age = 20
your_age = int(input("Enter your age"))
if my_age < your_age:
    print(f"You are {your_age - my_age} years older than me")
elif my_age == your_age:
    print("We were born the same year")
else:
    print(f"I am {my_age - your_age} years older than you")

a = int(input("Enter a number"))
b = int(input("Enter another number"))
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is smaller than b")
else:
    print("a is equal to b")

score = int(input("What is your score ?"))
if 100 >= score >= 90:
    print("Your grade is A")
elif 89 >= score >= 80:
    print("Your score is B")
elif 79 >= score >= 70:
    print("Your grade is C")
elif 69 >= score >= 60:
    print("Your grade is D")
else:
    print("Your grade is F") 

month = input("Enter the month")
if month == 'September' or month == 'October' or month == 'November' or 'December' or month == 'January' or month == 'February' or month == 'March' or month == 'April' or month == 'May' or month == 'June' or month == 'July' or month == 'August': 
    if month == 'September' or month == 'October' or month == 'November':
        print("The season is Autumn")
    elif month == 'December' or month == 'January' or month == 'February':
        print("The season is Winter")
    elif month == 'March' or month == 'April' or month == 'May':
        print("The season is Spring")
    elif month == 'June' or month == 'July' or month == 'August':
        print("The season is Summer")
else: 
    print("This is not a month")

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit")
if fruit not in fruits:
    fruits.append(fruit)
    print(fruits)
elif fruit in fruits:
    print("The fruit already exists in the list") 

person={
    'first_name' : 'Asabeneh',
    'last_name' : 'Yetayeh',
    'age' : 250,
    'country' : 'Finland',
    'is_married' : True,
    'skills' : ['Javascript', 'React', 'Node', 'MongoDB', 'Python'],
    'adress': {
        'rue' : '10 avenue adolphe chauvin',
        'code_postal' : '95300'
    }
}

if 'skills' in person:
    print(person['skills'][1])
    if 'JavaScript' in person['skills'] and 'React' in person['skills']:
        print("He is a frontend developer")
    elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
        print("He is a backend developer")
    elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
        print("He is a fullstack developer")
    else:
        print("unknown title")
    if 'Python' in person['skills']:
        print(person['skills'])
if person['is_married'] == True and person['country'] == 'Finland':
    print("Asabeneh Yetayeh lives in Finland. He is married")


