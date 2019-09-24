#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.exts import db
from datetime import datetime


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(32))
    complete = db.Column(db.Boolean)


# 设置基类方便管理公共字段
class BaseModel(object):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键
    create_time = db.Column(db.DateTime, default=datetime.now)  # 记录的创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)  # 记录的更新时间
    status = db.Column(db.Boolean, default=True, comment='状态')

    def to_dict(self):
        return {
            'id': self.id,
            'create_time': self.create_time,
            'update_time': self.update_time,
            'status': self.status,
        }


class Company(BaseModel, db.Model):
    """
    公司信息表
    """
    __tablename__ = 'company'

    company_code = db.Column(db.String(16), comment='公司编号', unique=True)
    company_name = db.Column(db.String(64), comment="公司名称")
    billing_account = db.Column(db.String(16), comment='计费账号')
    billing_cycle = db.Column(db.Integer, comment='计费周期')
    long_distance = db.Column(db.Float, comment='长途话费/分钟')
    short_distance = db.Column(db.Float, comment='市话费/分钟')
    contacts = db.Column(db.String(32), comment='联系人')
    mobile = db.Column(db.String(11), comment='手机号码')
    email = db.Column(db.String(32), comment='邮箱地址')
    address = db.Column(db.String(64), comment='联系地址')
    app_id = db.Column(db.String(64), comment='接口账号')
    app_key = db.Column(db.String(64), comment='接口秘钥')
    is_admin = db.Column(db.Boolean, default=False, comment='是否超级管理')

    def to_dict(self):
        return {
            "id": self.id,
            "create_time": self.create_time,
            "update_time": self.update_time,
            "status": self.status,
            "company_code": self.company_code,
            "company_name": self.company_name,
            "billing_account": self.billing_account,
            "billing_cycle": self.billing_cycle,
            "long_distance": self.long_distance,
            "short_distance": self.short_distance,
            "contacts": self.contacts,
            "mobile": self.mobile,
            "email": self.email,
            "address": self.address,
            "is_admin": self.is_admin
        }


# 用户表
class User(BaseModel, db.Model):
    """
    用户表，一个公司可以有多个用户，不同公司的用户可以相同
    """
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    company = db.relationship("Company", backref='user')
    public_id = db.Column(db.String(64), comment='用户标识')
    username = db.Column(db.String(50), comment='用户名')
    password = db.Column(db.String(128), comment='用户密码')
    admin = db.Column(db.Boolean, default=False, comment='是否管理员')

    def __repr__(self):
        """非必须, 用于在调试或测试时, 返回一个具有可读性的字符串表示模型."""
        return '<USER %r>' % self.username


# 分机表
class SipUser(BaseModel):
    """
    分机表 一个公司账号可以有多个分机，不同公司的分机号不同
    """
    __tablename__ = "sipuser"
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    company = db.relationship("Company", backref='sipuser')
    sipuser = db.Column(db.String(32), comment='分机号')
    password = db.Column(db.String(32), comment='分机密码')
    caller = db.Column(db.String(50), comment='主叫号码')
    callee = db.Column(db.String(50), comment='被叫号码')
    callmethod = db.Column(db.Integer, comment='呼叫方式')
    direction = db.Column(db.String(16), comment='呼叫方向')
    uuid = db.Column(db.String(50), comment='呼叫uuid')
    buuid = db.Column(db.String(50), comment='呼叫buuid')
    time = db.Column(db.Integer, comment='状态时间')
    state = db.Column(db.String(16), comment='呼叫状态')
    isbleg = db.Column(db.Boolean, comment='是否bleg')

#
#
# class CallOutRoute(db.Model):
#     """
#     呼出路由表， 一个公司账号可以存在多条路由记录
#     """
#     __tablename__ = "calloutroute"
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     company = db.Column(db.Integer, db.ForeignKey('company.code'))
#     start = db.Column(db.String(16), comment='开始分机')
#     end = db.Column(db.String(16), comment='结束分机')
#     prefix = db.Column(db.String(16), comment='前缀')
#     trunk = db.Column(db.String(16), comment='主通道')
#     backup = db.Column(db.String(16), comment='备用通道')
#     number = db.Column(db.String(16), comment='主叫号码')
#     weight = db.Column(db.Integer, comment='优先级')
#     status = db.Column(db.Boolean, default=True, comment='状态')
#     uptime = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')
#
#
# class CallInRoute(db.Model):
#     """
#     呼入路由表， 一个公司账号可以存在多条路由记录
#     """
#     __tablename__ = "callinroute"
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     company = db.Column(db.Integer, db.ForeignKey('company.code'))
#     caller = db.Column(db.String(16), comment='主叫号码')
#     callee = db.Column(db.String(16), comment='被叫号码')
#     timegroup = db.Column(db.String(16), comment='时间组')
#     sourceip = db.Column(db.String(64), comment='呼叫源地址')
#     doaction = db.Column(db.String(16), comment='执行动作')
#     args = db.Column(db.String(16), comment='动作参数')
#     weight = db.Column(db.Integer, comment='优先级')
#     status = db.Column(db.Boolean, default=True, comment='状态')
#     uptime = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')
#
#
# class SipTrunk(db.Model):
#     """
#     线路表、 一个公司可以对应多条线路记录。一个线路记录可以对应多个主叫
#     """
#     __tablename__ = "siptrunk"
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     company = db.Column(db.Integer, db.ForeignKey('company.code'))
#     name = db.relationship("CallerNumber", backref='siptrunk', lazy='dynamic')
#     mark = db.Column(db.String(32), comment='线路名称')
#     prefix = db.Column(db.String(16), comment='呼叫前缀')
#     is_area = db.Column(db.Boolean, comment='固话是否加区号')
#     is_zone = db.Column(db.Boolean, comment='手机是否加拨0')
#     register = db.Column(db.Boolean, comment='是否注册')
#     context = db.Column(db.String(16), comment='文本域')
#     direction = db.Column(db.String(16), comment='接入方向')
#     register_server = db.Column(db.String(64), comment='注册地址')
#     username = db.Column(db.String(32), comment='注册账号')
#     password = db.Column(db.String(32), comment='注册密码')
#     proxy = db.Column(db.String(64), comment='代理ip')
#     transport = db.Column(db.String(16), comment='传输协议')
#     type = db.Column(db.String(16), comment='传输类型', default='rpid')
#     caller_id = db.Column(db.Boolean, comment='是否主叫', default=True)
#     expire = db.Column(db.Integer, comment='注册周期', default=300)
#     retry = db.Column(db.Integer, comment='超时重试', default=60)
#     ping = db.Column(db.Integer, comment='sip检测', default=25)
#     uptime = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')
#
#
# class DisNumber(db.Model):
#     """
#     号码表， 一个公司可以分配多个主叫号码
#     """
#     __tablename__ = "disnumber"
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     company = db.Column(db.Integer, db.ForeignKey('company.code'))
#     number = db.Column(db.String(16), comment='号码')
#     area = db.Column(db.String(16), comment='区号')
#     trunk = db.Column(db.String, db.ForeignKey('siptrunk.name'), comment='线路名称')
#     concurrent = db.Column(db.Integer, comment='号码并发')
#     now_concurrent = db.Column(db.Integer, comment='当前并发')
#     status = db.Column(db.Boolean, default=True, comment='状态')
#     uptime = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')
