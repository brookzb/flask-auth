#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_restful import Resource, reqparse, marshal_with

from auth import auth as auths
from auth.auth import authentication
from models.model import Company
from utils.common import mobile_field, email_field, company_info_fields
from utils.exts import db
from utils import randstr


class TokenResourceApi(Resource):
    def __init__(self):
        pass

    def get(self):
        app_id = request.args.get('app_id')
        app_key = request.args.get('app_key')
        company = Company.query.filter_by(
            app_id=app_id, app_key=app_key, status=True
        ).first()
        if not company:
            return {"code": 401, "error_message": "企业不存在"}

        token, exp, code = auths.generate_token(company)
        data = {'token': token.decode("utf8"), 'expire': exp, 'code': code}
        return data


class CompanyResourceApi(Resource):
    method_decorators = [authentication]

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("company_code", type=str, required=True, location="form")
        self.parser.add_argument("company_name", type=str, required=True, location="form")
        self.parser.add_argument("contacts", type=str, required=True, location="form")
        self.parser.add_argument("mobile", type=mobile_field, required=True, location="form")
        self.parser.add_argument("email", type=email_field, required=True, location="form")
        self.parser.add_argument("address", type=str, required=True, location="form")
        self.parser.add_argument("billing_account", type=str, required=True, location="form")
        self.parser.add_argument("billing_cycle", type=int, required=True, location="form")
        self.parser.add_argument("long_distance", type=float, required=True, location="form")
        self.parser.add_argument("short_distance", type=float, required=True, location="form")

    @marshal_with(company_info_fields)
    def get(self, company_id):
        """
        查询公司详情
        :param company_id:
        :return:
        """
        company = Company.query.filter_by(id=company_id).first()
        return company

    def put(self, company_id):
        """
        更新企业信息
        :param company_id:
        :return:
        """
        if not request.company.is_admin:
            return {"code": 403, "error_message": "没有编辑权限"}
        company = Company.query.filter_by(id=company_id, status=True).first()
        if not company:
            pass
        args = self.parser.parse_args(strict=False)
        for field, value in args.items():
            setattr(company, field, value)
        db.session.commit()
        return {"id": company.id}

    def post(self):
        """
        添加企业信息
        :return:
        """
        if not request.company.is_admin:
            return {"code": 403, "error_message": "没有添加权限"}
        app_id = randstr.generate_random_str(16)
        app_key = randstr.generate_random_str(32)
        args = self.parser.parse_args(strict=True)
        print(args.items(), args.mobile)
        data = {
            "company_code": args.company_code,
            "company_name": args.company_name,
            "contacts": args.contacts,
            "mobile": args.mobile,
            "email": args.email,
            "address": args.address,
            "billing_account": args.billing_account,
            "billing_cycle": args.billing_cycle,
            "long_distance": args.long_distance,
            "short_distance": args.short_distance,
            "app_id": app_id,
            "app_key": app_key,
            "status": True
        }
        new_company = Company(**data)
        db.session.add(new_company)
        db.session.commit()

        return {"id": new_company.id}

    def delete(self, company_id):
        """
        删除企业信息
        :param company_id:
        :return:
        """
        if not request.company.is_admin:
            return {"code": 403, "error_message": "没有删除权限"}
        company = Company.query.filter_by(id=company_id).first()
        if not company:
            return {"code": 404, "error_message": "企业不存在"}
        company.status = False
        db.session.commit()

        return {"id": company_id}


class CompanyListResourceApi(Resource):
    method_decorators = [authentication]

    def get(self):
        if not request.company.is_admin:
            return {"code": 403, "error_message": "没有查看企业列表权限"}

        queryset = Company.query.all()
        result = []
        for query in queryset:
            data = {
                "id": query.id,
                "company_code": query.company_code,
                "company_name": query.company_name,
                "billing_account": query.billing_account,
                "billing_cycle": query.billing_cycle,
                "long_distance": query.long_distance,
                "short_distance": query.short_distance,
                "contacts": query.contacts,
                "mobile": query.mobile,
                "email": query.email,
                "address": query.address,
                "status": query.status
            }
            result.append(data)
        return {"data": result}
