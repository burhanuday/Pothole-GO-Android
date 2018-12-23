import urllib.parse
import urllib.request
import urllib  # for #3
import os
from pprint import pprint
import random  # for # 4

'''
# 1
url = "https://storage.googleapis.com/potholego.appspot.com/Qe7ik9D.jpg_1545539333821"
f = urllib.request.urlopen(url)
pprint(f.read())
'''

'''
# 2
get_url = str(input("Enter url: "))
f = urllib.request.urlopen(get_url)
pprint(f.read())
'''

'''
# 3
f = open('00000001.jpg', 'wb')
f.write(urllib.request.urlopen('https://storage.googleapis.com/potholego.appspot.com/Qe7ik9D.jpg_1545539333821').read())
f.close()
'''


# 4
def download_image():
    get_url = str(input("Give URL: "))
    name = get_url.split("/")[-1]
    fullname = str(name) + ".jpg"
    urllib.request.urlretrieve(get_url, fullname)


download_image()