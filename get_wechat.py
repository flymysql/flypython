# 下载我的博客内容
from bs4 import BeautifulSoup
import requests,sys
import datetime

if __name__=='__main__':
	req=requests.get(url='https://mp.weixin.qq.com/s?__biz=MzI4MjU2NzEwNQ==&mid=2247484927&idx=1&sn=f8701e1bc199c05c0140104885106830&chksm=eb994d51dceec447de910fa83dc0b994aa4b132e047f8bca7093a70dece56ef37fb63008d6f3&scene=21#wechat_redirect')
	bf=BeautifulSoup(req.text,"html.parser")
	texts=bf.find_all('div',class_='rich_media_content')
	title=bf.find_all('h2',class_='rich_media_title')
	title=str(title[0].text)
	title=title[63:-82]
	title.replace('\n','')

	path=title+'.md'
	print(path)
	texts=(str(texts[0]).replace('data-src','src'))
	texts.replace('data-copyright="0"','')
	texts.replace('data-w','test1')
	write_flag=True
	with open(path,'a',encoding='utf-8') as f:
		f.write('---\ntitle: '+title+'\n')
		f.write('copyright: '+'true'+'\n')
		f.write('permalink: '+'1'+'\n')
		f.write('date: '+str(datetime.date.today())+'\n')
		f.write('updated: '+str(datetime.date.today())+'\n')
		f.write('tags: '+'资源'+'\n')
		f.write('categories: '+'资源'+'\n---\n\n')
		f.writelines(str(texts))