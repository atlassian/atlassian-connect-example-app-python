import requests
from flask import Flask, render_template, make_response, jsonify, json

from config.env import run_with_env
import os

app = Flask(__name__)
run_with_env(app)

app_url = os.environ.get("APP_URL")


@app.route("/")
def index():
    print("Rendering home page")
    return render_template("index.html")

connect_app_descriptor = {
    "name": "Sample Connect App Python",
    "description": "Atlassian Connect app - Python",
    "key": "com.atlassian.sample-app-python",
    "baseUrl": app_url,
    "vendor": {
        "name": "Python connect app sample",
        "url": "https://github.com/atlassian/atlassian-connect-sample-app-python/"
    },
    "authentication": {
        "type": "none"
    },
    "apiVersion": 1,
    "modules": {
        "generalPages": [
            {
                "url": "/templates/index.html",
                "key": "hello-world",
                "location": "system.top.navigation.bar",
                "name": {
                    "value": "Test"
                }
            }
        ],
        "postInstallPage": {
            "url": "index.html",
            "key": "acn-index",
            "name": {
                "value": "Index"
            }
        },
    }
}


@app.route("/atlassian-connect.json", methods=["GET"])
def atlassian_connect():
    return connect_app_descriptor


if __name__ == "__main__":
    app.run(debug=True)
