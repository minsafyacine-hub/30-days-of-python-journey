import requests
import json
from bs4 import BeautifulSoup

url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
donnes_boston = []
for element in soup.find_all(['h5', 'p']):
    lesliens = element.get_text(strip=True)
    if lesliens:
        donnes_boston.append(lesliens)
with open('exun.json', 'w', encoding='utf-8') as f:
    json.dump(donnes_boston, f, ensure_ascii=False, indent=4)

url2 = 'https://archive.ics.uci.edu/datasets'
reponse = requests.get(url2)
soupe = BeautifulSoup(reponse.text, 'html.parser')
les_tables = []
for element in soupe.find_all('a', class_='font-bold'):
    lelienss = element.get_text(strip=True)
    href = element.get('href')
    href_cache = f'https://archive.ics.uci.edu/{href}'
    if lelienss:
        les_tables.append({'nom' : lelienss, 'table' : href_cache})
with open('exdeux.json', 'w', encoding='utf-8') as f:
    json.dump(les_tables, f, ensure_ascii=False, indent=4)


url3 = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
answer = requests.get(url3)
soupee = BeautifulSoup(answer.text, 'html.parser')
lespresident = soupee.find('table', class_='wikitable')
lespresidents = lespresident.find_all(['tr'])
thepresidents = []
for line in lespresidents[1:]:
    lesspresidents = line.find_all(['td', 'th'])
    if len(lesspresidents) > 3:
        names = lesspresidents[2].get_text(strip=True)
        if "[" in names:
            names = names.split("[")[0]
        if names and not names.isdigit():
            thepresidents.append({'president name' : names})


with open('extrois.json', 'w', encoding='utf-8') as f:
    json.dump(thepresidents, f, ensure_ascii=False, indent=4)