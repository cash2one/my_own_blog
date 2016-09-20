# coding=utf-8

from flask import Flask, render_template, Blueprint
from bson import ObjectId
from mongo import conn

detail_page = Blueprint('detail_page', __name__, template_folder='templates')

db = conn()


@detail_page.route('/detail/<id>')
def detail_view(id):
    article = db.blog.find_one({"_id": ObjectId(id)})

    return render_template('detail.html',article=article)
