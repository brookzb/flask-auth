#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

from auth import auth as auths
from models.model import User, Company
from utils.exts import db
from utils import common

from flask import Blueprint
users_opt = Blueprint('users', __name__)


@users_opt.route('/list', methods=['GET'])
@auths.required_token
def get_all_users(current_company):
    # To mimic this API call via Postman,
    # include 'x-access-token' with the token value obtained from login call

    if not current_company.admin:
        return jsonify({'message': 'You are not authorized to see all users!'})

    # users = User.query.all()
    users = db.session.query(Company).filter(Company.code == current_company.code).first()
    users_li = users.user
    output = []
    for user in users_li:
        user_data = {'public_id': user.public_id, 'username': user.username, 'password': user.password, 'admin': user.admin}
        output.append(user_data)

    return common.trueReturn({'users': output}, 'get success!')


@users_opt.route('/list/<public_id>', methods=['GET'])
@auths.required_token
def get_one_user(current_company, public_id):
    if not current_company.admin:
        return jsonify({'message': 'You are not authorized see ny user data!'})

    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify(common.falseReturn('', 'User not found!'))

    user_data = {'public_id': user.public_id, 'name': user.username, 'password': user.password, 'admin': user.admin}
    return jsonify(common.trueReturn({'user': user_data}, 'get success!'))


@users_opt.route('/add', methods=['POST'])
@auths.required_token
def create_user(current_company):
    if not current_company.admin:
        return jsonify({'message': 'You are not authorized to create a user!'})

    data = request.get_json()
    print('Data is %s', data)
    hashed_pwd = generate_password_hash(data['password'], method='sha256')
    new_user = User(public_id=str(uuid.uuid4()), name=data['name'], password=hashed_pwd, admin=False)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(common.trueReturn(data['name'], 'New user created!'))


@users_opt.route('/put/<public_id>', methods=['PUT'])
@auths.required_token
def promote_user(current_user, public_id):
    if not current_user.admin:
        return jsonify({'message': 'You are not authorized to promote a user!'})

    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({'message': 'User not found!'})

    user.admin = True
    db.session.commit()
    return jsonify({'message': 'The user has been promoted!'})


@users_opt.route('/del/<public_id>', methods=['DELETE'])
@auths.required_token
def delete_user(current_user, public_id):
    if not current_user.admin:
        return jsonify({'message': 'You are not authorized to delete a user!'})

    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({'message': 'User not found!'})

    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'The user has been deleted!'})
