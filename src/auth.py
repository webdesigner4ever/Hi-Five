from flask import Blueprint, render_template, redirect, request, session, jsonify, abort
from functools import wraps
from flask_session import Session
from controllers.user_controller import user_controller

login_route = Blueprint("login_route", __name__)

def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        if not session.get("user"):
            return redirect("/login")
        return f(*args, **kws) 
    return decorated_function

@login_route.route('/login', methods=["GET"])
def index():
    return render_template("index.html")

@login_route.route("/login", methods=["POST"])
def login():
    try:
        username = request.form["username"]
        password = request.form["password"]  

        uc = user_controller(username, password)
        user = uc.login()
        if user != False:
            session["user"] = user
            return redirect("/")
        else:
            return render_template("index.html", message="Invalid Credentials")
    except:
        return render_template("index.html", message="All fields are required.")

@login_route.route("/logout")
def logout():
    session["user"] = None
    return redirect("/login")

@login_route.route("/register", methods=["GET"])
def register():
    return render_template("register.html")

# TODO: Password encryption
@login_route.route("/register.do", methods=["POST"])
def do_register():
    try:
        username = request.form["username"]
        password = request.form["password"]  
        confirm_password = request.form["confirm_password"]
        if (confirm_password == password):
            uc = user_controller(username, password)
            uc.register()
            return render_template("index.html", message="Registration Success")
        else:
            return render_template("register.html", message="Password does not match") 
    except:
        return render_template("index.html", message="Registration failed")
        
 
@login_route.route("/", methods=["GET"])
@authorize
def dashboard():
    return render_template("dashboard.html", user=session["user"])

@login_route.route("/settings", methods=["GET"])
def changepassword():
    return render_template("changepassword.html")

@login_route.route("/changepassword", methods=["POST"])
def do_password():
    currentpassword = request.form["current_password"]
    New_password = request.form["New_password"]  
    confirm_password = request.form["confirm_password"]

    if New_password==confirm_password:
        uc = user_controller(session.get("user").username, currentpassword)
        success = uc.changepassword(currentpassword,New_password)
        if success == True:
            return render_template("changepassword.html", message="Password changed successfully.")
        else:
            return render_template("changepassword.html", message="Incorrect current passowrd.")
    else:
        return render_template("changepassword.html", message="Password does not match")