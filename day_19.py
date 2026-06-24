def count_number_of_lines(file):
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        return f"number of lines : {len(lines)}"

def count_number_of_words(file):
    with open(file, 'r', encoding='utf-8') as f:
        words = f.read()
        leswords = words.split()
        return f"number of words : {len(leswords)}"
    
print(count_number_of_lines('./data/obama_speech.txt'))
print(count_number_of_words('./data/obama_speech.txt'))
print(count_number_of_lines('./data/michelle_obama_speech.txt'))
print(count_number_of_words('./data/michelle_obama_speech.txt'))
print(count_number_of_lines('./data/donald_speech.txt'))
print(count_number_of_words('./data/donald_speech.txt'))
print(count_number_of_lines('./data/melina_trump_speech.txt'))
print(count_number_of_words('./data/melina_trump_speech.txt'))

import json
def most_spoken_languages(file, x):
    with open(file,'r', encoding='utf-8') as f:
        lefile = json.load(f)
        languages = {}
        for country in lefile:
            for language in country['languages']:
                if language in lefile[languages]:
                    languages[language] += 1
                else:
                    languages[language] = 1
        leslanguages = [(number, language) for number, language in languages.items()]
        leslanguagess = sorted(leslanguages, reverse=True)
    return leslanguagess[:x]


def most_populated_countries(file, x):
    with open(file, 'r', encoding='utf-8') as f:
        lefile = json.load(f)
        countrypopulation = []
        for country in lefile:
            countrypopulation.append({"country : {country}, population : {population}"})
            countrypopulation = sorted(countrypopulation, key=lambda c: c['population'], reverse=True)
    return countrypopulation[:x]


with open('./data/email_exchange_big.txt', 'r') as f:
    listemails = f.readlines()

def  find_most_common_words(file, x):
    with open(file, 'r', encoding='utf-8') as f:
        lefile = f.read()
        words = lefile.split()
        leswords = {}
        for word in words:
            if word in leswords:
                leswords[word] += 1
            else:
                leswords[word] = 1
        listdeswords = [(number, word) for number, word in leswords.items()]
        listdeswordies = sorted(listdeswords, reverse=True)
        return listdeswordies[:x]
    
print(find_most_common_words('./data/obama_speech.txt', 10))
print(find_most_common_words('./data/michelle_obama_speech.txt', 10))
print(find_most_common_words('./data/donald_trump.txt', 10))
print(find_most_common_words('./data/melina_trump_speech.txt', 10))


def clean_text(file):
    with open(file, 'r', encoding='utf-8') as f:
        lefile = f.read().upper()
    return lefile.split()

from data.stop_words import stop_words
def remove_support_words(file):
    sf = clean_text(file)
    sfi = [word for word in sf if word not in stop_words]
    return sfi

def check_text_similarity(file, file2):
    csf = set(remove_support_words(file))
    csf2 = set(remove_support_words(file2))
    wordscommun = csf.intersection(csf2)
    wordstotaux = csf.union(csf2)
    return f"The poucentage of similarity is {len(wordscommun) / (len(wordstotaux)) * 100}"

print(check_text_similarity('./data/michelle_obama_speech.txt', './data/melina_trump_speech.txt')) 

print(find_most_common_words('./data/romeo_and_juliet.txt', 10))


import csv
import re
def number_of_lines(file, x):
    count = 0
    with open(file, 'r', encoding='utf-8') as f:
        lines = csv.reader(f)
        next(lines) 
        for line in lines:
            title = line[1]
            if re.search(x, title, re.IGNORECASE):
                count += 1
    return count

print(number_of_lines('./data/hacker_news.csv', 'python'))
print(number_of_lines('./data/hacker_news.csv', 'javascript'))
print(number_of_lines('./data/hacker_news.csv', 'Java'))

