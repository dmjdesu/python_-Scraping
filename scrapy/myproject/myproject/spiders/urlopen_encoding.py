# import sys
# from urllib.request import urlopen

# f = urlopen('https://gihyo.jp/dp')


# encoding = f.info().get_content_charset(failobj="utf-8")
# headers = {
#         "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
#         }
# print('encoding:', encoding, file=sys.stderr)

# text = f.read().decode(encoding)
# print(text)


import urllib.request

url = "https://gihyo.jp/dp"
headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
print(html)