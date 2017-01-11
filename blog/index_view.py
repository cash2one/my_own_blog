# coding=utf-8

from flask import Flask, Blueprint, render_template
from flask_bootstrap import Bootstrap
from mongo import conn
from blog_crawl import Blog_spider
from aboutme import Aboutme
import json

index_page = Blueprint('index_page', __name__, template_folder='templates')

db = conn()

Blog_spider.crawl_blog("blog")


@index_page.route('/laurence')
def hello_world():
    blog_list = db.blog.find()
    blog_list_1 = db.blog.find()
    return render_template('index.html', blog_list=blog_list, blog_list_1=blog_list_1)


@index_page.route('/about')
def aboutme():
    _me = Aboutme.me
    # me = _me.decode("utf-8")
    me = json.loads(json.dumps(_me))
    # me = xx.decode("utf-8")
    # print _me["birthplace"]
    # print me["birthday"]
    return render_template("about.html", me=me)
