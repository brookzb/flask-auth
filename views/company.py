#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

from auth import auth as auths
from models.model import Company
from utils.exts import db
from utils import common

from flask import Blueprint
company_opt = Blueprint('company', __name__)


@company_opt.route('/token', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        app_id = request.form['appid']
        app_key = request.form['appkey']
    else:
        app_id = request.args.get('appid')
        app_key = request.args.get('appkey')

    company_obj = Company.query.filter_by(app_id=app_id).first()

    if not company_obj:
        return common.falseReturn('检查appid', '')

    if app_key == company_obj.app_key:
        token, exp, code = auths.generate_token(company_obj)
        return jsonify({'token': token.decode('UTF-8'), 'expire': exp, 'code': code})

    return common.falseReturn('授权无效', '')


@company_opt.route('/list', methods=['GET'])
@auths.required_token
def get_one_user(current_company):
    if not current_company.admin:
        return jsonify({'message': 'You are not authorized see ny user data!'})

    company = Company.query.all()
    if not company:
        return jsonify(common.falseReturn('', 'User not found!'))

    output = []
    for com in company:
        com_data = {'code': com.code, 'name': com.name, 'account': com.account, 'cycle': com.cycle,
                    'long': com.long, 'short': com.short, 'contacts': com.contacts, 'phone': com.phone,
                    'email': com.email, 'address': com.address, 'status': com.status, 'update_time': com.update_time}
        output.append(com_data)
    return jsonify({'company': output})


@company_opt.route('/detail/<company_code>', methods=['GET'])
@auths.required_token
def get_all_users(current_company, company_code):
    # To mimic this API call via Postman,
    # include 'x-access-token' with the token value obtained from login call

    print(type(current_company.code), type(company_code))
    if current_company.code != int(company_code):
        return common.falseReturn('无效公司', '')

    com = Company.query.filter_by(code=company_code).first()
    if not com:
        return common.trueReturn(company_code, '公司code不存在')

    com_data = {'code': com.code, 'name': com.name, 'account': com.account, 'cycle': com.cycle,
                'long': com.long, 'short': com.short, 'contacts': com.contacts, 'phone': com.phone,
                'email': com.email, 'address': com.address, 'status':com.status, 'update_time': com.update_time}

    return jsonify({'company': com_data})


# @users_opt.route('/add', methods=['POST'])
# @auths.required_token
# def create_user(current_user):
#     if not current_user.admin:
#         return jsonify({'message': 'You are not authorized to create a user!'})
#
#     data = request.get_json()
#     print('Data is %s', data)
#     hashed_pwd = generate_password_hash(data['password'], method='sha256')
#     new_user = User(public_id=str(uuid.uuid4()), name=data['name'], password=hashed_pwd, admin=False)
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify(common.trueReturn(data['name'], 'New user created!'))
#
#
# @users_opt.route('/put/<public_id>', methods=['PUT'])
# @auths.required_token
# def promote_user(current_user, public_id):
#     if not current_user.admin:
#         return jsonify({'message': 'You are not authorized to promote a user!'})
#
#     user = User.query.filter_by(public_id=public_id).first()
#     if not user:
#         return jsonify({'message': 'User not found!'})
#
#     user.admin = True
#     db.session.commit()
#     return jsonify({'message': 'The user has been promoted!'})
#
#
# @users_opt.route('/put/demote/<public_id>', methods=['PUT'])
# @auths.required_token
# def demote_user(current_user, public_id):
#     if not current_user.admin:
#         return jsonify({'message': 'You are not authorized to demote any user!'})
#
#     user = User.query.filter_by(public_id=public_id).first()
#     if not user:
#         return jsonify({'message': 'User not found!'})
#
#     user.admin = False
#     db.session.commit()
#     return jsonify({'message': 'The user has been demoted!'})
#
#
# @users_opt.route('/del/<public_id>', methods=['DELETE'])
# @auths.required_token
# def delete_user(current_user, public_id):
#     if not current_user.admin:
#         return jsonify({'message': 'You are not authorized to delete a user!'})
#
#     user = User.query.filter_by(public_id=public_id).first()
#     if not user:
#         return jsonify({'message': 'User not found!'})
#
#     db.session.delete(user)
#     db.session.commit()
#     return jsonify({'message': 'The user has been deleted!'})
