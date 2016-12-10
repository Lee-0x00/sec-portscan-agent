# -*- coding: utf-8 -*-
# 创建数据表
# Author:Bing
# Contact:amazing_bing@outlook.com
# Date:2016.12.1

import torndb,time 

db = torndb.Connection(host = mysql_config,database= mysql_db, user = mysql_user, password = mysql_passwd)

sql='CREATE TABLE report(ID integer PRIMARY KEY NOT NULL AUTO_INCREMENT,REPORTID CHAR(32) NOT NULL,SERVICE TEXT NOT NULL,PORT INT NOT NULL);'
result = db.execute(sql)
print result

sql='CREATE TABLE task(ID integer PRIMARY KEY NOT NULL AUTO_INCREMENT,TASKVAL TEXT NOT NULL,TASKSTATUS INT NOT NULL,TASKID CHAR(32) NOT NULL,REPORTID CHAR(32) NOT NULL);'
result = db.execute(sql)
print result

sql='CREATE TABLE finger(ID integer PRIMARY KEY NOT NULL AUTO_INCREMENT,SERVICE TEXT NOT NULL,PORT INT NOT NULL);'
result = db.execute(sql)
print result

