import json
import urllib.request, urllib.error, urllib.parse

link = 'http://py4e-data.dr-chuck.net/comments_1262307.json'
Data = urllib.request.urlopen(link).read().decode()
print(Data)
info = json.loads(Data)
print(info)
counts = list()

for item in info['comments']:
    counts.append(item['count'])
print(counts)
print(sum(counts))