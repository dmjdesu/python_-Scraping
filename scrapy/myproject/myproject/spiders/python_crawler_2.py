import requests
import lxml.html

response = requests.get('https://gihyo.jp/dp')
root = lxml.html.fromstring(response.content)
root.make_links_absolute(response.url)
for a in root.cssselect('#listBook a[itemprop="url"]'):
	url = a.get('href')
	print(url)