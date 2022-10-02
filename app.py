from flask import Flask, jsonify
from models import todos
from flask import abort

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"


@app.route("/api/v1/todos/", methods=["GET"])
def todos_list_api_v1():
    return jsonify(todos.all())

@app.route("/api/v1/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    todo = todos.get(todo_id)
    if not todo:
        abort(404)
    return jsonify({"todo": todo})


if __name__ == "__main__":
    app.run(debug=True)