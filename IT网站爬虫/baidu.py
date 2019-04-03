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
	for every_day in today[1:]:
		tds = every_day.find_all('td')
		d1 = tds[0].text.replace(' ','').replace('\n','')
		d2 = tds[1].text.replace(' ','').replace('\n','')
		d3 = tds[2].text.replace(' ','').replace('\n','')
		d4 = tds[3].text.replace(' ','').replace('\n','')
		print('\t' + city+d1)
		ws.append([city,d1,d2,d3,d4])
	

def get_month(city,urals):
	print(city)
	year = 2017
	while 1 + 2 == 3:
		month = 1
		while month < 13:
			if month < 10:
				url = 'http://www.tianqihoubao.com/lishi/' + urals +'/month/' + str(year) + '0' + str(month) + '.html'
			else:
				url = 'http://www.tianqihoubao.com/lishi/' + urals +'/month/' + str(year)  + str(month) + '.html'
			get_tianqi(url,city)
			month = month + 1
		year = year + 1
		if year == 2019:
			break

def city():
	req = requests.get(url='http://www.tianqihoubao.com/weather/province.aspx?id=620000')
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
		city()
	except:
		print('error')
	wb.save("tianqi.xlsx")
	
	