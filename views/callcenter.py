#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, jsonify

import os
from auth import auth as auths
from models.model import Company
from utils.exts import db
from utils import common, randstr

from flask import Blueprint
call_opt = Blueprint('call', __name__)


@call_opt.route('/callout', methods=['POST'])
@auths.required_token
def callout(current_company):
    # print(request.args)  # get
    # print(request.form)    # post
    request_list = ['extnumber', 'disnumber', 'destnumber', 'crmid', 'memberid', 'customuuid']   # 所有字段
    request_dict = {}
    for field in request_list:
        if field in dict(request.form):
            request_dict[field] = request.form[field]
        else:
            request_dict[field] = 0
    print(request_dict)

    extnumber = request.form['extnumber']
    disnumber = request.form['disnumber']    # 主叫
    destnumber = request.form['destnumber']    # 被叫
    crmid = request.form['crmid']  # 销售工号
    memberid = request.form['memberid']  # 客户编号
    customuuid = request.form['customuuid']  # 自定义值

    call_cmd = 'lua apicall.lua extnumber=%s|disnumber=%s|destnumber=%s|crmid=%s|memberid=%s|customuuid=%s' % \
               (extnumber, disnumber, destnumber, crmid, memberid, customuuid)
    call_str = "ucc -p yunhu -x '%s'" % call_cmd
    print(call_str)
    # res = os.system(call_str)
    # if res == 0:
    #     return jsonify(common.trueReturn("", "呼叫成功"))
    return  ''''''

