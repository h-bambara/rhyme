# -*- coding: utf-8 -*-
import re
from pykakasi import kakasi

def anotate(word):

    kakasi_ = kakasi()
    kakasi_.setMode('H', 'a') # H(Hiragana) to a(roman)
    kakasi_.setMode('K', 'a') # K(Katakana) to a(roman)
    kakasi_.setMode('J', 'a') # J(Kanji) to a(roman)

    conv = kakasi_.getConverter()

    phonetic = conv.do(word)
    rhyme = re.sub('[^aeiouAEIOU]', '', phonetic)

    rhyme_set = phonetic + ',' + rhyme

    return rhyme_set
