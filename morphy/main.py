import requests
import pymorphy2
from string import punctuation

url = 'http://fan.lib.ru/g/gejman_a/nek5.shtml'
req = requests.get(url).text.split('\n')

text = list(filter(lambda x: x.startswith('<dd>'), req))[5].replace('<dd>&nbsp;&nbsp;', '')
string = text
punctuation_counter = 0

for elem in text:
    if elem in punctuation:
        punctuation_counter += 1

for elem in punctuation:
    text = text.replace(elem, '')

text = text.split()
noun_counter = 0
verb_counter = 0

morph = pymorphy2.MorphAnalyzer(lang="ru")

for elem in text:
    if morph.parse(elem)[0].tag.POS == 'NOUN':
        noun_counter += 1
    elif morph.parse(elem)[0].tag.POS == 'VERB':
        verb_counter += 1

with open('answer.txt', 'w', encoding='utf-8') as file:
    print(string, file=file)
    print(file=file)
    print(f'Существительных: {noun_counter}', file=file)
    print(f'Глаголов: {verb_counter}', file=file)
    print(f'Знаков препинания: {punctuation_counter}', file=file)



