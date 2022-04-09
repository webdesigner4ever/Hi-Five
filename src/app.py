from flask import Flask, render_template, redirect, request, session, jsonify, abort
from flask_session import Session
from functools import wraps
from flask.templating import render_template
from models.db import  db
import os
from controllers.user_controller import user_controller
from controllers.bookmark_controller import bookmark_controller

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        if not session.get("user"):
            return redirect("/login")
        return f(*args, **kws) 
    return decorated_function

@app.route('/login', methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]  

    uc = user_controller(username, password)
    user = uc.login()
    if user != False:
        session["user"] = user
        return redirect("/")
    else:
        return render_template("index.html", message="Invalid Credentials")

@app.route("/logout")
def logout():
    session["user"] = None
    return redirect("/login")

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

@app.route("/bookmarks")
@authorize
def view_bookmarks():
    bc = bookmark_controller(session["user"].user_id)
    bookmarks = bc.get_bookmarks() 
    return render_template("view_bookmarks.html", bookmarks=bookmarks) 

@app.route("/bookmark/add", methods=["POST"])
@authorize
def add_bookmark():
    bc = bookmark_controller(1)
    return ""

@app.route("/", methods=["GET"])
@authorize
def dashboard():
    return render_template("dashboard.html", user=session["user"])

db.init_app(app)

with app.app_context():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)
    db.create_all()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)