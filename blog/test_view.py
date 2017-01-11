# coding=utf-8

from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask import Blueprint, request
from mongo import conn

test_page = Blueprint('test_page', __name__, template_folder='templates')

db = conn()


@test_page.route('/test', methods=['POST', 'GET'])
def test():
    if request.method == "GET":
        xx = request.method
        return render_template('test.html', method=xx)
    elif request.method == "POST":
        pro = db["Upload_file"]
        _pro = request.get_data()
        print _pro
        xx = request.method
        str = ""
        str += _pro
        return render_template('test.html',method=xx)