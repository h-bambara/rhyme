# -*- coding: utf-8 -*-
import re
from pykakasi import kakasi

def anotate(word):

    kakasi_ = kakasi()
    kakasi_.setMode('H', 'a') # H(Hiragana) to a(roman)
    kakasi_.setMode('K', 'a') # K(Katakana) to a(roman)
    kakasi_.setMode('J', 'a') # J(Kanji) to a(roman)

    conv = kakasi_.getConverter()

    rhyme = re.sub('[^aeiouAEIOU]', '', conv.do(word))

    return rhyme
