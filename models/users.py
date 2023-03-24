from dataclasses import dataclass

from extensions import db


@dataclass
class User(db.Model):
    id: int
    name: str
    email: str
    age: int

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String, nullable=False)
