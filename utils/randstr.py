#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import string


def generate_random_str(length=16):
    """
    生成一个指定长度的随机字符串，其中
    string.digits=0123456789
    string.ascii_letters=abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    """
    str_list = [random.choice(string.digits + string.ascii_letters) for i in range(length)]
    random_str = ''.join(str_list)
    return random_str.upper()
