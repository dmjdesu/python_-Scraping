from robobrowser import RoboBrowser

browser = RoboBrowser(parser='html.parser')
browser.open('https://www.google.co.jp/')

form = browser.get_form(action='/search')

browser.submit_form(form, list(form.submit_fields.values())[0])

src = str(browser.parsed)
print(str)

for a in browser.select('h3 > a'):
	print(a.text)
	print(a.get('href'))
	
