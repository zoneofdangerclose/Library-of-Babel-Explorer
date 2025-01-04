import re
import os
import json
import subprocess
from multiprocessing import Pool



file_dir = os.getcwd().replace(os.path.basename(os.getcwd()),"")
print(os.getcwd())
explorer_dir = f'{file_dir}Library-of-Babel-Explorer/'
pybel_cli = f'{file_dir}Library-Of-Pybel/library_of_babel.py'

dictionary_shard_file = f'{explorer_dir}data_dir/dictionary_shard.json'
dictionary_shard_dict = json.load(open(dictionary_shard_file))

# trigram_table_file = f'{explorer_dir}data_dir/trigram_table.txt'

def word_filter(words: list[str]) -> list[str]:
    word_list = []
    for word in words:
        # if re.match("\n", word):
        word_len_temp = len(word)
        #average word size between 4 and 8 letters
        if word_len_temp < 4 or word_len_temp > 8:
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

#in a rare case stackoverflow was actually pretty useful and taught me something
##the first argument of the subprocess.run must be an executable, which is very clear in the current docs https://docs.python.org/3/library/subprocess.html
###this is helpful in understanding that common bash commands like "ls" aren't magic text, they are references to the 
####bash standard library of executables, which explains why awk can sometimes be refered to as a seperate language, neat!
# subprocess.run(["python.exe", pybel_cli, "--help"])



hex_var = 0
wall = 0
shelf = 4
# vol = 1
# page = 0

series = range(40,100)

def wordgen(series,hex_var=0,wall=0,shelf=4):
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
        body = re.sub('\n', '', body)
        
        body_str = body.split(' ')

        word_list_filtered = word_filter(body_str)

        complete_freq_list.append(round(len(word_list_filtered)/len(body_str),3))

        # web2lowerset = get_english_words_set(['web2'], lower=True)
        

        word_list_filtered_defined = []

        for word in word_list_filtered:
            # print(word)
            first_char = word[0]

            if first_char not in dictionary_shard_dict.keys():
                continue

            shard_temp = dictionary_shard_dict[word[0]]
            if word in shard_temp:
                word_list_filtered_defined.append(word)

        if word_list_filtered_defined:

            print(f'Defined words: {word_list_filtered_defined}')

            query_dict.update({query_string: {'defined_list': word_list_filtered_defined,
                                            'percent_pass_filter': round(len(word_list_filtered)/len(body_str),3)
                                            }
                                }
                            )

        defined_list = defined_list + word_list_filtered_defined

    open(f'{explorer_dir}data_dir/passfilter_stats_{hex_var}_{wall}_{shelf}_{vol}.txt', "w").write(str(complete_freq_list))

    open(f'{explorer_dir}data_dir/defined_wordlist_{hex_var}_{wall}_{shelf}_{vol}.json', "w").write(json.dumps(query_dict))



if __name__ == '__main__':
    

    Pool(2).map(wordgen, list(series))