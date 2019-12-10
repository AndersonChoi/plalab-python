# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
application = Flask(__name__)
CORS(application)

todo_list = '''[
  {
    "id": 1,
    "title": "first todo"
  },
  {
    "id": 2,
    "title": "second todo"
  },
  {
    "id": 3,
    "title": "third todo"
  }
]'''

json_todo = json.loads(todo_list)

@application.route("/", methods=['GET'])
def get():
    return jsonify(json_todo)


@application.route("/add", methods=['POST'])
def add():
  request_json = json.loads(json.dumps(request.get_json()))
  print(request_json)

  # 중복되지 않는 가장 큰값의 id보다 +1한 값을 추가
  new_key = {'id':get_latest_id()}
  request_json.update(new_key)

  # id가 추가된 item을 to-do list에 append
  json_todo.append(request_json)
  print(json_todo)
  return str(json_todo)


@application.route("/update", methods=['POST'])
def update():
  request_json = request.get_json()
  print(request_json)

  # element id를 찾아서 삭제
  delete_element_by_id(request_json['id'])

  # id를 가진 element를 기존 list에 추가
  json_todo.append(request_json)
  print(json_todo)
  return str(json_todo)


@application.route("/delete", methods=['DELETE'])
def delete():
  request_json = request.get_json()
  print(request_json)

  # element id를 찾아서 삭제
  delete_element_by_id(request_json['id'])

  return str(json_todo)

# 중복되지 않는 id를 가지기 위해 신규 추가한 to-do item은 
# latest id에 1을 추가한 값을 가지도록 한다.
def get_latest_id():
  max_id = -1
  for todo_item in json_todo:
    if max_id < todo_item['id']:
      max_id = todo_item['id']
  return max_id + 1

# element id를 찾아서 삭제
def delete_element_by_id(id):
  for i in range(len(json_todo)):
      if json_todo[i]["id"] == id:
          json_todo.pop(i)
          break

if __name__ == "__main__":
    application.run(host='0.0.0.0')
