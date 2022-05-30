# -*- coding: utf-8 -*-
import os
from typing import List

import isannlp
import pandas as pd

isannlp_path = os.path.dirname(isannlp.__file__)
corpus_path = os.path.join(isannlp_path,"corpus")


def korat_list() -> List[str]:
    with open(os.path.join(corpus_path,"korat_listword.txt"),"r",encoding="utf-8-sig") as f:
        return [i.strip() for i in f.readlines()]


def nangrong_words():
    df = pd.read_csv(os.path.join(corpus_path,"nangrong_words.txt"),sep=",")
    return df


def nangrong_list_words():
    _df = nangrong_words()
    return [str(i) for i in _df['word']]
