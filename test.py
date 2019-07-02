#1.获取整体网页数据 requests
#2.抽取目标数据   lxml.etree  xpath
#3.保存数据  with open
#面向对象编程
#decode  和 encode 的区别
import requests
from lxml import etree

class Spider(object):
    def __init__(self):
        self.url="https://search.jd.com/Search?keyword=%E9%98%BF%E7%8B%B8&enc=utf-8&wq=%E9%98%BF%E7%8B%B8&pvid=dc8c2e1705384b60a300c31946ce665e"
        #反爬虫
        self.headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
            "Referer": "https://search.jd.com/Search?keyword=%E9%98%BF%E7%8B%B8&enc=utf-8&wq=%E9%98%BF%E7%8B%B8&pvid=dc8c2e1705384b60a300c31946ce665e"
        }

    def start_request(self):
        for i in range(1,105):
            print("---------------------正在抓取%s页--------------------"%i)
            if i==1:
            #1.获取整体网页数据 requests
                response=requests.get(self.url)
                html = etree.HTML(response.content.decode())
            else:
                response=requests.get(self.url+"/home/"+str(i))
                html = etree.HTML(response.content.decode())        #content拿到2进制数据，用decode拿到字符串数据
                self.xpath_data(html)

    def xpath_data(self,html):
        #2.抽取想要的数据 lxml.etree xpath
        src_list=html.xpath("//div[@class='w']/ul/li/a/img/@src")
        alt_list=html.xpath("//div[@class='w']/ul/li/a/@titile")
        for src, alt in zip(src_list,alt_list):
            file_name=alt+".jpg"
            print("正在抓取"+file_name)
            response=requests.get(src,headers=self.headers)
            print(response.content)

            #保存数据
            try:
                with open(file_name,"wb") as f:
                    f.write(response.content)
            except:
                pass
spider=Spider()
spider.start_request()