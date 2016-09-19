# coding=utf-8

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.laurence

if db.blog:
    pass
else:
    blog = db.blog

if __name__ == '__main__':
    pass
