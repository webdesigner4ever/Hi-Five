from flask import Blueprint, render_template, redirect, request, session, jsonify, abort
from flask_session import Session
from controllers.pswrd_controller import pswrd_controller
from auth import authorize
from functools import wraps

pswrds_route = Blueprint("pswrds_route", __name__)

@pswrds_route.route("/pswrds")
@authorize
def view_pswrds():
    pc = pswrd_controller(session["user"].user_id)
    pswrds = pc.get_pswrds() 
    return render_template("view_pswrds.html", pswrds=pswrds) 

@pswrds_route.route("/pswrds/add", methods=["POST"])
@authorize
def add_pswrd():
    pswrd_title = request.form["pswrd_title"]
    pswrd_desc = request.form["pswrd_desc"]
    pswrd_cont = request.form["pswrd_cont"]
   
    pc = pswrd_controller(session["user"].user_id, pswrd_title, pswrd_desc,pswrd_cont)
    pc.create_pswrd()
    return redirect("/pswrds")

@pswrds_route.route("/pswrds/delete/<pswrd_id>", methods=["GET"])
@authorize
def delete_pswrd(pswrd_id):
    pc =pswrd_controller(user_id=session["user"].user_id,pswrd_id=pswrd_id)
    pc.delete_pswrd()
    return redirect("/pswrds")