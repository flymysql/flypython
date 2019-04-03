#pytest
#coding=utf-8
#!/usr/bin/python
# 作者： flyphp@outlook.com

from bs4 import BeautifulSoup
import requests,sys
import datetime
from openpyxl import Workbook

wb = Workbook()
ws = wb.get_sheet_by_name('Sheet')
def get_tianqi(urls,city):
	req = requests.get(url=urls)
	bf = BeautifulSoup(req.text,"html.parser")
	today = bf.find_all(name='tr')
	city='lanzhou'
	for every_day in today[1:]:
		tds = every_day.find_all('td')
		d1 = tds[0].text.replace(' ','').replace('\n','')
		d2 = tds[1].text.replace(' ','').replace('\n','')
		d3 = tds[2].text.replace(' ','').replace('\n','')
		d4 = tds[3].text.replace(' ','').replace('\n','')
		d5 = tds[4].text.replace(' ','').replace('\n','')
		d6 = tds[5].text.replace(' ','').replace('\n','')
		d7 = tds[6].text.replace(' ','').replace('\n','')
		d8 = tds[7].text.replace(' ','').replace('\n','')
		d9 = tds[8].text.replace(' ','').replace('\n','')
		d10 = tds[9].text.replace(' ','').replace('\n','')
		print('\t' + city+d1)
		ws.append([city,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10])
	

def get_month():
	city='lanzhou'
	year = 2017
	while 1 + 2 == 3:
		month = 1
		while month < 13:
			if month < 10:
				url = 'http://www.tianqihoubao.com/aqi/lanzhou-'  + str(year) + '0' + str(month) + '.html'
			else:
				url = 'http://www.tianqihoubao.com/aqi/lanzhou.html'  + str(year) + str(month) + '.html'
			get_tianqi(url,city)
			month = month + 1
		year = year + 1
		if year == 2019:
			break

def city():
	req = requests.get(url='http://www.tianqihoubao.com/aqi/lanzhou.html')
	bf = BeautifulSoup(req.text,"html.parser")
	today = bf.find_all(name='td')
	for citys in today:
		try:
			
			link = citys.find('a')
			cname = link.get('href').replace('top/','').replace('.html','')
			get_month(link.text, cname)
			
		except:
			print('error')

if __name__=='__main__':
	try:
		get_month()
	except:
		print('error')
	wb.save("lanzhou.xlsx")
	
	
