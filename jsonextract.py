import json
import urllib.request


url = "http://py4e-data.dr-chuck.net/comments_1018117.json"
connection = urllib.request.urlopen(url)
data = connection.read().decode()
info = json.loads(data)
print('Retrieving', url)
print('Retrieved', len(data), 'characters')

total = 0
count = 0
for item in info['comments']:
    num = item['count']
    total = total + num
    count += 1

print('Count:', count)
print('Sum:', total)