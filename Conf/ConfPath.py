#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2019/10/9 16:26
# @Author  :kira 
# @FileName: ConfPath.py

import os

# 项目路径
ProjectPath = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

# 测试用例目录
TestDataPath = os.path.join(ProjectPath, "interface")

# Html 测试报告路径
ReportPath = os.path.join(ProjectPath, "OutPut", "report\\")

# 日志路径
LogPath = os.path.join(ProjectPath, "OutPut", "Log")

# ini 配置文件路径
# ConfPath = os.path.join(ProjectPath, "Conf", "config.ini")
ConfPath = os.path.join(ProjectPath,'conee.config')

# if __name__ == "__main__":
    # print(TestDataPath, "\n", LogPath, "\n", ReportPath, "\n", ConfPath)
