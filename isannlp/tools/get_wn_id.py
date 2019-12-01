# -*- coding: utf-8 -*-
"""
Get WordNet ID
"""
from nltk.corpus import wordnet as wn
word = input("Word : ")
w = wn.synsets(word)
print(str(w))
while True:
    id = int(input("item : "))-1
    word_wn = w[id]
    print(word_wn.definition())
    print(word_wn.examples())
    print("WordNet ID : "+wn.ss2of(word_wn))
    print()