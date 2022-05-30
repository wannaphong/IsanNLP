# -*- coding: utf-8 -*-
from typing import List
from pythainlp.tokenize import Tokenizer
from pythainlp.corpus import thai_words
from isannlp.corpus import korat_list,nangrong_list_words

_word = Tokenizer(korat_list()+nangrong_list_words()+list(thai_words()), engine="newmm")

def word_tokenize(sent: str) -> List[str]:
    """
    Isan word tokenize
    :param str sent: Thai text
    :return: returns a list of Thai words
    :rtype: list
    """
    return _word.word_tokenize(sent)