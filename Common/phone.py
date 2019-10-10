# -*- coding: utf-8 -*-

import random
from random import choice


def create_phone(methos=None):
    """
    :param methos: 0 & string
    :return: 0 返回固定手机号，其它返回随机手机号
    """
    if methos == 0:
        phone = 18100000000
    else:
        # 第二位数字
        second = choice([3, 4, 5, 7, 8])
        # 第三位数字
        third = {
            3: random.randint(0, 9),
            4: choice([5, 7, 9]),
            5: choice([i for i in range(10) if i != 4]),
            7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
            8: random.randint(0, 9),
        }[second]
        # 最后八位数字
        suffix = random.randint(9999999, 100000000)
        # 拼接手机号
        phone = "1{}{}{}".format(second, third, suffix)
    return phone


if __name__ == "__main__":
    # 生成手机号
    phone = create_phone(1)
    print(phone)
