#!/usr/bin/env python
# -*- coding: utf-8 -*-
SECRET_KEY = 'this is secret'

DB_USER = 'root'
DB_PASSWORD = 'Admin@9000'
DB_HOST = '148.70.200.5:3306'
DB_DB = 'blog'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'mysql://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_DB
SQLALCHEMY_ECHO = True

DEBUG = True
PORT = 3333
HOST = '127.0.0.1'


UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp3'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024   # 16M
