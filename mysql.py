#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

# 连接数据库需要，IP，user，密码，库名
db = pymysql.connect(host='120.77.183.14', user="root", passwd='www.l975', db='www_idealli_com')

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("DELETE FROM wp_posts WHERE ID NOT IN (SELECT col1 FROM my_tmp)")
db.commit()


# 关闭数据库连接
db.close()