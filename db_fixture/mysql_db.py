# coding=utf8
import configparser as cparser

import pymysql.cursors
from Conf import ConfPath

# ======== Reading config.ini setting ===========

file_path = ConfPath.ConfPath

cf = cparser.ConfigParser()

cf.read(file_path)
host = cf.get("mysqlproconf", "host")
port = cf.get("mysqlproconf", "port")
db = cf.get("mysqlproconf", "db_name")
user = cf.get("mysqlproconf", "user")
password = cf.get("mysqlproconf", "password")


# ======== MySql base operating ===================
class DB:
    def __init__(self):
        try:
            # Connect to the database
            self.connection = pymysql.connect(host=host,
                                              port=int(port),
                                              user=user,
                                              password=password,
                                              db=db,
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    # clear user_address table data
    def clear_address(self, table_name):
        # real_sql = "truncate table " + table_name + ";"
        # real_sql = "delete from " + table_name + ";"    # 这是清光表数据
        real_sql = "delete from " + table_name + " where user_id = 352 and id >88;"    # 这是清空特定行数据
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")  # 删除外键约束
            cursor.execute(real_sql)
            cursor.execute("SET FOREIGN_KEY_CHECKS=1")  # 启动外键约束
        self.connection.commit()

    # clear funcl_fun_code table data
    def clear_fun_code(self, table_name):
        # real_sql = "truncate table " + table_name + ";"
        real_sql = "delete from " + table_name + ";"    # 这是清光表数据
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")  # 删除外键约束
            cursor.execute(real_sql)
            cursor.execute("SET FOREIGN_KEY_CHECKS=1")  # 启动外键约束
        self.connection.commit()

    # insert sql statement
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        print(real_sql)

        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)

        self.connection.commit()

    # close database
    def close(self):
        self.connection.close()

    # init user_address data
    def init_data_address(self, datas):
        for table, data in datas.items():
            self.clear_address(table)
            for d in data:
                self.insert(table, d)
        self.close()

    # init fun_code data
    def init_data_fun_code(self, datas):
        for table, data in datas.items():
            self.clear_fun_code(table)
            for d in data:
                self.insert(table, d)
        self.close()








'''

if __name__ == '__main__':
    db = DB()
    table_name = "user_address"
    data = {'user_id': 352, 'deliver_name': '测试工作者', 'deliver_phone': 17727475174, 'deliver_address_country_id': 44,
            'deliver_address_province_id': 11,
            'deliver_address_city_id': 1101, 'deliver_address_district_id': 110101, "deliver_address": "测试办公室",
            "created_at": "2018-11-28 19:10:00", "updated_at": "2018-11-28 19:10:00",
            "deliver_address_country_name": "中国",
            "deliver_address_province_name": "北京市", "deliver_address_city_name": "市辖区",
            "deliver_address_district_name": "东城区"}
    # table_name2 = "sign_guest"
    # data2 = {'realname': 'alen', 'phone': 12312341234, 'email': 'alen@mail.com', 'sign': 0, 'event_id': 1}

    db.clear(table_name)
    db.insert(table_name, data)
    db.close()
    
 '''
