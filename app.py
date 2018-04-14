from flask import Flask
from flask import render_template
from routes.todo_routes import todo_routes

app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")


app.register_blueprint(todo_routes, url_prefix="/todo")

if __name__ == "__main__":
	app.run(debug=True)