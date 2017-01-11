# coding=utf-8

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.laurence


class Mongodb():
    def __init__(self):
        pass

    @classmethod
    def c_collections(cls, blog_dic={}, name=""):
        # db.createCollection(name)
        article = db[name].insert_one(blog_dic).inserted_id
        pass

    @classmethod
    def data_count(cls):
        return db.blog.find().count()


def conn():
    db = client.laurence
    return db


if __name__ == '__main__':
    Mongodb.data_count()
    pass
