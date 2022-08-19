import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1262306.xml'
xmldata = urlopen(url, context=ctx).read().decode()
tree = ET.fromstring(xmldata)
lst = tree.findall('.//count') #找到所有count tags，放入一个list
amount = list()
for item in lst:
    amount.append(float(item.text)) #已经定位到了count tag，而不用像xml2中再进行一次.find操作
print(sum(amount))