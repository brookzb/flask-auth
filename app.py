#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify

from utils.exts import db
import config
from utils import common, headers

from views import todos, files, users, company

app = Flask(__name__)

# 注册蓝图，并指定其对应的前缀（url_prefix）
app.register_blueprint(files.files_opt, url_prefix="/api/v1/file")
app.register_blueprint(todos.todos_opt, url_prefix="/api/v1/todo")
app.register_blueprint(users.users_opt, url_prefix="/api/v1/user")
app.register_blueprint(company.company_opt, url_prefix="/api/v1")

app.config.from_object(config)
app.after_request(headers._access_control)

db.init_app(app)


@app.route('/')
def hello_world():
    return jsonify(common.falseReturn('/', 'Hello Flask!'))


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], host=app.config['HOST'], port=app.config['PORT'])
