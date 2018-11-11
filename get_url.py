from bs4 import BeautifulSoup
import requests,sys
import datetime

class downloader(object):


	#total配置初始化
	def __init__(total):
		total.target='https://mp.weixin.qq.com/s/WtmuM7iLymCQ_P36BNenuA'
		total.titles=[]
		total.links=[]
		total.nums=0

	#获取所有文章链接与标题
	def get_download_url(total):
		req=requests.get(url=total.target)
		bf=BeautifulSoup(req.text,"html.parser")
		links=bf.find_all('a')
		links=links[1:-4]
		total.nums=len(links)
		for x in links:
			title=str(x.string)
			title=title[2:]
			total.titles.append(title)
			total.links.append(x.get('href'))

	#下载所有文章
	def download_c(total):
		the_links=total.links
		the_title=total.titles
		for i in range(total.nums):
			req=requests.get(url=the_links[i])
			bf=BeautifulSoup(req.text,"html.parser")
			texts=bf.find_all('div',class_='rich_media_content')
			# date=bf.find_all('em',class_='rich_media_meta rich_media_meta_text')
			# date=date[0].text
			title=the_title[i]
			path='公众号文章'+str(i+1)+'.md'
			texts=(str(texts[0]).replace('data-src','src'))
			texts.replace('data-copyright="0"','')
			texts.replace('data-w','test1')
			date='2017-5-'+str(i)+' 08:52:05\n'
			write_flag=True
			with open(path,'a',encoding='utf-8') as f:
				f.write('---\ntitle: '+title+'\n')
				f.write('copyright: '+'true'+'\n')
				f.write('permalink: '+'1'+'\n')
				f.write('date: '+date)
				f.write('updated: '+date)
				if i<37:
					f.write('tags: '+'资源'+'\n')
					f.write('categories: '+'资源'+'\n---\n\n')
				if i>37:
					f.write('tags: '+'\n- 随想\n- 邻家酒肆'+'\n')
					f.write('categories: '+'邻家酒肆'+'\n---\n\n')
				f.writelines(str(texts))
				sys.stdout.write("\t全部已下载：%0.3f%%" % float(i/total.nums)+'\n')
				sys.stdout.write("\t正在下载《" +title+"》\n")
				sys.stdout.flush()

if __name__=='__main__':
	get_total=downloader()
	get_total.get_download_url()
	print('\n\n\t开始爬取《小鸡资源库》所有文章：')
	get_total.download_c()
