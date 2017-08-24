from selenium import webdriver

class Item(object):
	'''
	proxys

	'''
	ip = None
	port = None
	anontmous = None
	type = None
	get_post = None
	localadress = None
	speed = None 

class crawl(object):
	def __init__(self):
		print('initing')
		self.starturl = 'http://www.kuaidaili.com/free/inha/'
		self.urls = self.get_urls()
		self.filename = 'proxy.txt'
		self.proxy_list = self.get_proxy(self.urls)
		self.savetofile(self.filename,self.proxy_list)


	def get_urls(self):
		'''
		url list
		'''

		urls = []
		for x in range(1,3):
			url = self.starturl + str(x)
			urls.append(url)
		print('get urls  success')
		return urls

	def get_proxy(self,urls):
		'''
		proxy list

		'''
		browser = webdriver.PhantomJS()

		proxy_list = []
		for url in urls:
			print('browsering' + url)

			browser.get(url)
			browser.implicitly_wait(3)

			#find proxy
			print('finding elements')
			elements = browser.find_elements_by_xpath('//tbody/tr')
			

			for element in elements:
				print('dealing element')

				item = Item()
				item.ip = element.find_element_by_xpath('./td[1]').text
				print('ip get')
				item.port = element.find_element_by_xpath('./td[2]').text
				print('port get')

				item.anontmous = element.find_element_by_xpath('./td[3]').text
				print('anontmous get')

				item.type = element.find_element_by_xpath('./td[4]').text
				print('type get')

				item.get_post = element.find_element_by_xpath('./td[5]').text
				print('get_post get')

				item.localadress = element.find_element_by_xpath('./td[6]').text
				print('localadress get')
				
				item.speed = element.find_element_by_xpath('./td[7]').text
				print(' speed get')
				print(item.ip)
				proxy_list.append(item)
		browser.quit()
		return proxy_list

	def savetofile(self,filename,proxy_list):
		'''
		save proxys to file 

		'''
		with open(filename,'w') as f:
			for item in proxy_list:
				f.write(item.ip + '\t')
				f.write(item.port + '\t')
				f.write(item.anontmous + '\t')
				f.write(item.localadress + '\t')
				f.write(item.type + '\t')
				f.write(item.get_post + '\t')
				f.write(item.speed + '\n\n')
			print('saveing success')

if __name__ == '__main__':
	Get = crawl()


