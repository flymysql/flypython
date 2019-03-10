#pytest
#coding=utf-8
#!/usr/bin/python
import pymysql
import time
from bs4 import BeautifulSoup
import requests,sys
import datetime
import re

db = pymysql.connect("localhost","root","your passwd","www_idealli_com",charset='utf8')
tags = ['python','Android','Javascript','Java','Vue.js']
cur_tag = ''
urls = []
tar = []
link_head = "https://juejin.im"
otar = []
ourls = []
ii = 0
it = 0

def insert_post(ti,au,con,ta,tim,db):
	title = ti.encode('utf-8')
	author = au.encode('utf-8')
	content = con
	content = content.replace("'","`")
	tag = ta.encode('utf-8')
	time = tim.encode('utf-8')
	cursor = db.cursor()
	# check repeat post
	check_title="SELECT `ID` FROM `wp_posts` WHERE `post_title` = '" + title + "'"
	cursor.execute(check_title)
	data = cursor.fetchone()
	if data is None:

		# check tag
		check_tag = "SELECT `term_id` FROM `wp_terms` WHERE `name` = '" + tag + "'"
		cursor.execute(check_tag)
		tag_id = cursor.fetchone()
		tag_data = cursor.fetchall()
		if tag_id is None:
			try:	
				insert_tag = "INSERT INTO `wp_terms` (`term_id`, `name`, `slug`, `term_group`) VALUES (NULL, '"+ tag +"','" + tag + "', '0')"
				cursor.execute(insert_tag)
				cursor.execute(insert_tag)


				check_tag = "SELECT `term_id` FROM `wp_terms` WHERE `name` = '" + tag + "'"
				cursor.execute(check_tag)
				tag_data = cursor.fetchall()
				insert_taxonomy_tag = "INSERT INTO `wp_term_taxonomy` (`term_taxonomy_id`, `term_id`, `taxonomy`, `description`, `parent`, `count`) VALUES (NULL, '" + str(tag_data[0][0]) + "', 'post_tag', '', '0', '1')"
				insert_taxonomy_category = "INSERT INTO `wp_term_taxonomy` (`term_taxonomy_id`, `term_id`, `taxonomy`, `description`, `parent`, `count`) VALUES (NULL, '" + str(tag_data[1][0]) + "', 'category', '', '0', '1')"

				cursor.execute(insert_taxonomy_tag)
				cursor.execute(insert_taxonomy_category)
				db.commit()
			except:
				db.rollback()



		# check author
		check_author = "SELECT `ID` FROM `wp_users` WHERE `display_name` LIKE '" + author + "'"
		cursor = db.cursor()
		cursor.execute(check_author)
		author_id = cursor.fetchone()
		if author_id is None:
			insert_author = "INSERT INTO `wp_users` (`ID`, `user_login`, `user_pass`, `user_nicename`, `user_email`, `user_url`, `user_registered`, `user_activation_key`, `user_status`, `display_name`) VALUES (NULL, '', '', '', '', '', '0000-00-00 00:00:00.000000', '', '0', '" + author +"')"
			cursor = db.cursor()
			try:
				cursor.execute(insert_author)
				db.commit()
			except:
				db.rollback()
			check_author = "SELECT `ID` FROM `wp_users` WHERE `display_name` LIKE '" + author + "'"
			cursor = db.cursor()
			cursor.execute(check_author)
			author_id = cursor.fetchone()

		# creat new post

		insert_post = "INSERT INTO `wp_posts` (`ID`, `post_author`, `post_date`, `post_date_gmt`, `post_content`, `post_title`, `post_excerpt`, `post_status`, `comment_status`, `ping_status`, `post_password`, `post_name`, `to_ping`, `pinged`, `post_modified`, `post_modified_gmt`, `post_content_filtered`, `post_parent`, `guid`, `menu_order`, `post_type`, `post_mime_type`, `comment_count`) VALUES (NULL, '" + str(author_id[0]) + "', '" + str(time) + "', '" + str(time) + "', '" + str(content) + "', '" + str(title) + "', '', 'publish', 'open', 'open', '', '', '', '', '" + str(time) + "', '" + str(time) + "', '', '0', '', '0', 'post', '', '0')"
		try:

			try:
				cursor.execute(insert_post)
			except Exception as e:
				print(e)

			# check tag
			check_tag = "SELECT `term_id` FROM `wp_terms` WHERE `name` = '" + tag + "'"

			cursor.execute(check_title)
			post_id = cursor.fetchone()
			cursor.execute(check_tag)
			tag_data = cursor.fetchall()
			#print(tag_data)
			check_taxo = "SELECT `term_taxonomy_id` FROM `wp_term_taxonomy` WHERE `term_id` = '" + str(tag_data[0][0]) + "'"
			try:
				cursor.execute(check_taxo)

			except Exception as e:
				print(e)
			#print(cursor.fetchall())
			taxo_data = cursor.fetchone()

			insert_relationship = "INSERT INTO `www_idealli_com`.`wp_term_relationships` (`object_id`, `term_taxonomy_id`, `term_order`) VALUES ('" + str(post_id[0]) + "', '" + str(taxo_data[0]) + "', '0')"

			try:
				cursor.execute(insert_relationship)
			except Exception as e:
				print(e)
			update_taxo = "UPDATE `www_idealli_com`.`wp_term_taxonomy` SET `count` = `count`+1 WHERE `wp_term_taxonomy`.`term_taxonomy_id` = " + str(taxo_data[0])
			try:
				cursor.execute(update_taxo)
			except Exception as e:
				print(e)


			check_taxo = "SELECT `term_taxonomy_id` FROM `wp_term_taxonomy` WHERE `term_id` = '" + str(tag_data[1][0]) + "'"
			try:
				cursor.execute(check_taxo)
				#print(cursor.fetchall())
			except Exception as e:
				print(e)
			taxo_data = cursor.fetchone()
			insert_relationship = "INSERT INTO `www_idealli_com`.`wp_term_relationships` (`object_id`, `term_taxonomy_id`, `term_order`) VALUES ('" + str(post_id[0]) + "', '" + str(taxo_data[0]) + "', '0')"
			try:
				cursor.execute(insert_relationship)
			except Exception as e:
				print(e)

			update_taxo = "UPDATE `www_idealli_com`.`wp_term_taxonomy` SET `count` = `count`+1 WHERE `wp_term_taxonomy`.`term_taxonomy_id` = " + str(taxo_data[0])
			try:
				cursor.execute(update_taxo)
			except Exception as e:
				print(e)

			db.commit()
			global ii
			tip = "\tsucceed catch post" + str(title) + " this is the"+ str(ii) + "post"
			print(tip)
			ii = ii + 1
		except:
			db.rollback()
			print("\tinsert error!")
	else:
		global it
		print(u"\tThe post already exit! times" + str(it))
		it = it + 1

def get_post(lin):
	link = lin
	requests.adapters.DEFAULT_RETRIES = 5
	s = requests.session()
	
	s.keep_alive = False
	try:
		req = s.get(url = link)
		bf = BeautifulSoup(req.text,"html.parser")
		s.close
		req.close

		texts = bf.find_all('div',class_='article-content')[0]
		origin = u"<p>来源：<a target=_blank href="
		origin = origin.encode('utf-8')
		texts = str(texts) + origin + str(link) +" rel=noopener>" + str(link) + "</a></p>"
		title = bf.find_all('h1',class_='article-title')[0].text
		tim = bf.find_all('time',class_='time')[0]['datetime']
		tim = tim.replace('T',' ')
		tim = tim.replace('Z','')

		author = bf.find_all('meta',itemprop='name')[0]['content']
		tag = bf.find_all('div',class_='tag-title')[0].text
	except:
		print("\t######################\n\n\terror!\n\n\t#######################")
		nextlink = tar.pop()
		time.sleep(1)
		get_url(nextlink)

	global urls
	global tar
	print('\t' + title)
	insert_post(title,author,texts,tag,tim,db)
	time.sleep(1)
	
	# for link  in bf.find_all(name='a',class_='avatar-link'):
	#  	if link != None:
	#  		newp = link_head + link.get('href')
	#  		if newp in otar:
	#  			pass
	#  		else:
	#  			tar.append(newp)
	# 			otar.append(newp)

	if len(urls)!=0:
		
		get_post(urls.pop())



	#insert_post(title,author,texts,tag,time,db)


def get_url(begin):
	global tar
	global urls
	global ourls
	print("\tnow find url " + begin )
	if len(urls)!=0:
		get_post(urls.pop())
	
	requests.adapters.DEFAULT_RETRIES = 5
	s = requests.session()
	s.keep_alive = False
	try:
		req = s.get(url = begin)
		bf = BeautifulSoup(req.text,"html.parser")
		s.close
		req.close

		for link  in bf.find_all(name='a'):
			if link.get('href')!= None:
				#print type(link)
				cur = str(link.get('href'))
				if 'https://juejin.im/post/' in cur:
					urls.append(link_head + cur)
					ourls.append(link_head + cur)
				elif '/post/' in cur:
					if (link_head + cur) in ourls:
						pass
					else:
						if 'http' in cur:
							pass
						elif '#' in cur:
							pass
						else:
							urls.append(link_head + cur)
							ourls.append(link_head + cur)
				
				if link_head + cur in otar:
					pass
				else:
					if link_head in cur:
						tar.append(cur)
						otar.append(cur)
					elif '/tag/' in cur:
						tar.append(link_head + cur)
						otar.append(link_head + cur)
					elif '/welcome/' in cur:
						otar.append(link_head + cur)
						tar.append(link_head + cur)
					elif '/user/' in cur:
						otar.append(link_head + cur)
						tar.append(link_head + cur)
	except:
		nextlink = tar.pop()
		print("\t######################\n\n\terror!\n\n\t#######################")
		time.sleep(1)
		get_url(nextlink)

	print("\tthe number of links is" + str(len(urls)))
	print("\tthe number of target is" + str(len(tar)))
	
	#print(urls)
	if len(tar) > 0:
		nextlink = tar.pop()
		time.sleep(1)
		get_url(nextlink)
	


	# global urls
	# urls = []
	# for tag in tags:
	# 	for x in xrange(1,5000):
	# 		target = "https://so.csdn.net/so/search/s.do?p=" + str(x) + "&q=" + tag
	# 		print(target)
	# 		req = requests.get(url = target)
	# 		bf = BeautifulSoup(req.text,"html.parser")
	# 		post_links = bf.find_all('a')
			
	# 		for ls in post_links:
	# 			if '/article/details' in ls['href']:
	# 				if ls['href'] in urls:
	# 					pass
	# 				else:
	# 					urls.append(ls['href'])
	# 					get_post(ls['href'],tag)
	# 		urls = []


if __name__ == '__main__':
	print("\tbegin catch CSDN all post！\n")
	get_url('https://juejin.im/user/5c3edfbf6fb9a049e82bca89')

db.close()

