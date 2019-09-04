#!/usr/bin/env python
# -*- coding: utf-8 -*-
SECRET_KEY = 'this is secret'

DB_USER = 'brook'
DB_PASSWORD = '123456.com'
DB_HOST = '127.0.0.1'
DB_DB = 'api_dev'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'mysql://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_DB
SQLALCHEMY_ECHO = True

DEBUG = True
PORT = 3333
HOST = '127.0.0.1'


UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp3'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024   # 16M
