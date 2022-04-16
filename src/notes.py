from flask import Blueprint, render_template, redirect, request, session, jsonify, abort
from flask_session import Session
from controllers.note_controller import note_controller
from auth import authorize
from functools import wraps

notes_route = Blueprint("notes_route", __name__)

@notes_route.route("/notes")
@authorize
def view_notes():
    nc = note_controller(session["user"].user_id)
    notes = nc.get_notes() 
    return render_template("view_note.html", notes=notes) 

@notes_route.route("/notes/add", methods=["POST"])
@authorize
def add_note():
    note_title = request.form["note_title"]
    note_desc = request.form["note_desc"]
    note_cont = request.form["note_cont"]
   
    nc = note_controller(session["user"].user_id, note_title, note_desc,note_cont)
    nc.create_note()
    return redirect("/notes")

@notes_route.route("/notes/delete/<note_id>", methods=["GET"])
@authorize
def delete_note(note_id):
    nc =note_controller(user_id=session["user"].user_id,note_id=note_id)
    nc.delete_note()
    return redirect("/notes")
    