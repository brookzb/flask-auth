define({ "api": [
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "varname1",
            "description": "<p>No type.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "varname2",
            "description": "<p>With type.</p>"
          }
        ]
      }
    },
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "./static/docs/main.js",
    "group": "D__project_pyproject_flask_flask_auth_static_docs_main_js",
    "groupTitle": "D__project_pyproject_flask_flask_auth_static_docs_main_js",
    "name": ""
  },
  {
    "type": "get",
    "url": "/api/v1.0/file/download/<filename>",
    "title": "下载文件",
    "version": "1.0.0",
    "name": "download",
    "group": "File",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "filename",
            "description": "<p>(必须)    文件名</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "回参": [
          {
            "group": "回参",
            "type": "String",
            "optional": false,
            "field": "status",
            "description": "<p>true</p>"
          },
          {
            "group": "回参",
            "type": "String",
            "optional": false,
            "field": "data",
            "description": "<p>文件</p>"
          },
          {
            "group": "回参",
            "type": "String",
            "optional": false,
            "field": "message",
            "description": "<p>下载成功</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"data\":test.txt,\n    \"message\":\"success！\",\n    \"status\": \"true\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "{\n    \"errno\":4002,\n    \"errmsg\":\"文件下载失败！\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./views/files.py",
    "groupTitle": "File"
  },
  {
    "type": "post",
    "url": "/api/v1.0/file/upload",
    "title": "上传文件",
    "version": "1.0.0",
    "name": "upload",
    "group": "File",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "file",
            "description": "<p>(必须)    文件名</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    file: \"test.txt\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "回参": [
          {
            "group": "回参",
            "type": "String",
            "optional": false,
            "field": "status",
            "description": "<p>true</p>"
          },
          {
            "group": "回参",
            "type": "String",
            "optional": false,
            "field": "data",
            "description": "<p>文件</p>"
          },
          {
            "group": "回参",
            "type": "String",
            "optional": false,
            "field": "message",
            "description": "<p>上传成功</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"data\":test.txt,\n    \"message\":\"success！\",\n    \"status\": \"true\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "{\n    \"errno\":4001,\n    \"errmsg\":\"文件上传失败！\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./views/files.py",
    "groupTitle": "File"
  },
  {
    "type": "post",
    "url": "/api/v1.0/todo/add",
    "title": "添加数据",
    "version": "1.0.0",
    "name": "add",
    "group": "Todo",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "text",
            "description": "<p>(必须)    内容</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    text: \"测试数据\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "回参": [
          {
            "group": "回参",
            "type": "int",
            "optional": false,
            "field": "todo_id",
            "description": "<p>数据id</p>"
          },
          {
            "group": "回参",
            "type": "String",
            "optional": false,
            "field": "text",
            "description": "<p>文本内容</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"errno\":0,\n    \"errmsg\":\"添加成功！\",\n    \"data\": {\n        \"user_id\": 1,\n        \"text\": \"\"测试数据\n    }\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "{\n    \"errno\":4001,\n    \"errmsg\":\"添加失败！\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./views/todos.py",
    "groupTitle": "Todo"
  },
  {
    "type": "delete",
    "url": "/api/v1.0/todo/del/<todo_id>",
    "title": "删除数据",
    "version": "1.0.0",
    "name": "del",
    "group": "Todo",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "todo_id",
            "description": "<p>(必须)    数据id</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "回参": [
          {
            "group": "回参",
            "type": "int",
            "optional": false,
            "field": "todo_id",
            "description": "<p>数据id</p>"
          },
          {
            "group": "回参",
            "type": "String",
            "optional": false,
            "field": "text",
            "description": "<p>文本内容</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"errno\":0,\n    \"errmsg\":\"删除成功！\",\n    \"data\": {\n    }\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "{\n    \"errno\":4001,\n    \"errmsg\":\"删除失败！\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./views/todos.py",
    "groupTitle": "Todo"
  },
  {
    "type": "get",
    "url": "/api/v1.0/todo/list",
    "title": "查询所有数据",
    "version": "1.0.0",
    "name": "list",
    "group": "Todo",
    "success": {
      "fields": {
        "回参": [
          {
            "group": "回参",
            "type": "String",
            "optional": false,
            "field": "status",
            "description": "<p>true</p>"
          },
          {
            "group": "回参",
            "type": "String",
            "optional": false,
            "field": "data",
            "description": "<p>内容</p>"
          },
          {
            "group": "回参",
            "type": "String",
            "optional": false,
            "field": "message",
            "description": "<p>获取成功</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"errno\":0,\n    \"errmsg\":\"获取成功！\",\n    \"data\": {\n        \"id\": 1,\n        \"text\": \"text\",\n        \"complete\": \"complete\"\n    }\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "{\n    \"errno\":4001,\n    \"errmsg\":\"记录不存在！\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./views/todos.py",
    "groupTitle": "Todo"
  },
  {
    "type": "get",
    "url": "/api/v1.0/todo/list/<todo_id>",
    "title": "查询指定数据",
    "version": "1.0.0",
    "name": "list",
    "group": "Todo",
    "success": {
      "fields": {
        "回参": [
          {
            "group": "回参",
            "type": "String",
            "optional": false,
            "field": "status",
            "description": "<p>true</p>"
          },
          {
            "group": "回参",
            "type": "String",
            "optional": false,
            "field": "data",
            "description": "<p>内容</p>"
          },
          {
            "group": "回参",
            "type": "String",
            "optional": false,
            "field": "message",
            "description": "<p>获取成功</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"errno\":0,\n    \"errmsg\":\"获取成功！\",\n    \"data\": {\n        \"id\": 1,\n        \"text\": \"text\",\n        \"complete\": \"complete\"\n    }\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "{\n    \"errno\":4001,\n    \"errmsg\":\"记录不存在！\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./views/todos.py",
    "groupTitle": "Todo"
  },
  {
    "type": "put",
    "url": "/api/v1.0/todo/put/<todo_id>",
    "title": "修改数据",
    "version": "1.0.0",
    "name": "put",
    "group": "Todo",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "todo_id",
            "description": "<p>(必须)    数据id</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "回参": [
          {
            "group": "回参",
            "type": "int",
            "optional": false,
            "field": "todo_id",
            "description": "<p>数据id</p>"
          },
          {
            "group": "回参",
            "type": "String",
            "optional": false,
            "field": "text",
            "description": "<p>文本内容</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    \"errno\":0,\n    \"errmsg\":\"修改成功！\",\n    \"data\": {\n        \"user_id\": 1,\n        \"text\": \"\"测试数据\n    }\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "{\n    \"errno\":4001,\n    \"errmsg\":\"添加失败！\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./views/todos.py",
    "groupTitle": "Todo"
  }
] });
