import os
from app.app import app, db
from flask import request, jsonify
from app.db import User


@app.route('/')
def index():
    return jsonify({'hello': 'Welcome to the world of tommorow!'})


@app.route('/users')
def users():
    data = [x.as_dictionary() for x in db.session.query(User).all()]
    return jsonify(data)


@app.route('/add_user')
def add_user():
    username = request.args.get('username', '')
    email = request.args.get('email', '')

    if not username:
        return jsonify({'msg': f'Please provide username'})

    if not email:
        return jsonify({'msg': f'Please provide email'})

    user = db.session.query(User).filter(User.username == username).first()
    if user:
        return jsonify({'msg': f'User with this username already exists'})

    user = db.session.query(User).filter(User.email == email).first()
    if user:
        return jsonify({'msg': f'User with this email already exists'})

    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()

    return jsonify({'msg': f'User {username} {email} added'})


@app.route('/delete_user')
def delete_user():
    id = request.args.get('id', '')
    if not id:
        return jsonify({'msg': f'Please provide id'})

    user = db.session.query(User).filter_by(User.id == id).first()
    db.session.delete(user)
    db.session.commit()
    return jsonify({'msg': f'User {user.name} {user.email} was deleted'})


@app.route('/enviroment_settings')
def enviroment_settings():
    dictionary = {}
    dictionary['NODE_ENV'] = os.environ.get('NODE_ENV', '')
    dictionary['DB_HOST'] = os.environ.get('DB_HOST', '')
    dictionary['DB_PORT'] = os.environ.get('DB_PORT', '')
    dictionary['DB_USER'] = os.environ.get('DB_USER', '')
    dictionary['DB_PASSWORD'] = os.environ.get('DB_PASSWORD', '')
    dictionary['DB_NAME'] = os.environ.get('DB_NAME', '')
    return jsonify(dictionary)
