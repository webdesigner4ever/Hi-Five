from flask import Blueprint, render_template, redirect, request, session, jsonify, abort
from flask_session import Session
from controllers.bookmark_controller import bookmark_controller
from auth import authorize
from functools import wraps

bookmarks_route = Blueprint("bookmarks_route", __name__)

@bookmarks_route.route("/bookmarks")
@authorize
def view_bookmarks():
    bc = bookmark_controller(session["user"].user_id)
    bookmarks = bc.get_bookmarks() 
    return render_template("view_bookmarks.html", bookmarks=bookmarks) 

@bookmarks_route.route("/bookmarks/add", methods=["POST"])
@authorize
def add_bookmark():
    bookmark_title = request.form["bookmark_title"]
    bookmark_desc = request.form["bookmark_desc"]
    bookmark_url = request.form["bookmark_url"]
    bc = bookmark_controller(session["user"].user_id, bookmark_title, bookmark_desc, bookmark_url)
    bc.create_bookmark()
    return redirect("/bookmarks")

@bookmarks_route.route("/bookmarks/delete/<bookmark_id>", methods=["GET"])
@authorize
def delete_bookmark(bookmark_id):
    bc = bookmark_controller(user_id=session["user"].user_id,bookmark_id=bookmark_id)
    bc.delete_bookmark()
    return redirect("/bookmarks")
    