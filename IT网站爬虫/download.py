# test1

from bs4 import BeautifulSoup
import requests,sys

class downloader(object):


	#book配置初始化
	def __init__(book):
		book.server='http://www.biqukan.com/'
		book.target='http://www.biqukan.com/1_1094/'
		book.names=[]
		book.url=[]
		book.nums=0

	#获取链接
	def get_download_url(book):
		req = requests.get(url = book.target)
		html = req.text
		div_bf = BeautifulSoup(html,"html.parser")
		div = div_bf.find_all('div', class_ = 'listmain')
		a_bf = BeautifulSoup(str(div[0]))
		a = a_bf.find_all('a')
		book.nums = len(a[15:])                             #剔除不必要的章节，并统计章节数
		for each in a[15:]:
			book.names.append(each.string)
			book.url.append(book.server + each.get('href'))


	#获取每章内容
	def get_content(book,target):
		req=requests.get(url=target)
		html=req.text
		bf=BeautifulSoup(html,"html.parser")
		texts=bf.find_all('div',class_='showtxt')
		texts=texts[0].text.replace('\xa0'*8,'\n\n')
		return texts

	#将每章内容写入
	def writer(book,name,path,text):
		write_flag=True
		with open(path,'a',encoding='utf-8') as f:
			f.write(str(name)+'\n\n')
			f.writelines(str(text))
			f.write('\n\n')

if __name__=='__main__':
	getbook=downloader()
	getbook.get_download_url()
	print('《一念永恒》 开始下载：')
	for i in range(getbook.nums):
		getbook.writer(getbook.names,'一念永恒.txt',getbook.get_content(getbook.url[i]))
		sys.stdout.write("已下载：%0.3f%%" % float(i/getbook.nums)+'\r')
		sys.stdout.flush()
	print('《一念永恒》 下载完成')
