# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies.update({'Youtube', 'Anthropic', 'OpenAI', 'Capgemini', 'Deepseek'})
print(it_companies)
it_companies.remove('Facebook')
print(it_companies)
#remove enleve un item et retourne erreur s'il n'y a pas l'item et discard enleve l'item et s'il est absent, ne retourne pas erreur
print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print((A.union(B)).union(B.union(A)))
print(A.symmetric_difference(B))
A.clear()
B.clear()

age = [22, 19, 24, 25, 26, 24, 25, 24]
print(set(age))
print(len(age) == len(set(age)))
print(len(age) < len(set(age)))
print(len(age) > len(set(age)))
#string est un texte pur entre '', une liste est un ensemble de 'string' entre[], 
# un tuple c'est comme une liste mais entre parentheses mais avec beaucoup moins d'options de formats, 
# un set est comme une liste entre {} avec des options de formattage plus eleves que les tuples et avec des 
# options de maths niveau lycée (intersection, union...)
sentence = "I am a teacher and I love to inspire and teach people"
split_sentence = sentence.split()
print(len(set(split_sentence)))

