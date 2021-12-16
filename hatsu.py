import os
import spacy as spacy
import json
from mymodule.Patent import Patent

path = './effect_words/'
effect_words = os.listdir(path)
dict_eff_words = dict.fromkeys(effect_words)

patents_list = []

for patent in dict_eff_words.keys():
    file_path = path+patent
    new = Patent(file_path)
    patents_list.append(new)

print(patents_list)

