#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

from flask_restful import fields


def mobile_field(value):
    """
    自定义手机号校验方法
    :param value:
    :return:
    """
    res = re.fullmatch(r'1[345789]\d{9}', value)
    if not res:
        raise ValueError("手机号码格式不正确")
    return value


def email_field(value):
    """
    自定义邮箱校验方法
    :param value:
    :return:
    """
    res = re.fullmatch(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', value)
    if not res:
        raise ValueError("邮箱地址格式不正确")
    return value


company_info_fields = {
    "id": fields.Integer,
    "company_name": fields.String,
    "company_code": fields.String,
    "billing_account": fields.String,
    "billing_cycle": fields.String,
    "long_distance": fields.Float,
    "short_distance": fields.Float,
    "contacts": fields.String,
    "mobile": fields.String,
    "email": fields.String,
    "address": fields.String,
    "create_time": fields.String,
    "update_time": fields.String
}