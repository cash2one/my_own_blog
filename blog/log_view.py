# coding=utf-8

from flask import Flask, Blueprint, render_template
from flask_bootstrap import Bootstrap



log_page = Blueprint('log_page', __name__, template_folder='templates')


@log_page.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
