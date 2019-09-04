#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, jsonify
from auth import auth as auths
from models.model import Todo
from utils.exts import db

from flask import Blueprint
todos_opt = Blueprint('todos', __name__)


@todos_opt.route('/list', methods=['GET'])
@auths.required_token
def get_all_todos(current_user):
    """
        @api {get} /api/v1.0/todo/list 查询所有数据
        @apiVersion 1.0.0
        @apiName list
        @apiGroup Todo

        @apiSuccess (回参) {String} status  true
        @apiSuccess (回参) {String} data  内容
        @apiSuccess (回参) {String} message  获取成功
        @apiSuccessExample {json} Success-Response:
            {
                "errno":0,
                "errmsg":"获取成功！",
                "data": {
                    "id": 1,
                    "text": "text",
                    "complete": "complete"
                }
            }

        @apiErrorExample {json} Error-Response:
           {
               "errno":4001,
               "errmsg":"记录不存在！"
           }
   """
    todos = Todo.query.filter_by(user_id=current_user.id).all()
    output = []
    for todo in todos:
        todo_data = {'id': todo.id, 'text': todo.text, 'complete': todo.complete}
        output.append(todo_data)
    return jsonify({'todos': output})


@todos_opt.route('/list/<todo_id>', methods=['GET'])
@auths.required_token
def get_one_todo(current_user, todo_id):
    """
         @api {get} /api/v1.0/todo/list/<todo_id> 查询指定数据
         @apiVersion 1.0.0
         @apiName list
         @apiGroup Todo

         @apiSuccess (回参) {String} status  true
         @apiSuccess (回参) {String} data  内容
         @apiSuccess (回参) {String} message  获取成功
         @apiSuccessExample {json} Success-Response:
              {
                  "errno":0,
                  "errmsg":"获取成功！",
                  "data": {
                      "id": 1,
                      "text": "text",
                      "complete": "complete"
                  }
              }

         @apiErrorExample {json} Error-Response:
             {
                 "errno":4001,
                 "errmsg":"记录不存在！"
             }
    """
    todo = Todo.query.filter_by(id=todo_id, user_id=current_user.id).first()
    if not todo:
        return jsonify({'message': 'No todo found!'})
    todo_data = {'id': todo.id, 'text': todo.text, 'complete': todo.complete}
    return todo_data


@todos_opt.route('/add', methods=['POST'])
@auths.required_token
def create_todo(current_user):
    """
       @api {post} /api/v1.0/todo/add  添加数据
       @apiVersion 1.0.0
       @apiName add
       @apiGroup Todo
       @apiParam {String}  text      (必须)    内容
       @apiParamExample {json} Request-Example:
           {
               text: "测试数据"
           }

       @apiSuccess (回参) {int} todo_id 数据id
       @apiSuccess (回参) {String} text  文本内容
       @apiSuccessExample {json} Success-Response:
           {
               "errno":0,
               "errmsg":"添加成功！",
               "data": {
                   "user_id": 1,
                   "text": ""测试数据
               }
           }

       @apiErrorExample {json} Error-Response:
           {
               "errno":4001,
               "errmsg":"添加失败！"
           }
       """
    data = request.get_json()

    new_todo = Todo(text=data['text'], complete=False, user_id=current_user.id)
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({'message': 'Todo created!'})


@todos_opt.route('/put/<todo_id>', methods=['PUT'])
@auths.required_token
def complete_todo(current_user, todo_id):
    """
        @api {put} /api/v1.0/todo/put/<todo_id> 修改数据
        @apiVersion 1.0.0
        @apiName put
        @apiGroup Todo
        @apiParam {String}  todo_id      (必须)    数据id

        @apiSuccess (回参) {int} todo_id 数据id
        @apiSuccess (回参) {String} text  文本内容
        @apiSuccessExample {json} Success-Response:
           {
               "errno":0,
               "errmsg":"修改成功！",
               "data": {
                   "user_id": 1,
                   "text": ""测试数据
               }
           }

        @apiErrorExample {json} Error-Response:
           {
               "errno":4001,
               "errmsg":"添加失败！"
           }
   """
    todo = Todo.query.filter_by(id=todo_id, user_id=current_user.id).first()
    if not todo:
        return jsonify({'message': 'No todo found!'})

    todo.complete = True
    db.session.commit()

    return jsonify({'message': 'Todo item has been marked completed'})


@todos_opt.route('/del/<todo_id>', methods=['DELETE'])
@auths.required_token
def delete_todo(current_user, todo_id):
    """
        @api {delete} /api/v1.0/todo/del/<todo_id> 删除数据
        @apiVersion 1.0.0
        @apiName del
        @apiGroup Todo
        @apiParam {String}  todo_id      (必须)    数据id

        @apiSuccess (回参) {int} todo_id 数据id
        @apiSuccess (回参) {String} text  文本内容
        @apiSuccessExample {json} Success-Response:
           {
               "errno":0,
               "errmsg":"删除成功！",
               "data": {
               }
           }

        @apiErrorExample {json} Error-Response:
           {
               "errno":4001,
               "errmsg":"删除失败！"
           }
       """
    todo = Todo.query.filter_by(id=todo_id, user_id=current_user.id).first()
    if not todo:
        return jsonify({'message': 'No todo found!'})

    db.session.delete(todo)
    db.session.commit()
    return jsonify({'message': 'The todo item has been deleted!'})
