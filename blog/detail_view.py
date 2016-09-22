# coding=utf-8

from flask import Flask, render_template, Blueprint
from bson import ObjectId
from mongo import conn

detail_page = Blueprint('detail_page', __name__, template_folder='templates')

db = conn()


@detail_page.route('/detail/<id>')
def detail_view(id):
    article = db.blog.find_one({"_id": ObjectId(id)})
    index = article['index']
    before = db.blog.find_one({"index": index - 1})
    after = db.blog.find_one({"index": index + 1})
    return render_template('detail.html', article=article,before=before,after=after)
