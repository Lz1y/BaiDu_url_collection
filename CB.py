# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup

def getHTMLText(url,timeout = 30):
	try:
		htl = requests.get(url,headers=headers)
		htl.raise_for_status()
		htl.encode = 'utf-8'
		return htl.text
	except:
		return ""

def findUrl(ulist, html):
	soup = BeautifulSoup(html, "html.parser")
	for u in soup.find_all(attrs={'class':'c-showurl'}):	
		if (u.string != None):
			st = u.string
			ulist.append(st)
	return ulist

def printUrl(ulist):
	print("url:")
	for u in ulist:
		if (u != None):
			print(u)
			
def tools1():
	with open("url.txt") as url:
		a  = "baidu"
		lines = url.readlines()
		for line in lines:
			if a in line:
				pass
			else:
				with open("urls.txt","a") as ulrs:
					ulrs.write(line)
			
def tools2():
	with open("urls.txt") as urls:
		url = urls.readlines()
	
	news_url = []
	for id in url:
		if id not in news_url:
			news_url.append(id)

	print(len(news_url))

	for i in range(len(news_url)):
		with open("edu.txt",'a') as edu:
			edu.write(news_url[i])

if __name__ == "__main__":


	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0"
	}
	
	keyword = input("what:")
	s_url = "http://www.baidu.com/s?wd=" + keyword
	num = int(input("how many:"))
	ulist = []
	for i in range(0,num):
		url = s_url + "&pn=" + str(i*10) + "&oq=" + keyword + "&ie=utf-8&usm=3&rsv_idx=1&rsv_pq=c1367a9d0000cd09&rsv_t=aab82N6IeY3zbB7gDAttzHxKJ%2BZz659gVpEFN9PPzuxMCtLAsGdpbh6YtIU"
		html = getHTMLText(url)
		findUrl(ulist, html)
	printUrl(ulist)
	for i in range(len(ulist)):
		ulist[i] = re.sub(r'/(.*)$',"",str(ulist[i]))	   
	with open('url.txt' ,'w',encoding='utf-8') as ul:
		
		for u in ulist:
			if (u != 'None'):
				ul.write(u)
				ul.write("\n")
				
	tools1()
	tools2()
	
	
