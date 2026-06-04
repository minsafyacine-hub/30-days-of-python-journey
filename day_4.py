string1 = 'Thirty' + ' ' + 'Days' + ' ' +  'Of' + ' ' + 'Python'
print(string1)
string2 = 'Coding'+ ' ' + 'For' + ' ' + 'All'
print(string2)
company = "Coding For All"  
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(string2.capitalize()) 
print(string2.title())
print(string2.swapcase())
print(string2[0:6]) 
print(string2.find('Coding'))
print(string2.replace('Coding', 'Python'))
string3 = 'Python For Everyone'
print(string3.replace('Everyone', 'All')) 
print(string2.split(' '))
string4 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(string4.split(','))
print(string2[0])
print(string2[-1])
print(string2[11])
print(string3[0] + string3[7] + string3[11])
print(string2[0] + string2[7] + string2[11])
print(string2.index('C'))
print(string2.index('F'))
print(string2.rfind('i'))
string5 = "You cannot end a sentence with because because because is a conjunction"
print(string5.find('because'))
print(string5.rfind('because'))
print(string5[31:54]) 
print(string5.find('because'))
print(string2.startswith('Coding'))
print(string2.endswith('coding'))
string6 = '   Coding   '
print(string6.strip(' '))
string7 = '30DaysOfPython'
string8 = 'thirty_days_of_python'
print(string7.isidentifier())
print(string8.isidentifier())
list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("#".join(list))
print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square'.format(radius, area))
a = 8
b = 6
print( '{} + {} = {}'.format(a, b, a + b))
print( '{} - {} = {}'.format(a, b, a - b))
print( '{} * {} = {}'.format(a, b, a * b))
print( '{} / {} = {}'.format(a, b, a / b))
print( '{} % {} = {}'.format(a, b, a % b))
print( '{} // {} = {}'.format(a, b, a // b))
print( '{} ** {} = {}'.format(a, b, a ** b))