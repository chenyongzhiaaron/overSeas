# -*- coding: utf-8 -*-

import random
from random import choice

def create_phone(metho=None):
    if metho == 0:
        phone = 18100000000
    else:
        # 第二位数字
        second = choice([3, 4, 5, 7, 8])
        # 第三位数字
        third = {
            3: random.randint(0, 9),
            4: [5, 7, 9][random.randint(0, 2)],
            5: [i for i in range(10) if i != 4][random.randint(0, 8)],
            7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
            8: random.randint(0, 9),
        }[second]
        # 最后八位数字
        suffix = random.randint(9999999, 100000000)
        # 拼接手机号
        phone = "1{}{}{}".format(second, third, suffix)
    return phone


# # 生成手机号
# phone = create_phone(1)
# print(phone)

list_b = []
for i in range(0,99):
    a = choice([3, 4, 5, 7, 8])

    list_b.append(a)
    print(list_b)
