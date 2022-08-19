#网页循环点击链接，循环7次，每次点击第18个链接，最后输出该链接中的人名
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

n = 0
url = 'http://py4e-data.dr-chuck.net/known_by_Buddy.html'

while n < 7:
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    linklist = list()
    tags = soup('a')
    for tag in tags:
        tag = str(tag)
        link = re.findall('"(\S+?)"',tag)
        if len(link) != 1:
            continue
        else:
            linklist.append(link[0])
    print(linklist)
    url = linklist[17]
    n = n+1
print(url)
last_name = re.findall('known_by_(\S+?)\.',url)
print(last_name[0])
