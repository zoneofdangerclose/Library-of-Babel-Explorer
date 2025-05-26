import re
import os
import json
import subprocess
from multiprocessing import Pool

# def word_filter(words: list[str]) -> list[str]:
#     word_list = []
#     for word in words:
#         # if re.match("\n", word):
#         word_len_temp = len(word)
#         #average word size between 4 and 8 letters
#         if word_len_temp < 3 or word_len_temp > 8:
#             continue
#         #handled ealier
#         # if word == '\n':
#         #     continue
#         #allowance for one special character per word, contractions and sentence punct
#         ##a more agressive filter would allow none
#         if len(re.findall('[^a-z]',word)) > 1:
#             continue
#         #average consonant to vowel ratio 60:40, expected random ratio 50:50 a little too close to be useful
#         word_list.append(word)

#     return word_list

file_dir = os.getcwd().replace(os.path.basename(os.getcwd()),"")
# print(os.getcwd())
file_dir = f'{file_dir}cgzho\\OneDrive\\Documents\\GitHub\\'
explorer_dir = f'{file_dir}Library-of-Babel-Explorer/'
pybel_cli = f'{file_dir}Library-Of-Pybel/library_of_babel.py'

# dictionary_shard_file = f'{explorer_dir}data_dir/dictionary_shard.json'
# dictionary_shard_dict = json.load(open(dictionary_shard_file))

trigram_file = f'{explorer_dir}data_dir/trigram_abbrv.txt'
trigram_set = set()
for trigram in open(trigram_file).readlines():
    trigram = trigram.replace('\n','')
    # trigram_dict.update({trigram: 0})
    trigram_set.add(trigram)

def word_filter(words: list[str]) -> list[str]:
    word_list = []
    for word in words:
        # if re.match("\n", word):
        word_len_temp = len(word)
        #average word size between 4 and 8 letters
        #bumped up to 3 and 14 for trigram filter
        if word_len_temp < 3 or word_len_temp > 14:
            continue
        #handled ealier
        # if word == '\n':
        #     continue
        #allowance for one special character per word, contractions and sentence punct
        ##a more agressive filter would allow none
        if len(re.findall('[^a-z]',word)) > 1:
            continue
        #average consonant to vowel ratio 60:40, expected random ratio 50:50 a little too close to be useful
        word_list.append(word)

    return word_list

def page_score(body_list: list[str]):
    page_score = 0

    for word in body_list:

        if len(word) > 3:
            word_prefix = word[0:3]
            word_suffix = word[len(word)-3:len(word)]
        else:
            word_prefix = word
            word_suffix = word

        if word_prefix in trigram_set:
            page_score +=1

        if word_suffix in trigram_set:
            page_score +=1
        # for tri_key in trigram_set:

        #     if word.find(tri_key) != -1:

        #         page_score += 1

    page_tri_ratio = page_score/len(body_list)
    
    page_score_dict = {'page_score': page_score,
                        'page_tri_ratio': page_tri_ratio,
                        }
    return page_score_dict




hex_var = 0
wall = 0
shelf = 4
# vol = 1
# page = 0

series = range(0,100)

def wordgen(series,hex_var=0,wall=0,shelf=5):
    vol = series
    # for vol in series:
    print(vol)
    query_dict = {}
    complete_freq_list = []
    defined_list = []

    pages_list = range(410)
    for page in pages_list:

        query_string = f'{hex_var}:{wall}:{shelf}:{vol}:{page}'
        body = subprocess.run(["python.exe", pybel_cli, '--checkout', query_string], capture_output=True, text=True)
        body = body.stdout

        body = re.sub('Title:.*\n', '', body)
        body = re.sub('\n', ' ', body)
        
        body_list = body.split(' ')

        word_list_filtered = word_filter(body_list)

        page_score_dict = page_score(word_list_filtered)

        if page_score_dict['page_tri_ratio'] >= 0.2:
            print('query string')
            print(f'{query_string}')
            print('trigram ratio')
            print(page_score_dict)


if __name__ == '__main__':
    

    Pool(2).map(wordgen, list(series))