#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

from auth import auth as auths
from models.model import User
from utils.exts import db
from utils import common

from flask import Blueprint
users_opt = Blueprint('users', __name__)


@users_opt.route('/login')
def login():
    # To mimic this API call ia Postman,
    # select GET as http protocol and in the Authorization section, select Basic Auth.
    # Enter username and password to invoke the API
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    user = User.query.filter_by(name=auth.username).first()

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    if check_password_hash(user.password, auth.password):
        token, exp = auths.generate_token(user)

        return jsonify({'token': token.decode('UTF-8'), 'expire': exp})

    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})


@users_opt.route('/list', methods=['GET'])
@auths.required_token
def get_all_users(current_user):
    # To mimic this API call via Postman,
    # include 'x-access-token' with the token value obtained from login call

    if not current_user.admin:
        return jsonify({'message': 'You are not authorized to see all users!'})

    users = User.query.all()
    output = []
    for user in users:
        user_data = {'public_id': user.public_id, 'name': user.name, 'password': user.password, 'admin': user.admin}
        output.append(user_data)

    return jsonify({'users': output})


@users_opt.route('/list/<public_id>', methods=['GET'])
@auths.required_token
def get_one_user(current_user, public_id):
    if not current_user.admin:
        return jsonify({'message': 'You are not authorized see ny user data!'})

    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify(common.falseReturn('', 'User not found!'))

    user_data = {'public_id': user.public_id, 'name': user.name, 'password': user.password, 'admin': user.admin}
    return jsonify({'user': user_data})


@users_opt.route('/add', methods=['POST'])
@auths.required_token
def create_user(current_user):
    if not current_user.admin:
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


@users_opt.route('/put/demote/<public_id>', methods=['PUT'])
@auths.required_token
def demote_user(current_user, public_id):
    if not current_user.admin:
        return jsonify({'message': 'You are not authorized to demote any user!'})

    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({'message': 'User not found!'})

    user.admin = False
    db.session.commit()
    return jsonify({'message': 'The user has been demoted!'})


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
