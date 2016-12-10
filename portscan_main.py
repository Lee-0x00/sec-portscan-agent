# -*- coding: utf-8 -*-
# 端口扫描WEB主程序API入口
# Author:Bing
# Contact:amazing_bing@outlook.com
# Date:2016.12.1

from utils.port import Scanner
from optparse import OptionParser
import re
from gevent import monkey; monkey.patch_all()
import gevent

version = 'V2.0'
author = 'Bingli'

reip = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
def save(ip):
	print ip[0],ip[1],ip[2]


def start(text):
	if reip.match(text):
		res = reip.findall(text)
		result = "".join(res)
		callback = lambda ip: save(ip)
		scanner = Scanner(from_port=1, to_port=30000,host=result)
		scanner.scan(search_for='opened',first_match=False, nthreads=100, send_fn=callback)
	else:
		pass

def run(text):
    try:
        result = text.split("/")
        if int(result[1]) == 24 :
            for i in range(1,255):
                ip = result[0].split('.')[0]+'.'+result[0].split('.')[1]+'.'+result[0].split('.')[2]+'.'+str(i)
                start(ip)
    except:
        start(text)

if __name__ == '__main__':
	usage = """
     _______.  ______     ___      .__   __. 
    /       | /      |   /   \     |  \ |  | 
   |   (----`|  ,----'  /  ^  \    |   \|  | 
    \   \    |  |      /  /_\  \   |  . `  | 
.----)   |   |  `----./  _____  \  |  |\   | 
|_______/     \______/__/     \__\ |__| \__|

	Author: %s && Ver: %s
	""" % (author,version)
	print usage
	parser = OptionParser()
	parser.add_option("-u", "--target", dest="target", default='', help="set ip/ip-list.(simple: 127.0.0.1 or 10.10.12.3/24)")

	(options, args) = parser.parse_args()
	run(options.target)




