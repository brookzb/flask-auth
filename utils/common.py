#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
