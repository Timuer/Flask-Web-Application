from flask import Flask
from routes.todo_routes import todo_routes

app = Flask(__name__)


@app.route("/")
def index():
	return "Hello"


app.register_blueprint(todo_routes, url_prefix="/todo")

if __name__ == "__main__":
	app.run(debug=True)