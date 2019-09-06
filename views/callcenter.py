#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, jsonify
import os
from auth import auth as auths
from utils import common, randstr

from flask import Blueprint
call_opt = Blueprint('call', __name__)


# 发起呼叫
@call_opt.route('/callout', methods=['POST'])
@auths.required_token
def callout(current_company):
    # print(request.args)  # get
    # print(request.form)    # post
    request_list = ['extnumber', 'disnumber', 'destnumber', 'crmid', 'memberid', 'customuuid']   # 所有字段,前三个字段必填
    request_dict = {}
    for field in request_list:
        if field in dict(request.form):
            request_dict[field] = request.form[field]
        else:
            request_dict[field] = 0

    call_cmd = 'lua apicall.lua extnumber=%s|disnumber=%s|destnumber=%s|crmid=%s|memberid=%s|customuuid=%s' % \
               (request_dict['extnumber'], request_dict['disnumber'], request_dict['destnumber'], request_dict['crmid'],
                request_dict['memberid'], request_dict['customuuid'])
    call_str = "ucc -p yunhu -x '%s'" % call_cmd
    print(call_str)
    # res = os.system(call_str)
    # if res == 0:
    #     return jsonify(common.trueReturn("", "呼叫成功"))
    return  ""


# 播放语音
@call_opt.route('/playvoice', methods=['POST'])
@auths.required_token
def callout(current_company):
    request_list = ['method', 'calltonumber', 'disnumber', 'crmid', 'memberid', 'customuuid']   # 所有字段,前三个字段必填
    request_dict = {}
    for field in request_list:
        if field in dict(request.form):
            request_dict[field] = request.form[field]
        else:
            request_dict[field] = 0

    call_cmd = 'lua playvoice.lua method=%s|calltonumber=%s|disnumber=%s|crmid=%s|memberid=%s|customuuid=%s' % \
               (request_dict['method'], request_dict['calltonumber'], request_dict['disnumber'], request_dict['crmid'],
                request_dict['memberid'], request_dict['customuuid'])
    call_str = "ucc -p yunhu -x '%s'" % call_cmd
    print(call_str)
    # res = os.system(call_str)
    # if res == 0:
    #     return jsonify(common.trueReturn("", "播放成功"))
    return  ""


# 呼叫监听
@call_opt.route('/spycall', methods=['POST'])
@auths.required_token
def callout(current_company):
    request_list = ['type', 'extnumber', 'destnumber']   # 所有字段,字段必填
    request_dict = {}
    for field in request_list:
        if field in dict(request.form):
            request_dict[field] = request.form[field]
        else:
            request_dict[field] = 0

    call_cmd = 'lua spycall.lua type=%s|extnumber=%s|destnumber=%s' % \
               (request_dict['type'], request_dict['extnumber'], request_dict['destnumber'])
    call_str = "ucc -p yunhu -x '%s'" % call_cmd
    print(call_str)
    # res = os.system(call_str)
    # if res == 0:
    #     return jsonify(common.trueReturn("", "监听成功"))
    return  ""


# 结束呼叫
@call_opt.route('/hangup', methods=['POST'])
@auths.required_token
def callout(current_company):
    request_list = ['extnumber']   # 所有字段,字段必填
    request_dict = {}
    for field in request_list:
        if field in dict(request.form):
            request_dict[field] = request.form[field]
        else:
            request_dict[field] = 0

    call_cmd = 'lua hangup.lua extnumber=%s' % request_dict['extnumber']
    call_str = "ucc -p yunhu -x '%s'" % call_cmd
    print(call_str)
    # res = os.system(call_str)
    # if res == 0:
    #     return jsonify(common.trueReturn("", "挂机成功"))
    return  ""
