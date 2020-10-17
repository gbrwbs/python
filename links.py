import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Maias.html"
count = int(input("Enter count: "))
position = int(input("Enter position: "))

print("Retrieving:", url)

for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a') # Give a list of all anchor tags
    url = tags[position - 1].get('href', None)
    print("Retrieving:", url)