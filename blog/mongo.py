# coding=utf-8

from pymongo import MongoClient

# localhost
client = MongoClient('localhost', 27017)

# 测试Mongo服务器
# client = MongoClient("mongodb://chinahlj_user:chinahlj_user123@125.211.222.237:27638/laurence")
# connection = MongoClient('125.211.222.237:27638', 123456)
# db = connection["laurence"]
# db.authenticate('chinahlj_user', 'chinahlj_user123')
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
