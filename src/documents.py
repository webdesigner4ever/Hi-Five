from flask import Blueprint, render_template, redirect, request, session, jsonify, abort, current_app
from werkzeug.utils import secure_filename
from flask_session import Session
from controllers.document_controller import document_controller
from auth import authorize
from functools import wraps
import uuid
import os 

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
    f = request.files['document']
    folder_id = str(uuid.uuid4())
    filename = folder_id + "/" + f.filename
    os.mkdir(os.path.join(current_app.config['UPLOAD_FOLDER'], folder_id))
    f.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
    dc = document_controller(session["user"].user_id, document_title, filename)
    dc.create_document()
    return redirect("/documents")

@documents_route.route("/documents/delete/<document_id>", methods=["GET"])
@authorize
def delete_document(document_id):
    dc = document_controller(user_id=session["user"].user_id, document_id=document_id)
    dc.delete_document()
    return redirect("/documents")
    