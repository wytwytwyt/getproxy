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
		self.starturl = 'http://www.kuaidaili.com/ops/proxylist/'
		self.urls = self.get_urls()
		self.filename = 'proxy.txt'
		self.proxy_list = self.get_proxy(self.urls)
		self.savetofile(self.filename,self.proxy_list)


	def get_urls(self):
		'''
		url list
		'''
		urls = []
		for x in range(1,10):
			url = self.starturl + str(x)
			urls.append(url)
		return urls

	def get_proxy(self,urls):
		'''
		proxy list

		'''
		browser = webdriver.PhantomJS()
		proxy_list = []
		for url in urls:
			browser.get(url)
			browser.implicitly_wait(3)

			#find proxy
			elements = browser.find_elements_by_xpath('//tdbody/tr')

			for element in elements:
				item = Item()
				item.ip = element.find_elements_by_xpath('./td[1]').text
				item.port = element.find_elements_by_xpath('./td[2]').text
				item.anontmous = element.find_elements_by_xpath('./td[3]').text
				item.type = element.find_elements_by_xpath('./td[4]').text
				item.get_post = element.find_elements_by_xpath('./td[5]').text
				item.localadress = element.find_elements_by_xpath('./td[6]').text
				item.speed = element.find_elements_by_xpath('./td[7]').text
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

if __name__ == '__main__':
	Get = crawl()


