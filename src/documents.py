from flask import Blueprint, render_template, redirect, request, session, jsonify, abort
from flask_session import Session
from controllers.document_controller import document_controller
from auth import authorize
from functools import wraps

documents_route = Blueprint("documents_route", __name__)

@documents_route.route("/documents")
@authorize
def view_documents():
    dc = document_controller(session["user"].user_id)
    documents = dc.get_documents() 
    return render_template("view_documents.html", documents=documents) 

@documents_route.route("/documents/add", methods=["POST"])
@authorize
def add_document():
    document_title = request.form["document_title"]
    document_desc = request.form["document_desc"]
    documents_url = request.form["document_url"]
    dc = document_controller(session["user"].user_id, document_title, document_desc, document_url)
    dc.create_document()
    return redirect("/documents")

@documents_route.route("/documents/delete/<document_id>", methods=["GET"])
@authorize
def delete_document(document_id):
    dc = document_controller(user_id=session["user"].user_id,document_id=document_id)
    dc.delete_document()
    return redirect("/documents")
    