from flask import Blueprint, render_template, redirect, request, session, jsonify, abort
from flask_session import Session
from controllers.note_controller import note_controller
from auth import authorize
from functools import wraps
import markdown2

notes_route = Blueprint("notes_route", __name__)

@notes_route.route("/notes")
@authorize
def view_notes():
    nc = note_controller(session["user"].user_id)
    notes = nc.get_notes() 
    return render_template("view_note.html", notes=notes) 

@notes_route.route("/notes/edit/<note_id>", methods=["GET"])
@authorize
def edit_note(note_id):
    nc = note_controller(session["user"].user_id, note_id=note_id)
    note = nc.get_note()
    return render_template("view_note.html", edit_note=note) 

@notes_route.route("/notes/view/<note_id>", methods=["GET"])
@authorize
def view_note(note_id):
    nc = note_controller(session["user"].user_id, note_id=note_id)
    note = nc.get_note()

    view_note = {
        "title": note.note_title,
        "content": markdown2.markdown(note.note_content)
    }
    return render_template("view_note.html", view_note=view_note) 

@notes_route.route("/notes/add", methods=["POST"])
@authorize
def add_note():
    note_title = request.form["note_title"]
    note_cont = request.form["note_cont"]
   
    nc = note_controller(session["user"].user_id, note_title, note_cont)
    nc.create_note()
    return redirect("/notes")

@notes_route.route("/notes/update/<note_id>", methods=["POST"])
@authorize
def update_note(note_id):
    note_title = request.form["note_title"]
    note_cont = request.form["note_cont"]
    nc = note_controller(session["user"].user_id, note_id=note_id, note_title=note_title, note_content=note_cont)
    nc.update_note()
    return redirect("/notes")

@notes_route.route("/notes/delete/<note_id>", methods=["GET"])
@authorize
def delete_note(note_id):
    nc = note_controller(user_id=session["user"].user_id, note_id=note_id)
    nc.delete_note()
    return redirect("/notes")
    