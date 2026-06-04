def count_number_of_lines(file):
    with open(file, 'w') as f:
        lines = f.readlines()
        list_of_lines = []
        for line in lines:
            if line in list_of_lines:
                list_of_lines = 1
            else:
                list_of_lines += 1
        return f"number of lines : {list_of_lines}"

def count_number_of_words(file):
    with open(file, 'r') as f:
        words = f.read()
        leswords = words.split()
        return f"number of words : {len(leswords)}"
    
print(count_number_of_lines('./data/obama_speech.txt'))
print(count_number_of_words('/data/obama_speech.txt'))
print(count_number_of_lines('/data/michelle_obama_speech.txt'))
print(count_number_of_words('/data/michelle_obama_speech.txt'))
print(count_number_of_lines('./data/donald_speech.txt'))
print(count_number_of_words('./data/donald_speech.txt'))
print(count_number_of_lines('./data/melina_trump_speech.txt'))
print(count_number_of_words('./data/melina_trump_speech.txt'))

import json
def most_spoken_languages(file, x):
    with open(file,'r', encoding='utf-8') as f:
        lefile = json.load()
        languages = {}
        for lang in lefile:
            if lang in languages:
                languages[lang] += 1
            else:
                languages[lang] = 1
        leslanguages = [(number, language) for number, language in lang.items()]
        leslanguagess = sorted(leslanguages, reverse=True)
    return leslanguagess[:x]

print(most_spoken_languages(countries_data.json, 10))

def most_populated_countries(file, x):
    with open(file, 'r') as f:
        lefile = f.read()
        for country in file:
            for population in country:
                listi = [{f"country : {country}, population : {population}"}]
                listii = sorted(listi, reverse=True)
    return listii[:x]

print(most_populated_countries(countries_data.json, 10))

with open('./data/email_exchange_big.txt', 'r') as f:
    listemails = f.readlines()

def  find_most_common_words(file, x):
    with open(file, 'r') as f:
        lefile = f.read()
        words = lefile.split()
        leswords = {}
        for word in words:
            if word not in leswords:
                leswords[word] += 1
            else:
                leswords[word] = 1
        listdeswords = [(number, word) for number, word in leswords.item()]
        listdeswordies = sorted(listdeswords, reverse=True)
        return listdeswordies[:x]
    
print(find_most_common_words('./data/obama_speech.txt', 10))
print(find_most_common_words('./data/michelle_obama_speech.txt', 10))
print(find_most_common_words('./data/donald_trump.txt', 10))
print(find_most_common_words('./data/melina_trump_speech.txt', 10))


def clean_text(file):
    with open(file, 'w') as f:
        lefile = f.read()
        upper_file = lefile.upper()
        splitted_file = upper_file.split()
    return splitted_file

def remove_support_words(file):
    with open(file, 'w') as f:
        sf = clean_text(f)
        for item in sf:
            for word in 'stop_words':
                if item == word:
                    sf.remove(item)
    return sf

def check_text_similarity(file, file2):
    with open(file, 'r') as f:
        with open(file2, 'r') as g:
            csf = remove_support_words(f)
            csf2 = remove_support_words(g)
            for item in csf:
                for item2 in csf2:
                    similar_words = []
                    if item == item2:
                        similar_words += 1
                    else:
                        similar_words = 1
    return f"The poucentage of similarity is {sum(similar_words) / (len(csf) + len(csf2)) * 100}"

print(check_text_similarity('./data/michelle_obama_speech.txt', './data/melina_trump_speech.txt')) 

print(find_most_common_words('./data/romeo_and_juliet.txt', 10))


import csv
import re
def number_of_lines(file, x):
    with open(file, 'r') as f:
        lines = csv.load()
        liness = lines.readlines()
        for line in liness:
            nmbrlines = []
            if (x, re.I) in line:
                nmbrlines = 1
            else:
                nmbrlines += 1
    return nmbrlines

print(number_of_lines(hacker_news.csv, 'python'))
print(number_of_lines(hacker_news.csv, 'javascript'))
print(number_of_lines(hacker_news.csv, 'Java'))

