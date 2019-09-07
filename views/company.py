#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, jsonify
from flask_restful import Resource

from auth import auth as auths
from models.model import Company
from utils.exts import db
from utils import common, randstr

from flask import Blueprint

from views.forms import RegisterCompanyForm

company_opt = Blueprint('company', __name__)


@company_opt.route('/token', methods=['POST'])
def token():
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
def get_all_company(current_company):
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


@company_opt.route('/add', methods=['POST'])
@auths.required_token
def create_user(current_company):
    if not current_company.admin:
        return jsonify({'message': 'You are not authorized to create a user!'})

    appid = randstr.generate_random_str()
    appkey = randstr.generate_random_str(32)
    form = RegisterCompanyForm()
    if form.validate_on_submit():
        data = {
            "company_code": form.company_code,
            "company_name": form.company_name,
            "contacts": form.contacts,
            "mobile": form.mobile,
            "address": form.address,
            "billing_account": form.billing_account,
            "billing_cycle": form.billing_cycle,
            "long_distance": form.long_distance,
            "short_distance": form.short_distance,
            "appid": appid,
            "appkey": appkey,
            "status": True
        }
        new_company = Company(**data)
        db.session.add(new_company)
        db.session.commit()
        return jsonify(common.trueReturn(data, 'create success!'))
    else:
        pass


@company_opt.route('/del/<company_code>', methods=['DELETE'])
@auths.required_token
def delete_user(current_company, company_code):
    if not current_company.admin:
        return jsonify({'message': 'You are not authorized to delete a user!'})

    company = Company.query.filter_by(code=company_code).first()
    if not company:
        return jsonify({'message': 'Company not found!'})

    db.session.delete(company)
    db.session.commit()
    return common.trueReturn(company_code, 'Company is delete')


@company_opt.route('/detail/<company_code>', methods=['GET'])
@auths.required_token
def get_one_users(current_company, company_code):
    # To mimic this API call via Postman,
    # include 'x-access-token' with the token value obtained from login call

    if current_company.code != int(company_code):
        return common.falseReturn(company_code, '无效公司')

    com = Company.query.filter_by(code=company_code).first()
    if not com:
        return common.trueReturn(company_code, '公司code不存在')

    com_data = {'code': com.code, 'name': com.name, 'account': com.account, 'cycle': com.cycle,
                'long': com.long, 'short': com.short, 'contacts': com.contacts, 'phone': com.phone,
                'email': com.email, 'address': com.address, 'status': com.status, 'update_time': com.update_time}

    return jsonify({'company': com_data})


@company_opt.route('/put/<company_code>', methods=['PUT'])
@auths.required_token
def put_company(current_company, company_code):
    if not current_company.admin:
        if current_company.code != int(company_code):
            return common.falseReturn(company_code, '无权限修改')

        company = Company.query.filter_by(code=company_code).first()
        if not company:
            return jsonify({'message': 'Company not found!'})

        company.admin = True
        db.session.commit()
    else:
        company = Company.query.filter_by(code=company_code).first()
        if not company:
            return jsonify({'message': 'Company not found!'})

        company.admin = True
        db.session.commit()

    return common.falseReturn(company_code, 'Company is modify')


class CompanyResourceApi(Resource):
    def __init__(self):
        pass

    def get(self):
        return {"data": "hello world"}

    def post(self):
        return {"data": "hello world"}

    def put(self):
        return {"data": "hello world"}