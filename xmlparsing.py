import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1018116.xml"
data = urllib.request.urlopen(url).read()
print('Retrieving', url)
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
list = tree.findall('.//count')
print('Count:', len(list))

total = 0
for item in list:
    total = total + int(item.text)
print('Sum:', total)