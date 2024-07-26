from english_words import get_english_words_set
import string
import os
import json

web2lowerset = list(get_english_words_set(['web2'], lower=True))

file_dir = os.getcwd().replace(os.path.basename(os.getcwd()),"")
explorer_dir = f'{file_dir}Library-of-Babel-Explorer/'

alphabet = string.ascii_lowercase

dict_shard = {}

for letter in alphabet:
    dict_shard.update({letter:[]})
    
for word in web2lowerset:
    dict_shard.update({word[0]: dict_shard[word[0]] + [word]})

open(f'{explorer_dir}data_dir/dictionary_shard.json', "w").write(json.dumps(dict_shard))