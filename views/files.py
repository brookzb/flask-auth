#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, make_response, url_for, send_from_directory
from urllib.parse import quote
import os, re
# from werkzeug.utils import secure_filename

# from app import app
import config
from utils import common

from flask import Blueprint
files_opt = Blueprint('files', __name__)


def secure_filename(filename):
    # 确保文件名中不包含非法字符
    filename = re.sub('[" "\/\--]+', '-', filename)
    filename = re.sub(r':-', ':', filename)
    filename = re.sub(r'^-|-$', '', filename)
    return filename


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in config.ALLOWED_EXTENSIONS


@files_opt.route('/upload', methods=['POST'])
def upload():
    """
       @api {post} /api/v1.0/file/upload 上传文件
       @apiVersion 1.0.0
       @apiName upload
       @apiGroup File
       @apiParam {String}  file      (必须)    文件名
       @apiParamExample {json} Request-Example:
           {
               file: "test.txt"
           }

       @apiSuccess (回参) {String} status  true
       @apiSuccess (回参) {String} data  文件
       @apiSuccess (回参) {String} message  上传成功
       @apiSuccessExample {json} Success-Response:
           {
               "data":test.txt,
               "message":"success！",
               "status": "true"
           }

       @apiErrorExample {json} Error-Response:
           {
               "errno":4001,
               "errmsg":"文件上传失败！"
           }

       """
    upload_file = request.files['file']
    filename = secure_filename(upload_file.filename)
    if upload_file and allowed_file(upload_file.filename):
        upload_file.save(os.path.join(config.UPLOAD_FOLDER, filename))
        print(url_for('upload', filename=filename))
        return common.trueReturn(filename, 'success')
    else:
        return common.falseReturn(filename, 'failed')


@files_opt.route("/download/<filename>", methods=['GET'])
def download(filename):
    """
       @api {get} /api/v1.0/file/download/<filename> 下载文件
       @apiVersion 1.0.0
       @apiName download
       @apiGroup File
       @apiParam {String}  filename      (必须)    文件名

       @apiSuccess (回参) {String} status  true
       @apiSuccess (回参) {String} data  文件
       @apiSuccess (回参) {String} message  下载成功
       @apiSuccessExample {json} Success-Response:
           {
               "data":test.txt,
               "message":"success！",
               "status": "true"
           }

       @apiErrorExample {json} Error-Response:
           {
               "errno":4002,
               "errmsg":"文件下载失败！"
           }

       """
    # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名(带扩展名)
    directory = config.UPLOAD_FOLDER     # 假设在当前目录
    print(quote(filename.encode('utf8')))
    response = make_response(send_from_directory(directory, filename, as_attachment=True))
    response.headers["Content-Disposition"] = "attachment; filename={0}; filename*=utf-8''{0}"\
        .format(quote(filename.encode('utf8')))
    return response
