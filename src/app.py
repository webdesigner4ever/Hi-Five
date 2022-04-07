from flask import Flask, request, jsonify, redirect
from flask.templating import render_template
from models.db import  db
import os
from controllers.user_controller import user_controller
from controllers.bookmark_controller import bookmark_controller

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]  

    uc = user_controller(username, password)
    if uc.login():
        return render_template("index.html", message="Welcome")
    else:
        return render_template("index.html", message="Invalid Credentials")


@app.route("/register", methods=["GET"])
def register():
    return render_template("register.html")

@app.route("/register.do", methods=["POST"])
def do_register():
    username = request.form["username"]
    password = request.form["password"]  

    uc = user_controller(username, password)
    uc.register()
    
    return render_template("index.html", message="Registration Success")

@app.route("/bookmark/create", methods=["POST"])
def create_bookmark():
    bc = bookmark_controller(1)

@app.route("/dashboard", methods=["GET"])
def dashboard():
    return render_template("dashboard.html")


db.init_app(app)

with app.app_context():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.create_all()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)