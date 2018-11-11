由于以前公众号发了挺多分享资源的文章，索性写个python爬虫来爬取

特点：
1. 保留公众号排版样式（就是把div样式全拷下来了）
2. 写成md格式，并且加了hexo渲染需要的头部
3. **解除了微信图片防盗链的限制！！！**

不过一次只能抓一篇文章（不过我是因为之前公众号有一篇文章发了链接合集，所以直接全都下载了）

脚本放在GitHub练习库里
https://github.com/flymysql/flypython

<!--more-->
下面是抓取单篇的python

```python

# 下载我的博客内容
from bs4 import BeautifulSoup
import requests,sys
import datetime

if __name__=='__main__':
	reurl = input("粘贴要抓取的文章链接:")
	req=requests.get(url=reurl)
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

```