paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

import re

def most_frequent_word(sentence):
    sentence_splitted = re.split(r'\w+', sentence)
    items = {}
    for item in sentence_splitted:
        if item in items:
            items[item] += 1
        else:
            items[item] = 1
    frequent_words = ((count, word) for count, word in items.items())
    enordre = sorted(frequent_words, reverse=True)
    return enordre


enonce = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'

sorted_points = re.findall('-?\d+', enonce)
int_sorted_points = [int(x) for x in sorted_points]
distance = max(int_sorted_points) - min(int_sorted_points)



def is_valid_variable(sttr):
    pattern = r"^[A-Za-z]+[A-Za-z0-9_]*$"
    return bool(re.match(pattern,  sttr))

def clean_text(sentencee):
    return re.sub('[^A-Za-z0-9 ]', '', sentencee)

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''


