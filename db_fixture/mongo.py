#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2019/9/20 13:47
# @Author  :kira 
# @FileName: mongo.py

# @Software: PyCharm
import pymongo as pm
import os
import pprint
import configparser as  config

path = os.path.dirname(os.path.dirname(__file__))
path.replace("\\", "/")
real_path = path + "/config.ini"
cf = config.ConfigParser()
cf.read(real_path)

host = cf.get("mongotestconf", "host")
port = cf.get("mongotestconf", "port")


class MongoDb(object):
    def mongo(self, db_name, table_time):
        """

        :param db_name: mongo 数据库名（statistics为数据库名）
        :param table_time: 集合对象表的名称（visitedInfoBean+日期（分区格式））
        :return:
        """
        client = pm.MongoClient(host=host, port=int(port))
        db = client[db_name]
        collect = db[table_time]
        result = collect.find_one()
        return result


if __name__ == "__main__":
    pprint.pprint(MongoDb().mongo("money", "UserInfoEvent20190920")["phone"])
