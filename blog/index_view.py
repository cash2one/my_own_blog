# coding=utf-8

from flask import Flask, Blueprint, render_template
from flask import render_template
from flask_bootstrap import Bootstrap



index_page = Blueprint('index_page', __name__, template_folder='templates')


@index_page.route('/')
def hello_world():
    return render_template('index.html')
