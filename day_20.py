import requests
url = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(url)
urlsplitted = response.text.split()
listwords = {}
for word in urlsplitted:
    if word in listwords:
        listwords[word] += 1
    else:
        listwords[word] = 1
mostspokenwords = [(number, word) for word, number in listwords.items()]
mostspokenwords = sorted(mostspokenwords, reverse=True)
print(mostspokenwords[:10])

import pandas as pd
url2 = 'https://api.thecatapi.com/v1/breeds'
reponse = requests.get(url2)
reponse = reponse.json() 
catweightsmetrics = []
for cat in reponse:
    catweight = cat['weight']['metric']
    catweight = catweight.split(' - ')
    lesweight = (int(catweight[0]) + int(catweight[1])) / 2
    catweightsmetrics.append(lesweight)
series_poids = pd.Series(catweightsmetrics)
print(series_poids.min())
print(series_poids.max())
print(series_poids.mean())
print(series_poids.std())

lifespann = []
for chat in reponse:
    lifespan = chat['life_span']
    lifespan = lifespan.split(' - ')
    leslifespan = ((int(lifespan[0]) + int(lifespan[1])) / 2)
    lifespann.append(leslifespan)
series_lifespan = pd.Series(lifespann)
print(series_lifespan.min())
print(series_lifespan.max())
print(series_lifespan.mean())
print(series_lifespan.std())

list_of_origines = []
for chat in reponse:
    list_of_origines.append(chat['origin'])
series_origine = pd.Series(list_of_origines)
print(series_origine.value_counts())

url3 = 'https://restcountries.com/v3.1/all?fields=name,area'
lurl3 = requests.get(url3)
lurl3 = lurl3.json()

lapopulation = []
for country in lurl3:
    if 'area' in country:
        lapopulation.append({ 'name' : country['name']['common'],'area' : country['area']})
populationenordre = sorted(lapopulation, key= lambda a: a['area'], reverse=True)
les10largestcountries = populationenordre[:10]
print(les10largestcountries)

languagess = {}
for country in lurl3:
        dict_lang = (country.get('languages', {}))
        for lang_name in dict_lang.values():
            if lang_name in languagess:
                languagess[lang_name] += 1
            else:
                languagess[lang_name] = 1
leslangues = [(number, language) for language, number in languagess.items()]
leslangues = sorted(leslangues, reverse=True)
les10mostspokenlanguages = leslangues[:10]
print(les10mostspokenlanguages)

leslanguages = []
for language in leslangues:
    leslanguages.append(language)
print(len(leslanguages))


from bs4 import BeautifulSoup
url4 = 'https://archive.ics.uci.edu/datasets'
responsi = requests.get(url4)
soup = BeautifulSoup(responsi.text, 'html.parser')
dataset_links = soup.find_all('a', class_='font-bold')
for link in dataset_links:
    nom_link = link.get_text(strip=True)
    print(nom_link)