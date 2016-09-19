# coding=utf-8

import urllib2, requests, re, sys,chardet
from pyquery import PyQuery as pyq

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Cookie": 'uuid_tt_dd=1684901611836556247_20160615; cache_cart_num=0; lzstat_uv=6103127391396727825|3475012@3603726; __utma=17226283.348199281.1466472479.1468809623.1470205102.2; __utmz=17226283.1468809623.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __message_district_code=230000; _ga=GA1.2.348199281.1466472479; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1474266325; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1474266325; _message_m=4cf1xvkrzl30ljil4xzi2liq; UserName=laurencechan; UserInfo=jWzio%2FHHUPCTe9tJ1Hp4dw6Vsiz13LsMZW9IouKiwch4%2BTDHaNsk3ykMXEXj0RH4a3oOQyKtGw1ai89dWQm5JseWlpfjinil4FaZ9OG9LCn1atlrIcP7shdyPkbMSBQHQG065qz7c3xigrtD4SCb9A%3D%3D; UserNick=laurencechan; AU=8AE; UN=laurencechan; UE="chenlr10@aliyun.com"; BT=1474266328239; access-token=c9faaa93-a61a-49ab-a6c5-01d8525d7b17; dc_tos=odqq3p; __message_sys_msg_id=0; __message_gu_msg_id=0; __message_cnel_msg_id=0; __message_in_school=0; dc_session_id=1474270117427',
    "Host": "write.blog.csdn.net",
    "Referer": "http://passport.csdn.net/account/login?from=http%3a%2f%2fwrite.blog.csdn.net%2f%3fticket%3dST-20681-SsmpOWNcvvVv3Sj21a9r-passport.csdn.net",
    "Upgrade-Insecure-Requests": 1,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}


class Blog_spider():
    def __init__(self, url):
        self.url = url
        pass

    @classmethod
    def get_html(self, url):
        response = urllib2.Request(url, headers=headers)
        html = urllib2.urlopen(response).read()
        return html

    @classmethod
    def get_href(cls):
        reg = r'(http.+?/details/\d+)'
        url_reg = re.compile(reg)
        url_list = re.findall(url_reg, Blog_spider.get_html("http://write.blog.csdn.net/postlist"))
        # for i in url_list:
        #     print i
        return url_list

    @classmethod
    def get_data(cls):
        for i in Blog_spider.get_href():
            doc = Blog_spider.get_html(i)
            html = pyq(doc)
            cts = html('.article_title')
            print cts



if __name__ == '__main__':
    # Blog_spider.get_html("http://write.blog.csdn.net/postlist")
    # Blog_spider.get_href()
    Blog_spider.get_data()
    pass
