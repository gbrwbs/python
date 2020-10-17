import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = " http://py4e-data.dr-chuck.net/comments_1018114.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

total = 0
elements = soup('span') 
for element in elements:
    num = element.contents[0]
    num = int(num)
    total = total + num

print(total)