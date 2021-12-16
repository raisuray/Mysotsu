import os
import spacy as spacy
import json
from mymodule.Patent import Patent
import pprint
import regex

path = './effect_words/'
effect_words = os.listdir(path)
dict_eff_words = dict.fromkeys(effect_words)

patents_list = []

for patent in dict_eff_words.keys():
    file_path = path+patent
    new = Patent(file_path)
    patents_list.append(new)


pattern = "[(.*ように)]"
nlp = spacy.load("ja_ginza")

for patent in patents_list:
    print(patent.name)
    inv_words = patent.doc_invention

    for inv_word in inv_words:
        sentences = inv_word.split("、")

        for sentence in sentences:
            doc = nlp(sentence)
            for span in doc:
                print(span.text, span.head, span.)


        break
    break

