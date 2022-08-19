from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
comment = list()

url = 'http://py4e-data.dr-chuck.net/comments_1262304.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    tag = str(tag) #需要将tags中的每一项转换为字符串
    num = re.findall('\>(\S+?)\<',tag)
    if len(num) != 1:
        continue
    else:
        comment.append(float(num[0]))
print(comment)
amount = sum(comment)
print(amount)