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

@pswrds_route.route("/pswrd/add", methods=["POST"])
@authorize
def add_pswrd():
    try:
        pswrd_username = request.form["pswrd_username"]
        pswrd_description = request.form["pswrd_description"]
        pswrd_content = request.form["pswrd_content"]
        if (len(pswrd_content)==0 or (len(pswrd_description)==0) or (len(pswrd_username)==0)):
            print("Invalid Password")
            # TODO: Redirect message
        return redirect("/pswrds")
    except:
        return redirect("/pswrds")

    pc = pswrd_controller(session["user"].user_id, pswrd_username, pswrd_description, pswrd_content)
    pc.create_pswrd()
    return redirect("/pswrds")

@pswrds_route.route("/pswrds/delete/<pswrd_id>", methods=["GET"])
@authorize
def delete_pswrd(pswrd_id):
    pc =pswrd_controller(user_id=session["user"].user_id,pswrd_id=pswrd_id)
    pc.delete_pswrd()
    return redirect("/pswrds")
@pswrds_route.route("/pswrds/pin/<pswrd_id>", methods=["GET"])
@authorize
def pin_pswrd(pswrd_id):
    pc = pswrd_controller(user_id=session["user"].user_id,pswrd_id=pswrd_id)
    pc.pin_pswrd(1)
    return redirect("/pswrds")
@pswrds_route.route("/pswrds/pin/<pswrd_id>", methods=["GET"])
@authorize
def unpin_pswrd(pswrd_id):
    pc = pswrd_controller(user_id=session["user"].user_id,pswrd_id=pswrd_id)
    pc.pin_pswrd(0)
    return redirect("/pswrds")
