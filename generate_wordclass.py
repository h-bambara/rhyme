# -*- coding: utf-8 -*-
import divide_wordclass
import anotate_words

def generate_wordclass(in_path, noun_path, verb_path):
    f = open(in_path, 'r')#読み込ませる文章が書かれたファイルのパスを引数で指定する
    line = f.readline()

    while line:
        divide_wordclass.divide_wordclass(line, noun_path, verb_path)
        line = f.readline()
    f.close()

    print("finish!")

