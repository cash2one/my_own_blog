# coding=utf-8

import urllib2, requests, re, sys, chardet, datetime
from pyquery import PyQuery as pyq
from mongo import Mongodb

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Cookie": 'uuid_tt_dd=1684901611836556247_20160615; cache_cart_num=0; lzstat_uv=6103127391396727825|3475012@3603726; __message_district_code=230000; __utma=17226283.348199281.1466472479.1470205102.1474351237.3; __utmz=17226283.1474351237.3.2.utmcsr=write.blog.csdn.net|utmccn=(referral)|utmcmd=referral|utmcct=/postlist; _ga=GA1.2.348199281.1466472479; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1474266325,1474334971,1474429914; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1474429920; _message_m=155nwfcrqx2hlpi1aqya3vqj; UserName=laurencechan; UserInfo=jWzio%2FHHUPCTe9tJ1Hp4dw6Vsiz13LsMZW9IouKiwch4%2BTDHaNsk3ykMXEXj0RH4a3oOQyKtGw1ai89dWQm5JseWlpfjinil4FaZ9OG9LCn1atlrIcP7shdyPkbMSBQHQG065qz7c3xigrtD4SCb9A%3D%3D; UserNick=laurencechan; AU=8AE; UN=laurencechan; UE="chenlr10@aliyun.com"; BT=1474429922334; access-token=e65ca402-36ed-4884-942f-b6e0e417db1e; dc_tos=odubcc; dc_session_id=1474437612141; __message_sys_msg_id=0; __message_gu_msg_id=0; __message_cnel_msg_id=0; __message_in_school=0',
    "Upgrade-Insecure-Requests": 1,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}
headers_1 = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    # "Cookie":"bdshare_firstime=1465873936870; uuid_tt_dd=1684901611836556247_20160615; cache_cart_num=0; lzstat_uv=6103127391396727825|3475012@3603726; __utma=17226283.348199281.1466472479.1468809623.1470205102.2; __utmz=17226283.1468809623.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __message_district_code=230000; uuid=10e4bae1-148a-4c78-a4f3-7053c35d8290; _ga=GA1.2.348199281.1466472479; _gat=1; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1474266325,1474334971; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1474334971; _message_m=gjg3e0sgizts2za1ykiknso2; UserName=laurencechan; UserInfo=jWzio%2FHHUPCTe9tJ1Hp4dw6Vsiz13LsMZW9IouKiwch4%2BTDHaNsk3ykMXEXj0RH4a3oOQyKtGw1ai89dWQm5JseWlpfjinil4FaZ9OG9LCn1atlrIcP7shdyPkbMSBQHQG065qz7c3xigrtD4SCb9A%3D%3D; UserNick=laurencechan; AU=8AE; UN=laurencechan; UE="chenlr10@aliyun.com"; BT=1474334972401; access-token=3d07b7e1-ee43-4260-a7a4-8e25dbd1570a; avh=8727308%2c39927017%2c51939809; dc_tos=ods45m; dc_session_id=1474334968389; __message_sys_msg_id=0; __message_gu_msg_id=0; __message_cnel_msg_id=0; __message_in_school=0",
    "Referer": "http://write.blog.csdn.net/postlist",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}

headers_2 = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Cookie": 'bdshare_firstime=1465873936870; uuid_tt_dd=1684901611836556247_20160615; cache_cart_num=0; lzstat_uv=6103127391396727825|3475012@3603726; __message_district_code=230000; uuid=10e4bae1-148a-4c78-a4f3-7053c35d8290; _message_m=gjg3e0sgizts2za1ykiknso2; _ga=GA1.2.348199281.1466472479; UserName=laurencechan; UserInfo=jWzio%2FHHUPCTe9tJ1Hp4dw6Vsiz13LsMZW9IouKiwch4%2BTDHaNsk3ykMXEXj0RH4a3oOQyKtGw1ai89dWQm5JseWlpfjinil4FaZ9OG9LCn1atlrIcP7shdyPkbMSBQHQG065qz7c3xigrtD4SCb9A%3D%3D; UserNick=laurencechan; AU=8AE; UN=laurencechan; UE="chenlr10@aliyun.com"; BT=1474339430090; access-token=e57db925-17e1-44bb-bd45-38f1b77a85c0; __utma=17226283.348199281.1466472479.1470205102.1474351237.3; __utmc=17226283; __utmz=17226283.1474351237.3.2.utmcsr=write.blog.csdn.net|utmccn=(referral)|utmcmd=referral|utmcct=/postlist; avh=51907576%2c51939809; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1474266325,1474334971; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1474354695; __message_sys_msg_id=0; __message_gu_msg_id=0; __message_cnel_msg_id=0; __message_in_school=0; dc_tos=odsjlo; dc_session_id=1474354453601',
    "Referer": "http://blog.csdn.net/laurencechan/article/details/51939809",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}


class Blog_spider():
    def __init__(self, url):
        self.url = url
        pass

    @classmethod
    def get_html(self, url):
        # 获取目标url的html str
        response = urllib2.Request(url, headers=headers)
        html = urllib2.urlopen(response).read()
        # print html
        return html

    @classmethod
    def get_html_1(cls, url):
        # 获取目标url的html str 与上一个方法相比  headers不相同 并且得到的是一个pyquery类
        response = urllib2.Request(url, headers=headers_1)
        html = urllib2.urlopen(response).read()
        doc = pyq(html)
        return doc

    @classmethod
    def get_summary(cls):
        response = urllib2.Request("http://blog.csdn.net/laurencechan", headers=headers_2)
        html = urllib2.urlopen(response).read()
        doc = pyq(html)
        summary_list = []
        summary_dic = {}
        for i in range(0, len(Blog_spider.get_href())):
            summary_dic["title"] = doc(".link_title a").eq(i).text()
            summary_dic["summary"] = doc(".article_description").eq(i).text()
            summary_dic["index"] = len(Blog_spider.get_href())-i
            summary_list.append(summary_dic)
            summary_dic = {}
        return summary_list

    @staticmethod
    def get_href():
        # 通过正则匹配获取目标url
        reg = r'(http.+?/details/\d+)'
        url_reg = re.compile(reg)
        url_list = re.findall(url_reg, Blog_spider.get_html("http://write.blog.csdn.net/postlist"))
        # for i in url_list:
        #     print i
        return url_list

    @classmethod
    def get_data(cls, url):
        # 将目标内容以json格式存入Mongodb
        # url_list = Blog_spider.get_href()
        blog_dic = {}
        # for i in url_list:
        doc = Blog_spider.get_html_1(url)
        blog_dic["title"] = doc(".link_title a").text()
        blog_dic["cat"] = doc(".category_r span").text()
        blog_dic["content"] = doc("#article_content").html()
        blog_dic["time"] = doc(".link_postdate").text()
        blog_dic["tag"] = doc(".link_categories a").text()
        if doc(".article_content img").attr("src") != None:
            blog_dic["image"] = doc(".article_content img").attr("src")
        else:
            blog_dic["image"] = "static/images/python.jpg"
        for i in Blog_spider.get_summary():
            if i["title"] == blog_dic["title"]:
                blog_dic["summary"] = i["summary"]
                blog_dic["index"] = i["index"]
        # print blog_dic
        Mongodb.c_collections(blog_dic)
        # blog_dic = {}

    @classmethod
    def crawl_decide(cls):
        # 判断是否有新的数据，如果有刚添加进Mongodb
        new_list = Blog_spider.get_href()
        xx = len(new_list)
        # blog_dic = {}
        if len(new_list) <= Mongodb.data_count():
            pass
        else:
            for i in range(0, len(new_list) - Mongodb.data_count()):
                Blog_spider.get_data(new_list[i])


if __name__ == '__main__':
    # Blog_spider.get_html("http://write.blog.csdn.net/postlist")
    # Blog_spider.get_href()
    # Blog_spider.get_data()
    # Blog_spider.get_html_1("http://blog.csdn.net/laurencechan/article/details/51907576")
    # Blog_spider.crawl_decide()
    # Blog_spider.get_summary()
    pass
