from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.PhantomJS()
driver.get('https://www.google.co.jp')


assert 'Google' in driver.title

input_element = driver.find_element_by_name('q')
input_element.send_keys('Python')
input_element.send_keys(Keys.RETURN)

assert 'Python' in driver.title

print(driver)

driver.save_screenshot('search_results.png')

for g_h3 in driver.find_elements_by_css_selector(".g h3"):
    print(g_h3.text)

for a in driver.find_elements_by_css_selector('h3 > a'):
	while True:
		try:
			print(a.text)
			print(a.get_attribute('href'))
			break
		except:
			print('エラー発生したけど続けるよ')
	print('一つ終了')



