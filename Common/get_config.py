#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2019/10/10 10:42
# @Author  :kira 
# @FileName: get_config.py

# @Software: PyCharm

from configparser import ConfigParser
from Conf import ConfPath


class ReadConf:
    # 读取配置文件信息
    def read_conf(self, filename, section, option):
        cf = ConfigParser()
        cf.read(filename, encoding='utf-8')
        value = cf.get(section, option)
        return value


if __name__ == '__main__':
    res = ReadConf().read_conf(ConfPath.ConfPath, 'url', 'url_test')
    print(res)
