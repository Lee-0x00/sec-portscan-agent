## oss-security-portscan-v2
---
##### Introduce
本程序基于python开发,采用tornado和redis做的分布式多任务，高并发的端口扫描agent，默认扫描1-65530端口；
portscan_web采用tornado做web框架，简单易操作，利用装饰器做访问限制
redis做消息中间件，实现分布式操作；
utils里面的为端口扫描主程序，利用多线程加队列实现高并发端口扫描
portscan_laucher任务执行主程序，从redis池中接受任务执行；
portscan_main端口终端运行程序


##### Install
1.创建一个数据库
2.修改conf中的globals全局配置文件
3.修改db_create中的数据库连接参数
执行以下：
pip install -r requeirements.txt 	安装模块包
python db_create.py 				创建数据库表，字段

4.利用navicat把conf中的port.txt指纹导入到finger表

##### Features
功能块包括：
:---:|:----:|:---:|:---:
list	|	列出所有的任务的扫描端口
add		|	增加任务进行端口扫描
report	|	根据taskid任务查询
del 	|	根据taskid删除任务


##### Usage
how to use this???
```
web运行：
python portscan_web.py
cd core
python portscan_launcher.py
```
![portscan_web]()


终端运行:
```
python portscan_main.py -h
```

##### Issue
如有bug，欢迎提交。。。。。。。。。


#### todo
下一版本：
1.设置守护进程
2.添加第二次任务，无需等待



