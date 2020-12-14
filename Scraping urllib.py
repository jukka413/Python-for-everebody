from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

summ = 0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1050810.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    # print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    s = tag.contents[0]
    summ = summ + int(s)
    # print('Attrs:', tag.attrs)
print(summ)
