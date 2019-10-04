# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count=int(input('Enter count:'))
position=int(input('Enter position:'))
j=0
for i in range(count+1):
    html = urllib.request.urlopen(url,context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    #print(url)  
    #print(html.decode())
    titles=soup('title')
    head=titles[0].contents[0]
    head=head.split()
    print(head[2])
# Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        if j!=position and tag.get('href', None)!=None:
            url=tag.get('href', None)
            j+=1
    j=0
    

