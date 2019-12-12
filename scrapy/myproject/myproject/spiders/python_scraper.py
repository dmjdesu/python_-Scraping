import re
import sqlite3
from urllib.request import urlopen
from html import unescape
import urllib.request


# def main():
def main():
	html = fetch('https://gihyo.jp/dp')
	print(html)
	books = scrape(html)
	save('books.db', books)
# url = "https://gihyo.jp/dp"
# headers = {
#         "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
#         }

# request = urllib.request.Request(url=url, headers=headers)
# response = urllib.request.urlopen(request)
# html = response.read().decode('utf-8')

# print(html)

def fetch(url):
	url = "https://gihyo.jp/dp"
	headers = {
	        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
	        }

	request = urllib.request.Request(url=url, headers=headers)
	response = urllib.request.urlopen(request)
	html = response.read().decode('utf-8')


	return html

	# url = "https://gihyo.jp/dp"
	# headers = {
	#         "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
	#         }

	# request = urllib.request.Request(url=url, headers=headers)
	# response = urllib.request.urlopen(request)
	# html = response.read().decode('utf-8')
	# print(html)

def scrape(html):
	books = []
	for partial_html in re.findall(r'<a itemprop="url".*?</ul>\s*</a></li>', html, re.DOTALL):
		url = re.search(r'<a itemprop="url" href="(.*?)">', partial_html).group(1)
		url = 'https://gihyo.jp' + url

		title = re.search(r'<p itemprop="name".*?</p>', partial_html).group(0)
		title = re.sub(r'<.*?>',"", title)
		title = unescape(title)

		books.append({'url':url, 'title':title})

	return books


def save(db_path, books):
	conn = sqlite3.connect(db_path)
	c = conn.cursor()

	c.execute('DROP TABLE IF EXISTS books')

	c.execute("CREATE TABLE books (title text,url text)")

	c.executemany('INSERT INTO books VALUES (:title, :url)', books)

	c.execute('SELECT * FROM books')
	for row in c.fetchall():
		print(row)

	conn.commit()
	conn.close()

if __name__ == '__main__':
	main()
