#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2019/10/9 17:41
# @Author  :kira 
# @FileName: ConfTime.py

# @Software: PyCharm
import time

# 定义当前时间
CurrentTime = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))
# 定义将来时间
FutureTime = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time() + 100000))
# 定义过去时间
PastTime = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time() - 100000))
if __name__ == "__main__":
    print(CurrentTime, "\n", PastTime, "\n", FutureTime)
