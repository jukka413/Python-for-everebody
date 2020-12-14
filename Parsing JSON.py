from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl
import json



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1050813.json"
js = urlopen(url, context=ctx).read()

info = json.loads(js)
print(info)
info = info['comments']
s = 0
for i in info:
    j = i['count']
    s = s + j
print(s)