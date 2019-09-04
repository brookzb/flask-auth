#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_apidoc.commands import GenerateApiDoc
from app import app
from utils.exts import db
# from models import  User,Todo
# db.create_all()

manager = Manager(app)

# init  migrate upgrade
# 模型 -> 迁移文件 -> 表

# 1.要使用flask_migrate,必须绑定app和DB
migrate = Migrate(app, db)

# 2.把migrateCommand命令添加到manager中。
manager.add_command('db', MigrateCommand)
manager.add_command('apidoc', GenerateApiDoc())


if __name__ == '__main__':
    manager.run()
