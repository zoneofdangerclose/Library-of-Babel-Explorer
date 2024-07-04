import requests
import html
import re
import os

file_dir = 'C:/Users/cgzho/OneDrive/Documents/GitHub/Library-of-Babel-Explorer/'

root_dir = 'https://libraryofbabel.info'

book_query = f'{root_dir}/book.cgi?'

# Enter any combination of up to 3260 numbers and/or lower case letters.
hex_var = 0
wall = 'w1'
shelf = 's1'
vol = 'v01'
page = 1
# request = requests.get(f'{book_query}{hex_var}-{wall}-{shelf}-{vol}:{page}')
# request_page = request.text

# body = re.search('<PRE id = "textblock">.*</PRE>', request_page, flags=re.DOTALL).group()
# body = body[23:-6]
# open(f'{file_dir}body.txt', "w").write(body)



# request.status_code
# print(html.unescape(request.text))
# https://libraryofbabel.info/book.cgi?0-w1-s1-v01:1
# print(re.search('<PRE id = "textblock">.*</PRE>', request_page, flags=re.DOTALL).group())
# <PRE id = "textblock">
# </PRE>

body = open(f'{file_dir}body.txt', 'r').read()
# print(body)
body = body.replace('\n', '')
# print(body)
body_str = ''
body_str = body_str.join(body)
body_str = body_str.split(' ')

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


word_list_filtered = word_filter(body_str)
# print(word_list_filtered)
print(f'words passed filter: {round(len(word_list_filtered)/len(body_str),2)}%')

