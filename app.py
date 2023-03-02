from flask import Flask, render_template
from flask_ngrok2 import run_with_ngrok
from config.env import run_with_env
from config.index import connect_app_descriptor

app = Flask(__name__)
run_with_ngrok(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/atlassian-connect.json", methods=["GET"])
def atlassian_connect():
    return connect_app_descriptor


@app.route("/config", methods=["GET"])
def config():
    return render_template("config.html")


if __name__ == "__main__":
    app.run(debug=True)
