import os
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db_host = os.environ.get("DB_HOST", "")
db_port = os.environ.get("DB_PORT", "")
db_user = os.environ.get("DB_USER", "")
db_pass = os.environ.get("DB_PASSWORD", "")
db_name = os.environ.get("DB_NAME", "")

if db_name:
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}"
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
