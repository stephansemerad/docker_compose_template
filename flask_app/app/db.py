# from app import app, db
from sqlalchemy import or_, cast, desc, func
from sqlalchemy import desc, func, distinct, and_

from app.app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def as_dictionary(self):
        dictionary = {}
        for column in self.__table__.columns:
            atrribute = getattr(self, column.name)
            dictionary[column.name] = "" if not atrribute else atrribute
        return dictionary


db.create_all()


users = [{'username': 'admin', 'email': 'admin@example.com'},
         {'username': 'guest', 'email': 'guest@example.com'}, ]

for i in users:
    check = (
        db.session.query(User).
        filter(User.username == i['username']).
        first()
    )
    if not check:
        user = User(username=i['username'], email=i['email'])
        db.session.add(user)
        db.session.commit()
