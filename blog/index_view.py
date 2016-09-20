# coding=utf-8

from flask import Flask, Blueprint, render_template
from flask import render_template
from flask_bootstrap import Bootstrap
from mongo import conn

index_page = Blueprint('index_page', __name__, template_folder='templates')

db = conn()


@index_page.route('/')
def hello_world():
    blog_list = db.blog.find()
    return render_template('index_test.html', blog_list=blog_list)
