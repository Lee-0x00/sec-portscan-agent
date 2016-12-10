# -*- coding: utf-8 -*-
# 多线程端口扫描主程序
# Author:Bing
# Contact:amazing_bing@outlook.com
# Date:2016.11.14

import threading, socket, sys, os, Queue

class ScannerThread(threading.Thread):
    def __init__(self, inq, outq):
        threading.Thread.__init__(self)
        # queues for (host, port)
        self.setDaemon(True)        #主程序等待任务队列
        self.inq = inq                #扫描队列
        self.outq = outq            #结果队列
        self.killed = False
        self.timeout = 0.5

    def run(self):
        while not self.killed:
            host, port = self.inq.get()
            #print threading.currentThread(),host
            sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sd.settimeout(self.timeout)
            try:
                # connect to the given host:port
                sd.connect((host, port))
                self.outq.put((host, port, 'OPENED'))
            except socket.error:
                # set the CLOSED flag
                self.outq.put((host, port, 'CLOSED'))             
            sd.close()


class Scanner:
    def __init__(self, from_port, to_port, host='localhost'):
        self.from_port = from_port
        self.to_port = to_port
        self.host = host
        self.scanners = []

    def scan(self, search_for='opened',first_match=False, nthreads=1,send_fn=None, exclude=[]):
        self.resp = []
        #生成任务队列
        toscan = Queue.Queue()
        scanned = Queue.Queue()
        #生成扫描线程
        self.scanners = [ScannerThread(toscan, scanned) for i in range(nthreads)]
        #print self.scanners
        #线程准备开始
        for scanner in self.scanners:
            scanner.start()
        #把端口和主机压入队列，exclude黑名单
        hostports = [(self.host, port) for port in xrange(self.from_port, self.to_port+1) if port not in exclude]
        #print hostports
        for hostport in hostports:
            toscan.put(hostport)

        results = {}
        for host, port in hostports:
            while (host, port) not in results:
                nhost, nport, nstatus = scanned.get()        #获取结果队列的值
                results[(nhost, nport)] = nstatus
            status = results[(host, port)]
            progress = ('%.2f' % (float(port)/float(65530)))
            value = (host, port, status,progress)
            #print value
            if status == 'OPENED' and search_for.lower() == 'opened' or port == 65530:
                if send_fn:
                    send_fn(value)
                if first_match:
                    return self._finish_scan()
            elif status == 'CLOSED' and search_for.lower() == 'closed':
                if send_fn:
                    send_fn(value)
                if first_match:
                    return self._finish_scan()
            elif search_for.lower() == 'all':
                if send_fn:
                    send_fn(value)
                if first_match:
                    return self._finish_scan()
        return self._finish_scan()

    #杀死线程
    def _finish_scan(self):
        for scanner in self.scanners:
            scanner.join(0.001)
            scanner.killed = True
        return self.resp


