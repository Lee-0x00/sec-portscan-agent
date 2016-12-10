# -*- coding: utf-8 -*-
# 数据操作模块
# Author:Bing
# Contact:amazing_bing@outlook.com
# Date:2016.12.1

import sys
sys.path.append("..")
import torndb,time 
from conf.globals import *
import redis

pool = redis.ConnectionPool(host = redis_host,port = redis_port,db = redis_db,password = redis_passwd)  
que = redis.Redis(connection_pool = pool)

db = torndb.Connection(host = mysql_config,database= mysql_db, user = mysql_user, password = mysql_passwd)

def select_list():
	sql='select task.TASKID,task.TASKVAL,report.SERVICE,report.PORT,task.TASKSTATUS FROM task,report'
	result = db.query(sql)
	return result

def insert_taskid(taskid='',host='',status='',resportid = ''):
	sql = "INSERT INTO task (TASKID,TASKVAL,TASKSTATUS,REPORTID) VALUES (%s,%s,%s,%s)"
	result = db.execute_rowcount(sql,taskid,host,status,resportid)
	return result

def insert_result(scanid='',service='',port=''):
	#FROM tb_demo065  a,tb_demo065_tel  b WHERE a.id=b.id AND b.id='$_POST[textid]'
	sql = "INSERT INTO report (REPORTID,SERVICE,PORT) VALUES (%s,%s,%s)"
	result = db.execute_rowcount(sql,scanid,service,port)
	return result

def select_report(taskid=''):
	#select * from T1 inner join T2 on T1.userid = T2.userid
	sql = "select task.TASKID,task.TASKVAL,report.SERVICE,report.PORT,task.TASKSTATUS FROM task inner join report on task.REPORTID=report.REPORTID where task.TASKID=%s"
	result = db.query(sql,taskid)
	return result

def delete_report(taskid=''):
	sql = "DELETE task,report from task LEFT JOIN report ON task.TASKID=report.REPORTID WHERE task.TASKID = %s"
	result = db.execute_rowcount(sql,taskid)
	return result

def select_task():
	sql = "select * from task where TASKSTATUS =0 "
	result = db.query(sql)
	return result

def modify_task_status(resportid = '',status=''):
	sql = "UPDATE task SET TASKSTATUS=%s WHERE REPORTID=%s"
	result = db.execute_rowcount(sql,status,resportid)
	return result


def port_service(port=''):
	sql = "select * from finger where port=%s"
	result = db.query(sql,port)
	return result



'''

por='CREATE TABLE report(ID integer PRIMARY KEY NOT NULL AUTO_INCREMENT,REPORTID CHAR(32) NOT NULL,SERVICE TEXT NOT NULL,PORT INT NOT NULL);'
result = db.execute(sql)
print result

sql='CREATE TABLE task(ID integer PRIMARY KEY NOT NULL AUTO_INCREMENT,TASKVAL TEXT NOT NULL,TASKSTATUS INT NOT NULL,TASKID CHAR(32) NOT NULL,REPORTID CHAR(32) NOT NULL);'
result = db.execute(sql)
print result

sql='CREATE TABLE finger(ID integer PRIMARY KEY NOT NULL AUTO_INCREMENT,SERVICE TEXT NOT NULL,PORT INT NOT NULL);'
result = db.execute(sql)
print result

'''













