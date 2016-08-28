# coding=utf-8

from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask import Blueprint

test_page = Blueprint('test_page', __name__, template_folder='templates')




@test_page.route('/test')
def test():
    return render_template('test.html')
