# -*- coding: utf-8 -*-
# 端口扫描WEB主程序API入口
# Author:Bing
# Contact:amazing_bing@outlook.com
# Date:2016.12.1

import tornado.ioloop
import tornado.web
from tornado.web import HTTPError
from conf.globals import allowip
from core.portscan_model import *

def blocks(func):
    def decorator(self,*args,**kwargs):
        remote_ip = self.request.remote_ip
        if str(remote_ip) in allowip:
            return func(self,*args, **kwargs)
        else:
            raise HTTPError(403)
    return decorator

class MainHandler(tornado.web.RequestHandler):
    @blocks
    def get(self):
        self.current_user = "hello!welcome to this portscan api index"
        name = tornado.escape.xhtml_escape(self.current_user)#tornado.escape.json_encode(self.current_user)
        self.write(name)


class ListHandler(tornado.web.RequestHandler):
    @blocks
    def get(self):
        data = {}
        try:
            result = select_list()
            respon_json = tornado.escape.json_encode(result)
            self.write(respon_json)
        except Exception, e:
            respon_json = tornado.escape.json_encode({'status':-1})
            self.write(respon_json)


class AddHandler(tornado.web.RequestHandler):
    @blocks
    def post(self):
        data ={} 
        try:
            current_ip = self.get_body_arguments('ip')
            scan_list = current_ip[0].encode("gbk").split(",")
            task_id = CreateHashId()
            print scan_list,task_id
            for ip in scan_list:
                resport_id = ScanId()
                result = insert_taskid(taskid = task_id,host = ip,status = 0,resportid = resport_id)
                que.lpush('taskid',[str(ip),resport_id])
                if result == 0:
                    respon_json = tornado.escape.json_encode({'status':-5})
                    self.write(respon_json)
            respon_json = tornado.escape.json_encode({'status':1,'taskid':task_id})    
            self.write(respon_json) 
        except Exception, e:
            respon_json = tornado.escape.json_encode({'status':-1})
            self.write(respon_json)

class RepHandler(tornado.web.RequestHandler):
    @blocks
    def get(self):
        data ={} 
        try:
            current_ip = self.get_argument('taskid').encode("gbk")
            result = select_report(taskid= current_ip)
            if result == 0:
                respon_json = tornado.escape.json_encode({'status':-5})
                self.write(respon_json)
            respon_json = tornado.escape.json_encode(result)    
            self.write(respon_json)
        except Exception, e:
            respon_json = tornado.escape.json_encode({'status':-1})
            self.write(respon_json)

class DelHandler(tornado.web.RequestHandler):
    @blocks
    def get(self):
        data ={} 
        try:
            current_ip = self.get_argument('taskid').encode("gbk")
            result = delete_report(taskid= current_ip)
            if result == 0:
                respon_json = tornado.escape.json_encode({'status':-5})
                self.write(respon_json)
            respon_json = tornado.escape.json_encode(result)    
            self.write(respon_json)
        except Exception, e:
            respon_json = tornado.escape.json_encode({'status':-1})
            self.write(respon_json)


settings = dict(
            # template_path=TEMPLATE_PATH,
            # static_path=STATIC_PATH,
            # cookie_secret=str(uuid.uuid1()),
            #cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            #login_url="/login",
            # gzip=True,
            # xheaders=True,
            # 'xsrf_cookies': True,          # 防止跨站伪造
            # 'ui_methods': mt,              # 自定义UIMethod函数
            # 'ui_modules': md,              # 自定义UIModule类
            debug=True
        )

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/list", ListHandler),
    (r"/add", AddHandler),
    (r"/report", RepHandler),
    (r"/del", DelHandler)
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()

'''
    def post(self,*args,**kwargs):
        #user = self.get_body_argument('user')  #删除ip
        result = {"status":"1"}
        respon_json = tornado.escape.json_encode(result)    
        self.write(respon_json)  
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()

'''