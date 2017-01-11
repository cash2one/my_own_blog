# # coding=utf-8
#
# import urllib2, requests
# from blog_crawl import Blog_spider
# from bs4 import BeautifulSoup as btfs
# import selenium
#
# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "Accept-Language": "zh-CN,zh;q=0.8",
#     "Cookie": 'hasShowWeiyun675912623=1; lastshowtime675912623=1473385739856; __Q_w_s__QZN_TodoMsgCnt=1; __Q_w_s_hat_seed=1; randomSeed=956635; mobileUV=1_155c2d17be7_f252d; tvfe_boss_uuid=e79d6d2f96679c01; __Q_w_s__appDataSeed=1; eas_sid=e1b417b1T3y9x0h8b0h7i5q915; ptui_loginuin=1360508532; AMCV_248F210755B762187F000101%40AdobeOrg=793872103%7CMCIDTS%7C17055%7CMCMID%7C03653594988939970986104545897040821131%7CMCAAMLH-1474094965%7C11%7CMCAAMB-1474094965%7CNRX38WO0n5BH8Th-nqAG_A%7CMCAID%7CNONE; pac_uid=1_675912623; RK=vT0GKO4zMl; o_cookie=675912623; pgv_pvid=6121923620; p_skey=gCG4vBXcneIVcN2ZbEtoiPhW3yoUV7ulaKsEHfSuQo8_; p_uin=o0675912623; pt4_token=2I5CBHg0I3VWG*cOZaJO7UfZ6goASqgVXVyL9x0*gkI_; pgv_info=ssid=s4140811464; pt2gguin=o0675912623; uin=o0675912623; skey=@Yv6sg24bc; ptisp=cnc; qzone_check=675912623_1474600407; ptcz=9e2f52219851303c1d1c7f248b0372ef982e2ac08f71db57dba1ee3da4c981ab; Loading=Yes; qzspeedup=sdch; qz_screen=1920x1080; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=10',
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
# }
#
#
# class Qzone_spider(Blog_spider):
#     # 获取qq空间日志
#     def __init__(self):
#         pass
#
#     @classmethod
#     def get_html(cls, url):
#         s = requests.session()
#         # s.cookies=
#         # response = urllib2.Request(url, headers=headers)
#         # html = urllib2.urlopen(response).read()
#         # html = btfs(html, "lxml")
#         # print html
#
#     @classmethod
#     def get_url(cls, html):
#         pass
#
#     @classmethod
#     def get_href(cls):
#         pass
#
#
# if __name__ == '__main__':
#     # Qzone_spider.get_html("http://user.qzone.qq.com/675912623/main")
#     pass
