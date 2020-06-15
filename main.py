# -*- coding: utf-8 -*-
import generate_wordclass
import glob

files = glob.glob("./wiki_data/*.txt")
i = 1
for file in files:
    nouns_path = "./nouns/nouns" + str(i) + ".csv"
    verbs_path = "./verbs/verbs" + str(i) + ".csv"
    generate_wordclass.generate_wordclass(file, nouns_path, verbs_path)
    i = i + 1