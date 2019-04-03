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
import json
import urllib
import urllib2
import types 

# 连接数据库需要，IP，user，密码，库名
db = pymysql.connect(host='localhost', user="root", passwd='your passwd', db='www_idealli_com')
ads = "<hr><p>阿里云云翼计划的学生机做出重大调整，所有实名认证<strong>只要在12岁到24岁之间的可以自动获取学生认证身份</strong>，和实名认证的在校大学生一样可以选择1核2G内存的云服务器或者轻量应用服务器，而且都是100%CPU性能！建个站什么的毫无压力。</p><hr>"
ads = ads + "<ol><li><p>注册领取阿里云服务器ECS幸运券(新用户优惠)：<a href=https://promotion.aliyun.com/ntms/yunparter/invite.html?userCode=rftv1tas target=_blank rel=noopener>点击领取</a></p></li><li><p>完成学生认证：<a href=https://account.console.aliyun.com/?spm=5176.7189909.0.0.SYBKvh#/student/home target=_blank rel=noopener>点击进入</a></p></li><li><p>学生专属优惠云服务器购买地址(购买之前领券，更优惠！)：<a href=https://promotion.aliyun.com/ntms/act/campus2018.html?userCode=rftv1tas target=_blank rel=noopener>点击进入</a><br></p></li></ol><hr>"
ads2 = "<p><strong>小推荐：</strong>VULTR刚出的新用户优惠活动，注册并充值10美元送50美元，没有VULTR账户的朋友可以去注册一个，此优惠活动为新用户专属。开一台服务器可以用1年多！<br><strong>活动地址：</strong><a target=_blank href=https://www.vultr.com/?ref=7772625-4F>点击注册领取</a></p><hr>"
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
cur_tag_num = 2
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
			print(tag_name)
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
	if len(taxo_data) == 0:
		insert_taxonomy_tag = "INSERT INTO `wp_term_taxonomy` (`term_taxonomy_id`, `term_id`, `taxonomy`, `description`, `parent`, `count`) VALUES (NULL, '" + str(tag_data[0][0]) + "', 'post_tag', '', '0', '1')"
		insert_taxonomy_category = "INSERT INTO `wp_term_taxonomy` (`term_taxonomy_id`, `term_id`, `taxonomy`, `description`, `parent`, `count`) VALUES (NULL, '" + str(tag_data[1][0]) + "', 'category', '', '0', '1')"

		cursor.execute(insert_taxonomy_tag)
		cursor.execute(insert_taxonomy_category)
		db.commit()
		cursor.execute(check_taxo)
		#print(cursor.fetchall())
		taxo_data = cursor.fetchall()
	return taxo_data


def insert_post(ti,au,con,tag_idd, tim,db):
	title = ti.encode('utf-8')
	cursor = db.cursor()
	check_title = "select ID from wp_posts where ID>263100 and post_title='" + title + "';"
	cursor.execute(check_title)
	have_exit = cursor.fetchone()
	if have_exit is None:
		pass
	else:
		return 0
	
	author = au.encode('utf-8')
	global last_post_id
	global check_title_time
	last_post_id = int(last_post_id) +1
	content = con
	content = content.replace("'","`")
	time = tim
	
	taxo_data = tag_idd
	post_id = last_post_id
	try:
		# check author
		check_author = "SELECT `ID` FROM `wp_users` WHERE `display_name` LIKE '" + author + "'"
		cursor = db.cursor()
		cursor.execute(check_author)
		author_id = cursor.fetchone()
		
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

		# creat new post
		post_id = str(last_post_id)
		
		insert_post = "INSERT INTO `wp_posts` (`ID`, `post_author`, `post_date`, `post_date_gmt`, `post_content`, `post_title`, `post_excerpt`, `post_status`, `comment_status`, `ping_status`, `post_password`, `post_name`, `to_ping`, `pinged`, `post_modified`, `post_modified_gmt`, `post_content_filtered`, `post_parent`, `guid`, `menu_order`, `post_type`, `post_mime_type`, `comment_count`) VALUES (" + post_id + ", '" + str(author_id[0]) + "', '" + str(time) + "', '" + str(time) + "', '" + str(content) + "', '" + str(title) + "', '', 'publish', 'open', 'open', '', '', '', '', '" + str(time) + "', '" + str(time) + "', '', '0', '', '0', 'post', '', '0')"
		
		try:

			cursor.execute(insert_post)
			insert_relationship = "INSERT INTO `wp_term_relationships` (`object_id`, `term_taxonomy_id`, `term_order`) VALUES ('" + post_id + "', '" + str(taxo_data[0][0]) + "', '0')"
			cursor.execute(insert_relationship)
			update_taxo = "UPDATE `wp_term_taxonomy` SET `count` = `count`+1 WHERE `wp_term_taxonomy`.`term_taxonomy_id` = " + str(taxo_data[0][0])
			cursor.execute(update_taxo)

			insert_relationship = "INSERT INTO `wp_term_relationships` (`object_id`, `term_taxonomy_id`, `term_order`) VALUES ('" + post_id + "', '" + str(taxo_data[1][0]) + "', '0')"
			cursor.execute(insert_relationship)
			update_taxo = "UPDATE `wp_term_taxonomy` SET `count` = `count`+1 WHERE `wp_term_taxonomy`.`term_taxonomy_id` = " + str(taxo_data[1][0])
			cursor.execute(update_taxo)

			db.commit()
			global ii
			tip = "\tsucceed catch post" + str(title) + "\n\t this is the"+ str(ii) + "post and tag " + str(cur_tag_num)
			print(tip)
			print("\thttps://flycode.co/archives/" + str(post_id))
			ii = ii + 1
			return 1
		except Exception as e:
			db.rollback()
			print(e)
			return 0
	except Exception as e:
		db.rollback()
		print(e)
		return 0


#################################################
# 		链接获取，爬虫部分
#################################################

def get_post(lin, tim , tag_idd):
	link = lin
	requests.adapters.DEFAULT_RETRIES = 5
	global ads
	global ads2
	try:
		print('\n\ttry to get post ' + link)
		req = requests.get(url = link,timeout=10)
		bf = BeautifulSoup(req.text,"html.parser")
		req.close
		
		texts = bf.find('div',class_='article-content')
		if texts is None:
			print(lin)
			return
		author = bf.find_all('meta',itemprop='name')[0]['content']
		title = bf.find_all('h1',class_='article-title')[0].text
		origin = u"<p>来源：<a target=_blank href="
		origin = origin.encode('utf-8')
		texts = "<meta name=\"referrer\" content=\"never\">" + ads2 + str(texts).replace('data-src=','src=') + ads + origin + str(link) +" rel=noopener>" + str(link) + "</a></p>"
		#tag = bf.find('a',class_='tag').get('data-original-title')
		#time.sleep(1.5)
	except Exception as e:
		print(e)
		print("\t######################\n\n\terror!\n\n\t#######################")
		time.sleep(3)
		# get_url(nextlink)
	try:
		if insert_post(title, author,texts, tag_idd,tim , db) == 0:
			print('\t post ' + title + ' have exit !!!')
			return 0
		else: 
			return 1
	except:
		return 0



def get_url(begin):
	# global tar
	# global urls
	# global ourls
	requests.adapters.DEFAULT_RETRIES = 5
	tags = []
	try:
		req = requests.get(url=begin,timeout=10)
		bf=BeautifulSoup(req.text,"html.parser")
		box = bf.find_all('div',class_='tag')
		
		for x in box:
			tagid = x.get('id')
			tag_name = x.find('div',class_='title').text.replace(' ','_')
			tags.append({'tag':tag_name,'tagid':tagid})
	except Exception as e:
		print(e)
	global last_post_id
	global urls
	global cur_tag_num
	ctn = cur_tag_num

	for y in tags[ctn:]:
		
		try:
			cur_page_num = 0
			ts = 'https://timeline-merger-ms.juejin.im/v1/get_tag_entry?src=web&tagId=' + y.get('tagid') + '&page='
			tag = y.get('tag')
			tag_idd = tag_id(tag)
			cursor = db.cursor()
			cursor.execute("SELECT MAX(`ID`) FROM `wp_posts`")
			lpi = cursor.fetchone()
			
			last_post_id = int(lpi[0])
			# continue
			
			if len(urls) > 30000:
				urls = []
			print('\n\t*************************\n')
			print('\t new tag!!! there is ' + 'pages and the tag is ' + tag)
			print('\t ' + ts )
			print('\n\t*************************\n')
			old_page = 0
			temp = 1 
			while 1:
				try:
					cur_page_num = cur_page_num + 1
					headers = {"Charset":"UTF-8","Content-Type":"application/json"}
					request = urllib2.Request(url=ts + str(temp) + '&pageSize=100&sort=time', headers=headers)
					response = urllib2.urlopen(request)
					
					print('\n\tthere is the new links 100 *' + str(temp))
					# new_req = requests(url = ts + str(temp) + '&pageSize=100&sort=time',timeout=10,header=headers)
					datas = json.loads(response.read())['d']['entrylist']
					if datas == []:
						break
					ex = 0
					for post in datas:
						try:
							href = post.get('originalUrl')
							if 'juejin.im' in href:
								if href in urls:
									continue
								urls.append(href)
								# print(author)
								tim = post.get('updatedAt')
								tim = tim.replace('T',' ')
								tim = tim[0:19]
								if get_post(href, tim , tag_idd) == 0:
									ex = ex + 1
								else:
									ex = 0
								if ex > 5:
									break
						except:
							continue
				except:
					continue
				temp = temp + 1
				# if old_page > 5:
				# 	break
				
			cur_tag_num = cur_tag_num + 1
		except Exception as e:
			print(e)
	

def come_on():
	global cur_tag_num
	try:
		get_url('https://yq.aliyun.com/tags')
	except:
		if(cur_tag_num > 80):
			return
		else:
			cur_tag_num = cur_tag_num + 1
			come_on()


if __name__ == '__main__':

	print("\tbegin catch juejin all post！\n")
	get_url('https://image.idealli.com/test1.html')

db.close()
