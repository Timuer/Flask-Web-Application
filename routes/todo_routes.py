from model.Todo import Todo
import time
from utils import get_local_time
from flask import (
	Blueprint,
	render_template,
	request,
)

todo_routes = Blueprint("todo", __name__)


@todo_routes.route("/")
def todo_index():
	todos = Todo.all()
	return render_template("todo.html", todos=todos)


@todo_routes.route("/add", methods=["POST"])
def add():
	todo = Todo.new(request.form)
	todo.save()
	todos = Todo.all()
	return render_template("todo.html", todos=todos)


@todo_routes.route("/update", methods=["GET", "POST"])
def update():
	if request.method == "GET":
		todo_id = request.args.get("id", "")
		return render_template("todo_edit.html", todo_id=todo_id)
	form = request.form
	todo_id = form.get("id", "")
	todo = Todo.find_by_id(todo_id)
	# update todo in the db
	_updateTodo(todo, form)
	Todo.delete(todo_id)
	todo.save()
	# get all the todos to render template
	todos = Todo.all()
	return render_template("todo.html", todos=todos)


def _updateTodo(todo, form):
	for k, v in form.items():
		setattr(todo, k, v)
	todo.ut = get_local_time(time.time())


@todo_routes.route("/del", methods=["GET"])
def delete():
	todo_id = request.args.get("id", "")
	Todo.delete(todo_id)
	todos = Todo.all()
	return render_template("todo.html", todos=todos)
