# coding=utf-8

import pymysql.cursors
import os
import configparser as cparser
import pymysql.cursors
from Common import login
from Conf import ConfPath

# ======== Reading config.ini setting ===========
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/config.ini"

cf = cparser.ConfigParser()

cf.read(file_path)
host = cf.get("mysqltestconf", "host")
port = cf.get("mysqltestconf", "port")
db = cf.get("mysqltestconf", "db_name")
user = cf.get("mysqltestconf", "user")
password = cf.get("mysqltestconf", "password")



class DB(object):

    def do_sql(self, sql, methods=4):
        """
        :param sql:传入的 单条sql 语句
        :param methods: 1==增，2==删，3==改，4==查,默认==4
        :return: 返回查的结果
        """
        try:
            # Connect to the database
            connect_mysql = pymysql.connect(host=host,
                                            port=int(port),
                                            user=user,
                                            password=password,
                                            db=db,
                                            charset='utf8mb4',
                                            cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
        with connect_mysql.cursor() as cursor:
            result = None
            if methods == 4:
                try:
                    cursor.execute(str(sql))  # 执行传入的 sql
                    result = cursor.fetchone()  # 查询单条数据 并将结果返回给 result
                    # result = cursor.fetchall()        # 查询多条数据 并将结果返回给 result
                except:
                    print("Error: unable to fecth data")
                    connect_mysql.close()  # 关闭数据连接
                return result
            elif methods == 2:
                try:
                    cursor.execute(sql)  # 执行删除 sql 操作
                    connect_mysql.commit()  # 提交操作
                except:
                    connect_mysql.rollback()  # 发生错误时执行回滚
            elif methods == 3:
                try:
                    cursor.execute(sql)  # 执行更新 sql 操作
                    connect_mysql.commit()  # 提交操作
                except:
                    connect_mysql.rollback()
            elif methods == 1:
                try:
                    cursor.execute(sql)  # 执行插入 sql 操作
                    connect_mysql.commit()  # 提交操作
                except:
                    connect_mysql.rollback()
            else:
                return print("method 没有这个关键字")
            connect_mysql.close()  # 关闭连接






'''
select_sql = "SELECT * FROM t_user_attendance WHERE accountid = '156286031586086490';"
update_sql = "UPDATE `sinaif_easy`.`t_user_attendance` SET `id`='132872401180598272', `accountid`='156286031586086490', `attendtime`='2019-06-26 09:55:22', `continueday`='1', `remark`=NULL, `creatime`='2019-01-02 15:47:29', `updatime`='2019-06-26 09:55:22' WHERE (`id`='132872401180598272');"

doSQL = DB()
result = []
result.append(doSQL.do_sql(update_sql, 3))
result.append(doSQL.do_sql(select_sql, 4))
print(result)
'''

