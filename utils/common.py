#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


def mobile_field(value):
    """
    自定义手机号校验方法
    :param value:
    :return:
    """
    res = re.fullmatch(r'1[345789]\d{9}', value)
    if not res:
        raise ValueError("手机号码格式不正确")


def email_field(value):
    """
    自定义邮箱校验方法
    :param value:
    :return:
    """
    res = re.fullmatch(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', value)
    if not res:
        raise ValueError("邮箱地址格式不正确")


def trueReturn(data, msg):
    return {
        "status": True,
        "data": data,
        "message": msg
    }


def falseReturn(data, msg):
    return {
        "status": False,
        "data": data,
        "message": msg
    }
