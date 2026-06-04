# Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
# Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file
# Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). 
# The table is not very structured and the scrapping may take very long time.

import requests
from bs4 import BeautifulSoup
url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
soup = BeautifulSoup(response, 'html.parser')
response = response.json()

url2 = 'https://archive.ics.uci.edu/ml/datasets.php'
reponse = requests.get(url2)
print(reponse.status_code)
soupe = BeautifulSoup(reponse, 'html.parser')
dataset_links = soup.find_all('a', class_='font-bold')
leslinks = []
for link in dataset_links:
    if link.status_code==200:
        leslinks.append(link)
print(leslinks) 
    
url3 = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
answer = requests.get(url3)
soupee = BeautifulSoup(answer, ('html.parser'))
