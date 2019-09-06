# coding: utf-8
from flask_wtf import Form
from wtforms import StringField, FloatField, validators


class RegisterCompanyForm(Form):
    company_name = StringField(
        "企业名称", [
            validators.required("company_name field required"), validators.length(max=32, message="企业名称长度不能超过32")
        ]
    )
    company_code = StringField(
        "企业编码", [
            validators.required("company_code field required"), validators.length(max=16, message="企业名称长度不能超过16")
        ]
    )
    billing_account = StringField("计费账户", [validators.required("billing_account field required")])
    billing_cycle = StringField("计费周期", [validators.required("billing_cycle field required")])
    contacts = StringField(
        "联系人", [
            validators.required("contacts field required"), validators.length(max=6, message="联系人长度不能超过6")
        ]
    )
    mobile = StringField(
        "联系电话", [validators.required("mobile field required"), validators.Regexp(r'1[345789]\d{9}', message="手机号码不合法")
                 ]
    )
    address = StringField(
        "联系地址", [
            validators.required("address field required"), validators.length(max=100, message="企业地址不能超过100")
        ]
    )
    email = StringField("联系邮箱", [validators.Email(message="email invalid")])
    long_distance = FloatField("长途话费")
    short_distance = StringField("短途话费")
