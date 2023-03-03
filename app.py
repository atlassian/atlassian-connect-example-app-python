from flask import Flask, render_template, json
from flask_ngrok2 import run_with_ngrok
import os
from config.env import run_with_env
from config.index import connect_app_descriptor

app = Flask(__name__)
run_with_env(app)


@app.route("/")
def index():
    return render_template("index.html", index="Home Page", body="You in the home page!")


@app.route("/atlassian-connect.json", methods=["GET"])
def atlassian_connect():
    return connect_app_descriptor


@app.route("/config", methods=["GET"])
def config():
    print(type(connect_app_descriptor))
    return render_template("config.html", index="Connect app descriptor", config=json.dumps(connect_app_descriptor,
                                                                                            skipkeys = True,
                                                                                            allow_nan = True,
                                                                                            indent = 6))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
