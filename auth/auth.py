#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from flask import jsonify, request, current_app
import jwt  # pip install pyjwt.PyJWT is a Python library which allows you to encode and decode JSON Web Tokens (JWT)
from functools import wraps
import datetime

from models.model import User


def generate_token(api_users):
    expiration = 3600
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)  # expiration是过期时间
    token = s.dumps({'public_id': api_users.public_id}).decode('ascii')
    return token, expiration


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
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except SignatureExpired:
            # return None  # valid token,but expired
            return jsonify({'message': 'Token is expired'}), 401
        except BadSignature:
            # return None  # invalid token
            return jsonify({'message': 'Token is invalid'}), 401

        return f(current_user, *args, **kwargs)

    return decorated


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
