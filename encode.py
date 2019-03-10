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


# 连接数据库需要，IP，user，密码，库名
db = pymysql.connect(host='localhost', user="root", passwd='your passwd', db='www_idealli_com')

if __name__ == '__main__':
    cursor = db.cursor()
    check = "SELECT `term_id`,`name` FROM `wp_terms` WHERE `name` = `slug`"
    cursor.execute(check)
    tag_id = cursor.fetchall()
    for x in tag_id:
        up = "UPDATE `www_idealli_com`.`wp_terms` SET `slug` = '" + urllib.quote(x[1]) + "' WHERE `wp_terms`.`term_id` = " + str(x[0])
        cursor.execute(up)
    db.commit()

db.close()