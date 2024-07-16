import requests
import html
import re
import os
from english_words import get_english_words_set
import json
import string
import random
import sys
import subprocess
import glob
import plotly.express as px



# data_dir = 
# print(os.path.expanduser('~'))
# print(os.getcwd())
# print(os.path.basename(os.getcwd()))
# print(os.getcwd().replace(os.path.basename(os.getcwd()),""))

file_dir = os.getcwd().replace(os.path.basename(os.getcwd()),"")
explorer_dir = f'{file_dir}Library-of-Babel-Explorer/'
data_dir = f'{explorer_dir}data_dir/'

# print(f'{data_dir}*.json')
# print(glob.iglob(f'{data_dir}*.json'))

json_files = glob.iglob(f'{data_dir}*.json')
# finite = 0
word_count = 0
one_pass_filter_list = []
more_pass_filter_list = []
for file in json_files:
    # if finite < 1:
    json_dict = json.load(open(file))
    keys = json_dict.keys()
    for key in keys:
        word_count_temp = len(json_dict[key]['defined_list'])
        word_count = word_count + word_count_temp

        if word_count_temp == 1:
            one_pass_filter_list.append(json_dict[key]['percent_pass_filter'])
        else:
            more_pass_filter_list.append(json_dict[key]['percent_pass_filter'])
        # print(json_dict[key]['percent_pass_filter'])
    # finite += 1

print(word_count)
print(one_pass_filter_list)
print(more_pass_filter_list)

# def word_filter(words: list[str]) -> list[str]:
#     word_list = []
#     for word in words:
#         # if re.match("\n", word):
#         word_len_temp = len(word)
#         #average word size between 4 and 8 letters
#         if word_len_temp < 4 or word_len_temp > 8:
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

# file_dir = 'C:/Users/cgzho/OneDrive/Documents/GitHub/'

# explorer_dir = f'{file_dir}Library-of-Babel-Explorer/'
# pybel_cli = f'{file_dir}Library-Of-Pybel/library_of_babel.py'

# #in a rare case stackoverflow was actually pretty useful and taught me something
# ##the first argument of the subprocess.run must be an executable, which is very clear in the current docs https://docs.python.org/3/library/subprocess.html
# ###this is helpful in understanding that common bash commands like "ls" aren't magic text, they are references to the 
# ####bash standard library of executables, which explains why awk can sometimes be refered to as a seperate language, neat!
# # subprocess.run(["python.exe", pybel_cli, "--help"])

# # root_dir = 'https://libraryofbabel.info'

# # book_query = f'{root_dir}/book.cgi?'

# # Enter any combination of up to 3260 numbers and/or lower case letters.
# # hex_var = 0
# # wall = 'w1'
# # shelf = 's1'
# # vol = 'v01'
# # page = 1

#     # request = requests.get(query_string)
#     # request_page = request.text

#     # body = re.search('<PRE id = "textblock">.*</PRE>', request_page, flags=re.DOTALL).group()
#     # body = body[23:-6]
#     # open(f'{file_dir}body_{page}.txt', "w").write(body)

#     # request.status_code
#     # print(html.unescape(request.text))
#     # https://libraryofbabel.info/book.cgi?0-w1-s1-v01:1
#     # print(re.search('<PRE id = "textblock">.*</PRE>', request_page, flags=re.DOTALL).group())
#     # <PRE id = "textblock">
#     # </PRE>

#     # body = open(f'{file_dir}body.txt', 'r').read()


# hex_var = 0
# wall = 1
# shelf = 1
# vol = 1
# page = 0

# query_string = f'{hex_var}:{wall}:{shelf}:{vol}:{page}'
# print(query_string)

# subprocess.run(["python.exe", pybel_cli, '--checkout', query_string])

# # pages_list = range(1)
# # for page in pages_list:
# #     # print(page)
# #     query_string = f'{hex_var}:{wall}:{shelf}:{vol}:{page}'
# #     print(query_string)
# #     # subprocess.run(["python.exe", pybel_cli, f'--checkout {query_string}'])
# #     subprocess.run(["python.exe", pybel_cli, f'--checkout 98756SDH987S:2:3:14:345'])