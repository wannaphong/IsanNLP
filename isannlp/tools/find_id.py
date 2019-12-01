# -*- coding: utf-8 -*-
"""
Get definition and examples from WordNet ID
"""
from nltk.corpus import wordnet as wn
word = input("WordNet ID : ")
word_wn = wn.of2ss(word.replace('-',''))
print(word_wn.definition())
print(word_wn.examples())
print("WordNet ID : "+wn.ss2of(word_wn))