from flask import Flask
import json
from flask import request

app = Flask(__name__)


@app.route("/")
def home():
    data = json.dumps({
        "username": "python",
        "pwd": "1234"
    })
    return data


@app.route("/passport/user/login", methods=['GET'])
def login():
    username = request.args.get("username")
    password = request.args.get("password")
    data = json.dumps({
        "code": 200,
        "messgae": "ログインしました",
        "info": {
            "username": username,
            "password": password,
        }
    })
    return data


@app.route("/passport/user/post_login", methods=["POST"])
def post_login():
    request_method = request.method
    if request_method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        data = json.dumps({
            "code": 200,
            "messgae": "ログインしました",
            "info": {
                "username": username,
                "password": password,
            }
        })
    else:
        data = json.dumps({
           "message": "methodエラー",
           "code": 405
        })
    return data

if __name__ == "__main__":
    app.run(debug=True)
