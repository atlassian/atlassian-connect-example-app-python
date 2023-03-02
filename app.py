from flask import Flask, render_template
from config.env import run_with_env
from config.index import connect_app_descriptor

app = Flask(__name__)
run_with_env(app)

@app.route("/")
def index():
    print("Rendering home page")
    return render_template("index.html")

@app.route("/atlassian-connect.json", methods=["GET"])
def atlassian_connect():
    return connect_app_descriptor


if __name__ == "__main__":
    app.run(debug=True)