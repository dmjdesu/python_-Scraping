import requests
import lxml.html

def main():
	response = requests.get('https://gihyo.jp/dp')
	root = lxml.html.fromstring(response.content)
	for a in root.cssselect('a[itemprop="url"]'):
		url = a.get('href')
		print(url)

def scrape_list_page(response):
	root = lxml.html.fromstring(response.content)
	root.make_links_absolute(response.url)

	for a in root.cssselect('#listBook a[itemprop="url"]'):
		url = a.get('href')
		yield url

if __name__ == '__main__':
	main()

