from flask import Flask
import json
app = Flask(__name__)

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

@app.route("/")
def hello():
    return todo_list

if __name__ == "__main__":
    app.run(debug=True)
