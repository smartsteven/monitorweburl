#!/usr/bin/env python
#coding:utf-8
 #更改返回的编码格式


import time
import requests

 #修改系统默认编码格式
 #reload(sys)
 #sys.setdefaultencoding('utf-8')

 #读取URLlist文本文件
f = open("URLLIST.txt", "r")
 #output = open("monitorurl.log","a+")
urlList = f.readlines()

def MonitorUrlList():
    i = int(1)
    for url in urlList:
    #print url

        r = requests.get(url)
        sta = str(r.status_code)
        #print date.fromtimestamp(time.time())
        t = str(time.ctime())

        print i,t,url,sta
        with open('monitorurl.log', 'a')as output:
            #output.write("time:" +t+ "url:" +url+ "status:" +sta+'\n')
            output.write( '\n'+ "(" +str(i) + ")" +"time:(" + t + ") url:" + url + "status:" + sta )
            output.close()
        i =int(i + 1)

f.close()

if __name__ == '__main__':

    MonitorUrlList()


#requests的请求方法:get
#r = requests.get(url)




#查看响应码
#print r.status_code
#status = r.status_code

#保存返回的结果
#fh = open("monitorurl.log", 'w')
#fh.write(r.content)
#fh.write(status)
#fh.close()
