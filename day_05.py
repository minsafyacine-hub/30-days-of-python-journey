list1 = []
list2 = ['one', 'two', 'three', 'four', 'five', 'six']
print(len(list2))
print(list[0], list[2], list[5])
mixed_data_types = ['yacine', 20, 1.75, 'single', 'Pontoise']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0], it_companies[3], it_companies[-1]) 
it_companies.insert(0, 'OpenAI')
print(it_companies)
it_companies.append('Anthropic')
print(it_companies) 
it_companies.insert(3, 'MistralAI')
print(it_companies)
it_companies[-1] = 'ANTHROPIC'
print(it_companies)
print('#; '.join(it_companies))
print('Facebook' in it_companies)
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
three_first_companies_from_the_list = it_companies[0:3]
print(three_first_companies_from_the_list)
three_last_companies_from_the_list = it_companies[-3:]
print(three_last_companies_from_the_list)
the_middle_IT_company_from_the_list = it_companies[((len(it_companies)) // 2)]
print(the_middle_IT_company_from_the_list)
del it_companies[0]
print(it_companies)
del it_companies[len(it_companies) // 2]
print(it_companies)
del it_companies[-1]
print(it_companies)
del it_companies[0:] 
print(it_companies)
it_companies.clear()
print(it_companies)
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
print(front_end + back_end) 
full_stack = front_end + back_end
print(full_stack)

full_stack.insert(5, 'Python')
full_stack.insert(5, 'SQL')
full_stack.insert(5, 'Redux')

print(full_stack) 
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(min(ages), max(ages))
median_age = (ages[3] + ages[4]) / 2
print(median_age)
avarege_age = sum(ages)  / len(ages)
print(avarege_age)
range_of_ranges = (max(ages), (max(ages) - min(ages)), min(ages))
print(range_of_ranges)
print(abs(min(ages) - avarege_age) == abs(max(ages) - avarege_age))
print(abs(min(ages) - avarege_age) < abs(max(ages) - avarege_age))
print(abs(min(ages) - avarege_age) > abs(max(ages) - avarege_age))
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]
middle_country = countries[len(countries) // 2]
print(middle_country) 
first_list = countries[0:len(countries) // 2]
second_list = countries[len(countries) // 2:]
list_hh = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch, ru, usa, *scandiccountries = list_hh
print(scandiccountries)