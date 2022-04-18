from flask import Flask
from models.db import db
from flask_session import Session
import os
basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    
    with app.app_context():       
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.sqlite')
        app.config["SESSION_PERMANENT"] = False
        app.config["SESSION_TYPE"] = "filesystem"
        Session(app)
        db.init_app(app)
        db.create_all()


        # Import parts of our application
        from bookmarks import bookmarks_route
        from auth import login_route
        from notes import notes_route
        from documents import documents_route
       
        # Register Blueprints
        app.register_blueprint(bookmarks_route)
        app.register_blueprint(login_route)
        app.register_blueprint(notes_route)
        app.register_blueprint(documents_route)
       

        return app

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8086, debug=True)