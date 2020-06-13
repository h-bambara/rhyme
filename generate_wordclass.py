# -*- coding: utf-8 -*-
import divide_wordclass
import anotate_words

in_path = ''#読み込ませる文章が書かれたファイルのパスを記述する
f = open(in_path, 'r')
line = f.readline()

while line:
    #print(line)
    divide_wordclass.divide_wordclass(line)
    line = f.readline()
f.close()
