#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from functools import wraps

from flask_restful import abort
from itsdangerous import BadSignature, SignatureExpired, \
    TimedJSONWebSignatureSerializer as Serializer
import jwt

from flask import jsonify, request, current_app

from models.model import User, Company


def generate_token(company_obj):
    expiration = 3600
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)  # expiration是过期时间
    token = s.dumps(
        {'app_id': company_obj.app_id, 'code': company_obj.company_code}
    )
    return token, expiration, company_obj.company_code


def required_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message': 'Token is missing!'})

        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
            current_company = Company.query.filter_by(app_id=data['app_id']).first()
        except SignatureExpired:
            # return None  # valid token,but expired
            return jsonify({'message': 'Token is expired'}), 401
        except BadSignature:
            # return None  # invalid token
            return jsonify({'message': 'Token is invalid'}), 401

        return f(current_company, *args, **kwargs)

    return decorated


def authentication(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Accesstoken")
        if not token:
            abort(401, error_message="token缺失")
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode("utf8"))
            company = Company.query.filter_by(app_id=data['app_id']).first()  # TODO 是否根据考虑企业状态过滤
            if not company:
                abort(401, error_message="企业不存在")
            request.company = company
        except SignatureExpired:
            abort(401, error_message="token过期")
        except BadSignature:
            abort(401, error_message="token错误")
        return func(*args, **kwargs)
    return wrapper


def token_generate(api_users):
    expiration = 3600
    token = jwt.encode({'public_id': api_users.public_id,
                        'exp': datetime.datetime.now() + datetime.timedelta(seconds=expiration)},
                       current_app.config['SECRET_KEY'])

    return token, expiration


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message': 'Token is missing!'})

        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            # data['public_id'] will have public id of the authenticated user. login()
            # had encoded the jwt token out of the user's public_id.
            # Check its implementation below in login()
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except Exception as e:
            return jsonify({'message': 'Token is invalid'}), 401

        return f(current_user, *args, **kwargs)

    return decorated
