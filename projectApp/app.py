from flask import Flask
from routes.notes import notes
from flask_sqlalchemy import SQLAlchemy
from utils.db import db

app = Flask(__name__)

app.secret_key = "secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/notes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#SQLAlchemy(app)
db.init_app(app)

app.register_blueprint(notes)

