#pytest
#coding=utf-8
#!/usr/bin/python
# IT网站文章爬虫
# 作者：小鸡  flyphp@outlook.com

import pymysql
import time
from bs4 import BeautifulSoup
import requests,sys
import datetime
import re

# 连接数据库需要，IP，user，密码，库名
db = pymysql.connect(host='localhost', user="root", passwd='your passwd', db='www_idealli_com')
cur_tag = ''
today = '2019-02-18 18:09:06'
urls = []
tar = []
link_head = "https://juejin.im"
otar = []
ourls = []
ii = 0
it = 0
cur_page_num = 0
cur_tag_num = 24
last_post_id = 0
check_title_time = 1
# url_fo = open("mysql_urls.log", "w")
# car_fo = open("mysql_cars.log", "w")


#################################################
# 		文章插入，数据库部分
#################################################
def tag_id(tag_name):
	# check tag
	cursor = db.cursor()
	check_tag = "SELECT `term_id` FROM `wp_terms` WHERE `name` = '" + tag_name + "'"
	try:
		cursor.execute(check_tag)
	except Exception as e:
		print(e)
	tag_id = cursor.fetchone()
	tag_data = cursor.fetchall()
	if tag_id is None:
		try:
			insert_tag = "INSERT INTO `wp_terms` (`term_id`, `name`, `slug`, `term_group`) VALUES (NULL, '"+ tag_name +"','" + tag_name + "', '0')"
			cursor.execute(insert_tag)
			cursor.execute(insert_tag)

			check_tag = "SELECT `term_id` FROM `wp_terms` WHERE `name` = '" + tag_name + "'"
			cursor.execute(check_tag)
			tag_data = cursor.fetchall()
			insert_taxonomy_tag = "INSERT INTO `wp_term_taxonomy` (`term_taxonomy_id`, `term_id`, `taxonomy`, `description`, `parent`, `count`) VALUES (NULL, '" + str(tag_data[0][0]) + "', 'post_tag', '', '0', '1')"
			insert_taxonomy_category = "INSERT INTO `wp_term_taxonomy` (`term_taxonomy_id`, `term_id`, `taxonomy`, `description`, `parent`, `count`) VALUES (NULL, '" + str(tag_data[1][0]) + "', 'category', '', '0', '1')"

			cursor.execute(insert_taxonomy_tag)
			cursor.execute(insert_taxonomy_category)
			db.commit()
		except Exception as e:
			print(e)
			db.rollback()
	try:
		cursor.execute(check_tag)
	except Exception as e:
		print(e)
	tag_data = cursor.fetchall()
	check_taxo = "SELECT `term_taxonomy_id` FROM `wp_term_taxonomy` WHERE `term_id` = '" + str(tag_data[0][0]) + "'" + "or `term_id` = '" + str(tag_data[1][0]) + "'"
	try:
		cursor.execute(check_taxo)

	except Exception as e:
		print(e)
	#print(cursor.fetchall())
	taxo_data = cursor.fetchall()
	return taxo_data


def insert_post(ti,au,con,tag_idd, tim,sum,db):
	title = ti.encode('utf-8')
	author = au.encode('utf-8')
	global last_post_id
	global check_title_time
	last_post_id = last_post_id +1
	content = con
	summ = sum.replace("'","`")
	content = content.replace("'","`")
	time = tim
	cursor = db.cursor()
	taxo_data = tag_idd
	post_id = last_post_id

	# check author
	check_author = "SELECT `ID` FROM `wp_users` WHERE `display_name` LIKE '" + author + "'"
	cursor = db.cursor()
	cursor.execute(check_author)
	author_id = cursor.fetchone()
	check_title = 1
	if author_id is None:
		insert_author = "INSERT INTO `wp_users` (`ID`, `user_login`, `user_pass`, `user_nicename`, `user_email`, `user_url`, `user_registered`, `user_activation_key`, `user_status`, `display_name`) VALUES (NULL, '', '', '', '', '', '0000-00-00 00:00:00.000000', '', '0', '" + author +"')"
		try:
			cursor.execute(insert_author)
			db.commit()
		except Exception as e:
			db.rollback()
		check_author = "SELECT `ID` FROM `wp_users` WHERE `display_name` LIKE '" + author + "'"
		cursor.execute(check_author)
		author_id = cursor.fetchone()
	else:
		check_title = 0
		try:
			cursor.execute("SELECT `ID` FROM `wp_posts` WHERE `post_title` = '" + title + "'")
		except:
			pass
		data = cursor.fetchone()
		if data is None:
			check_title = 1
	if check_title == 1:
		# creat new post
		post_id = str(last_post_id)
		insert_post = "INSERT INTO `wp_posts` (`ID`, `post_author`, `post_date`, `post_date_gmt`, `post_content`, `post_title`, `post_excerpt`, `post_status`, `comment_status`, `ping_status`, `post_password`, `post_name`, `to_ping`, `pinged`, `post_modified`, `post_modified_gmt`, `post_content_filtered`, `post_parent`, `guid`, `menu_order`, `post_type`, `post_mime_type`, `comment_count`) VALUES (" + post_id + ", '" + str(author_id[0]) + "', '" + str(time) + "', '" + str(time) + "', '" + str(content) + "', '" + str(title) + "', '" + summ + "', 'publish', 'open', 'open', '', '', '', '', '" + str(time) + "', '" + str(time) + "', '', '0', '', '0', 'post', '', '0')"
		try:

			cursor.execute(insert_post)

			insert_relationship = "INSERT INTO `wp_term_relationships` (`object_id`, `term_taxonomy_id`, `term_order`) VALUES ('" + str(post_id) + "', '" + str(taxo_data[0][0]) + "', '0')"
			cursor.execute(insert_relationship)
			update_taxo = "UPDATE `wp_term_taxonomy` SET `count` = `count`+1 WHERE `wp_term_taxonomy`.`term_taxonomy_id` = " + str(taxo_data[0][0])
			cursor.execute(update_taxo)

			insert_relationship = "INSERT INTO `wp_term_relationships` (`object_id`, `term_taxonomy_id`, `term_order`) VALUES ('" + str(post_id) + "', '" + str(taxo_data[1][0]) + "', '0')"
			cursor.execute(insert_relationship)
			update_taxo = "UPDATE `wp_term_taxonomy` SET `count` = `count`+1 WHERE `wp_term_taxonomy`.`term_taxonomy_id` = " + str(taxo_data[1][0])
			cursor.execute(update_taxo)


			db.commit()
			global ii
			tip = "\tsucceed catch post" + str(title) + " this is the"+ str(ii) + "post"
			print(tip)
			print("\thttps://www.idealli.com/archives/" + str(post_id))
			ii = ii + 1
		except Exception as e:
			db.rollback()
			print(e)
	else:
		global it
		print(u"\tThe post already exit! times" + str(it))
		it = it + 1
		return 0
	return 1

#################################################
# 		链接获取，爬虫部分
#################################################

def get_post(lin, tag_idd):
	link = lin
	requests.adapters.DEFAULT_RETRIES = 5
	
	try:
		req = requests.get(url = link)
		bf = BeautifulSoup(req.text,"html.parser")
		
		req.close

		texts = bf.find('div',class_='content-detail markdown-body')
		origin = u"<p>来源：<a target=_blank href="
		origin = origin.encode('utf-8')
		texts = "<meta name=\"referrer\" content=\"never\">" + str(texts).replace("data-src=\"","src=\"https://segmentfault.com") + origin + str(link) +" rel=noopener>" + str(link) + "</a></p>"
		
		title = bf.find('h2',class_='blog-title').text
		title = title.replace(' ','')
		title = title.replace('\n','')
		tim = bf.find('span',class_='b-time icon-shijian1').text

		author = bf.find(name='a', class_='b-author').text
		summary = bf.find('p',class_='blog-summary')
		#tag = bf.find('a',class_='tag').get('data-original-title')
	
	
		
		#time.sleep(1.5)
	except Exception as e:
		print(e)
		print("\t######################\n\n\terror!\n\n\t#######################")
		time.sleep(3)
		# get_url(nextlink)
	if u'阿里云' in title:
		return
	insert_post(title,author,texts,tag_idd, tim,str(summary),db)



def get_url(begin):
	# global tar
	# global urls
	# global ourls
	requests.adapters.DEFAULT_RETRIES = 5
	try:
		req = requests.get(url = begin)
		bf = BeautifulSoup(req.text,"html.parser")
		
		req.close
		tag_box = bf.find('div',class_='yq-all-tags')
		tags = tag_box.find_all('a')

		for x in tags:
			# temp.href = 'https://segmentfault.com' + x.get('href')  + '/blogs?page='
			tar.append({'tagid':x.get('href').replace('/tags/tagid_','').replace('/',''),'tag':x.text})
			# tag_name.append(x.text)
	except:
		print("error")

	global cur_page_num
	global cur_tag_num
	global last_post_id
	for y in tar[cur_tag_num:]:
		cur_page_num = 0
		ts = 'https://yq.aliyun.com/tags/type_blog-tagid_' + y.get('tagid') + '-page_'
		tag = y.get('tag')

		tag_idd = tag_id(tag)
		cursor = db.cursor()
		cursor.execute("SELECT MAX(`ID`) FROM `wp_posts`")
		lpi = cursor.fetchone()
		last_post_id = int(lpi[0])
		# continue

		print('\n\t*************************\n')
		print('\t new tag!!! there is ' + ts)
		print('\n\t*************************\n')
		old_page = 0

		for temp in xrange(1,1000):
			cur_page_num = cur_page_num + 1
			new_urls = ts + str(temp)
			
			print('\n\tnew page ! ' + new_urls)
			new_req = requests.get(url = new_urls)
			nbf = BeautifulSoup(new_req.text,"html.parser")
			h = nbf.find('section',class_='yq-new-list yq-n-l-tags')
			hh = h.find_all(name = 'h3')
			if len(hh) < 2:
				print('\t\n\nthe last page!\n\n')
				break
			old_urls = 0
			for hhh in hh:
				hhhh = hhh.find(name = 'a')
				if hhhh != None:
					hhhh = str(hhhh.get('href'))
					if	get_post('https://yq.aliyun.com/' + hhhh, tag) == 0:
						print('\tnext!')
						old_urls = old_urls +1
					if old_urls > 1:
						old_page = old_page +1
						break
						
			# if old_page > 5:
			# 	break
		cur_tag_num = cur_tag_num + 1

def come_on():
	global cur_tag_num
	try:
		get_url('https://yq.aliyun.com/tags')
	except:
		if(cur_tag_num > 80):
			return
		else:
			if cur_page_num > 500:
				cur_tag_num = cur_tag_num + 1
				come_on()
			else: 
				come_on()


if __name__ == '__main__':

	print("\tbegin catch aliyun all post！\n")
	come_on()

db.close()

