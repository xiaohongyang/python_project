import os
from urllib import *
import urllib
from urllib import  request

class Spider:

    def __init__(self, url):
        self.url = url
        self.header = {}
        self.linkList = []
    '''
    url 要下载的地址
    fileName 新建文件名
    '''
    def saveImg(self, url, fileName):

        #url = "http://s3.51cto.com/wyfs02/M01/30/03/wKioL1OiryfgvGZVAAIosMpN4lo679.jpg"

        try:
            req = urllib.request.Request(url,headers = self.header)
            html = urllib.request.urlopen(req)
            fileData = html.read()
            file = open(fileName, 'wb')
            file.write(fileData)
            file.close()
        except:
            pass

        # html = urllib.request.urlopen(url)
        # data = html.read()
        # img = open(fileName, "wb")
        # img.write(data)
        # img.close()
    def setHeader(self, header):

        self.header = header
        pass

    def setLinkList(self, linkList):
        self.linkList = linkList

    def getLinkList(self):
        return  self.linkList

    #下载文件列表到指定目录
    #saveDir 目标目录
    #suffix 文件名后缀
    #prefix 文件名前缀
    def downLinkList(self,saveDir, suffix, prefix=''):
        i = 1;
        for link in self.linkList:
            i += 1
            self.saveImg(link, saveDir + "/" + prefix +str(i)+suffix)


try:
    fileName ='22t.txt'
    url = 'http://baidu.com/'
    req = urllib.request.Request(url)
    html = urllib.request.urlopen(req)
    fileData = html.read()
    file = open(fileName, 'w+')
    data = str(fileData, 'utf-8')
    file.write(data)
    file.close()
    pass
except:
    pass
