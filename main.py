from flask import Flask, request, jsonify
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)

todo_list = '''[
  {
    "id": 1,
    "title": "first todo",
    "description": "pick up milk",
    "complete": true,
    "canceled": true,
    "date": 1389878466730
  },
  {
    "id": 2,
    "title": "second todo",
    "description": "learn backbone",
    "complete": false,
    "canceled": false,
    "date": 1389988926901 
  },
  {
    "id": 3,
    "title": "third todo",
    "description": "go for a run",
    "complete": false,
    "canceled": false,
    "date": 13899924942401  
  }
]'''

json_todo = json.loads(todo_list)

@app.route("/")
def hello():
    return jsonify(json_todo)


@app.route("/add", methods=['POST'])
def add():
  request_json = request.get_json()
  print(request_json)
  json_todo.append(request_json)
  print(json_todo)
  return str(json_todo)

if __name__ == "__main__":
    app.run(debug=True)
