# -*- coding: UTF-8 -*-
#coding=utf-8
#!/usr/bin/python

from bs4 import BeautifulSoup
import requests,sys
import datetime
import random

tags = ['python','Android','Javascript','Java','Vue.js']

def get_url():
	tag = tags[random.randint(0,len(tags)-1)]
	for x in xrange(1,2):
		target = "https://so.csdn.net/so/search/s.do?p=" + str(x) + "&q=" + tag
		req = requests.get(url = target)
		bf = BeautifulSoup(req.text,"html.parser")
		post_links = bf.find_all('a')
		for ls in post_links:
			if '/article/details' in ls['href']:
				urls.append(ls['href'])
				print(ls['href'])


def getpost():
	link = 'https://blog.csdn.net/weixin_42784331/article/details/86499952'
	req = requests.get(url=link)
	bf = BeautifulSoup(req.text,"html.parser")
	texts = bf.find_all('article')[0]
	title = bf.find_all('h1',class_='title-article')[0].text
	print(title)
	time = bf.find_all('span',class_='time')[0].text
	time = time.replace(u'年',"-")
	time = time.replace(u'月',"-")
	time = time.replace(u'日',"")
	print(time)
	author = bf.find_all('a',class_='follow-nickName')[0].text
	print(author)
	tag = bf.find_all('a',class_='tag-link')[0].text
	print(tag)


if __name__ == '__main__':
	get_url()
