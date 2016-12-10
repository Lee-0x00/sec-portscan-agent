# -*- coding: utf-8 -*-
# 执行程序
# Author:Bing
# Contact:amazing_bing@outlook.com
# Date:2016.12.1

import sys,Queue
sys.path.append("..")
import json,random,time
from utils.port import Scanner
from gevent import monkey; monkey.patch_all()
import gevent
from core.portscan_model import *

def save(scanid,x):
	service = 'no finger'
	try:
		service = port_service(int(x[1]))[0]["SERVICE"]
	except:  
	    pass
	if str(x[2]) == "OPENED":
		insert_result(scanid=str(scanid),service=str(service),port=int(x[1]))
	if float(x[3]) == float(1) :
		modify_task_status(resportid = str(scanid),status=1)
	#print str(scanid),str(x[0]),x[1],x[2],x[3],service


def launcher(scanid,key):
    callback = lambda x: save(scanid,x)
    scanner = Scanner(from_port=1, to_port=65530,host=str(key))
    scanner.scan(search_for='opened',first_match=False, nthreads=100, send_fn=callback)


def redis_start():
    try:
        results = []
        while True:
            result = eval(str(que.lpop('taskid')))
            if result != None:
                results.append(gevent.spawn(launcher, str(result[1]),str(result[0])))
                modify_task_status(resportid = str(result[1]),status=2)
                print result
            else:
                break
        gevent.joinall(results)
    except:
        pass



def deamon():
    while True:
        redis_start()

deamon()

