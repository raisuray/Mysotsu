from mymodule.Patent import Patent
from mymodule.findWords import *
from mymodule.discardP import *

import os
import spacy as spacy
import json

path = './effect_words/'
effect_words = os.listdir(path)
dict_eff_words = dict.fromkeys(effect_words)


patents_list = []

for patent in dict_eff_words.keys():
    file_path = path+patent
    new = Patent(file_path)
    patents_list.append(new)
 
#FIND ALL THE COMPOUND WORD IN ALL FILE#
nlp = spacy.load("ja_ginza")
for patent in patents_list:
    res = []
    list_of_compound_word = []
    print(patent.name)
    #print(len(patent.doc))

    for i in range(len(patent.doc_experiment)):
        
        doc_samp = nlp(patent.doc_experiment[i])
        if(check_symbol(doc_samp) == True and len(patent.doc_experiment[i]) <= 10):
            continue
        list_of_compound_word = find_noun_and_compound(doc_samp, i)
        res.extend(list_of_compound_word)        
    res = list(set(res))
    res = discard_Ascii(res)
    res = discard_word(res)
    dict_eff_words[patent.name] = res


#MAKE AN OUTPUT FILE#
path = "./out/"
with open(path + "out2.json", 'w') as f:
        json.dump(dict_eff_words,f, indent=4, ensure_ascii=False)