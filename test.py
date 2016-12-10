from requests import post,get
import threading,gevent,subprocess

if __name__ == '__main__':
    print post(url="http://127.0.0.1:8888/add",data={"ip":"www.baidu.com,www.sina.com"}).content
    #print get("http://127.0.0.1:8888/list").content
    #print get(url="http://127.0.0.1:8888/report?taskid=TASKID-20161202-007167").content
    #print dir(get())
    print dir(threading)
    print "----------------------------------------"
    print dir(gevent)
    print "----------------------------------------"
    print dir(subprocess)





