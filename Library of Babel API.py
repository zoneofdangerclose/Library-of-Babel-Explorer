import requests
import html

root_dir = 'https://libraryofbabel.info'

book_query = f'{root_dir}/book.cgi?'

# Enter any combination of up to 3260 numbers and/or lower case letters.
hex_var = 0
wall = 'w1'
shelf = 's1'
vol = 'v01'
page = 1
request = requests.get(f'{book_query}{hex_var}-{wall}-{shelf}-{vol}:{page}')
# request.status_code
print(html.unescape(request.text))
# https://libraryofbabel.info/book.cgi?0-w1-s1-v01:1


# <PRE id = "textblock">
# </PRE>