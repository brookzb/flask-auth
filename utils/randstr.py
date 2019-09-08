#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import string


def generate_random_str(length):
    """
    生成一个指定长度的随机字符串
    """
    str_list = [
        random.choice(string.digits + string.ascii_uppercase) for _ in range(length)
    ]
    random_str = ''.join(str_list)
    return random_str
