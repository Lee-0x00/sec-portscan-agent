# -*- coding: utf-8 -*-
# 配置文件
# Author:Bing
# Contact:amazing_bing@outlook.com
# Date:2016.12.1

import json,random,time

#允许访问ip地址
allowip = ['127.0.0.1','x.x.x.1']


redis_host = "1.1.1.1"
redis_passwd = "******"
redis_port = 6379
redis_db = 2

mysql_config = "127.0.0.1:3306"
mysql_db = "test"
mysql_user ="root"
mysql_passwd ="123456"


def CreateHashId():
    times = time.strftime("%Y%m%d-", time.localtime())
    salt = []
    for i in range(0,6):
        salt.append(str(random.randint(0,9)))
        salts = "".join(salt)
    result = "TASKID-"+str(times)+str(salts)
    return result

def ScanId():
    times = time.strftime("%Y%m%d-", time.localtime())
    salt = []
    for i in range(0,6):
        salt.append(str(random.randint(0,9)))
        salts = "".join(salt)
    result = "SCANID-"+str(times)+str(salts)
    return result

#print CreateHashId()
