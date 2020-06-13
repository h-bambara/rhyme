# -*- coding: utf-8 -*-
import MeCab
import re
import anotate_words

def divide_wordclass(file_line):
    mecab = MeCab.Tagger ('-Ochasen')

    result = mecab.parse(file_line)
    lines = result.split('\n')

    nounList = []#「名詞」を格納するリスト
    verbList = []#「動詞」を格納するリスト

    japanese = re.compile('[ぁ-んァ-ン一-龥]+')#日本語のみ抽出
    path = '' #動詞を吐き出すファイルを指定する
    f1 = open(path, 'a')
    path = '' #名詞を吐き出すファイルを指定する
    f2 = open(path, 'a')

    for line in lines:
        feature = line.split('\t')
        if len(feature) > 2:
            feature[0] = japanese.findall(feature[0])
            feature[0] = ''.join(feature[0])
            if feature[0] != "":
                wordclass = feature[3].split('-')
                if wordclass[0] == '名詞':
                    print('名詞: ' + feature[0] + ',' + feature[1] + ',' + anotate_words.anotate(feature[0]))
                    f1.write(feature[0] + ',' + feature[1] + ',' + anotate_words.anotate(feature[0]) + '\n')
                if wordclass[0] == '動詞':
                    print('動詞: ' + feature[0] + ',' + feature[1] + ',' + anotate_words.anotate(feature[0]))
                    f2.write(feature[0] + ',' + feature[1] + ',' + anotate_words.anotate(feature[0]) + '\n')
    f1.close()
    f2.close()
