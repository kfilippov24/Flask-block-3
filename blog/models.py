from flask_bcrypt (check_password_hash, # type: ignore
                  generate_password_hash) # type: ignore
from flask_login import UserMixin

from blog import db, bcrypt

class User(db.User,UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20), nullable=False)

    def set_password(self, password, hashed_password):
        self.hashed_password = bcrypt.generate_password_hash(
            password
        ).decode('utf-8')

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password) # type: ignore
    
    def __repr__(self):
        return f'User({self.name},{self.email},{self.password})'



