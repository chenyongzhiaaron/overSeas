# coding=utf-8

import pymysql.cursors
import os
import configparser as cparser
import pymysql.cursors
from Global_base import login

# ======== Reading db_config.ini setting ===========
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/db_config.ini"

cf = cparser.ConfigParser()

cf.read(file_path)
host = cf.get("mysqltestconf", "host")
port = cf.get("mysqltestconf", "port")
db = cf.get("mysqltestconf", "db_name")
user = cf.get("mysqltestconf", "user")
password = cf.get("mysqltestconf", "password")


class T_DB:

    def __init__(self):
        # 初始化链接数据库
        try:
            self.connection = pymysql.connect(host=host,
                                              port=int(port),
                                              user=user,
                                              password=password,
                                              db=db,
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def do_sql(self, method, sql, params=None):
        cursor = self.connection.cursor()
        result = None
        if method == "select":
            try:
                cursor.execute(sql)  # 执行传入的 sql
                result = cursor.fetchone()  # 查询单条数据 并将结果返回给 result
                # result = cursor.fetchall()        # 查询多条数据 并将结果返回给 result
            except:
                print("Error: unable to fecth data")
            values = result[params]
            self.connection.close()  # 关闭数据连接
            return str(values)
        elif method == "delete":
            try:
                cursor.execute(sql)  # 执行删除 sql 操作
            except:
                self.connection.rollback()  # 发生错误时执行回滚
        elif method == "update":
            try:
                cursor.execute(sql)  # 执行更新 sql 操作
            except:
                self.connection.rollback()
            return print("")
        elif method == "insert":
            try:
                cursor.execute(sql)  # 执行插入 sql 操作
            except:
                self.connection.rollback()
        else:
            return print("method 没有这个关键字")
        self.connection.commit()  # 提交插入操作
        self.connection.close()  # 关闭连接

    def action_init(self, method, sql, params=None):
        value = self.do_sql(method, sql, params)
        return value


select_sql = "SELECT * FROM t_user_attendance WHERE accountid = '154207626636745530';"
method = "select"
# doSQL = T_DB.action_init(method, select_sql, "accountid")
doSQL = T_DB.do_sql("select", select_sql, "accountid")
print(doSQL)

