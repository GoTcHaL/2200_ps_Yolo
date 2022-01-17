from flask import Flask, render_template, request, redirect, send_file
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
auth = HTTPBasicAuth()


        #ID: test        PW: 1234  
user = {"test": generate_password_hash("1234")}


@auth.verify_password
def verify_password(name, password):
    if name in user and \
        check_password_hash(user.get(name), password): # user가 가진 PW 와 입력한 PW 확인
        return name


@app.route('/')
@auth.login_required(role='admin') # ID 가 admin인 유저만 접근가능
def index():
    return "안녕하세요, {}님!".format(auth.current_user())



if __name__ == "__main__":
    app.run(debug=False)

    print('')