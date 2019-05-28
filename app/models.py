from sqlalchemy.ext.hybrid import hybrid_property
from flask_login import UserMixin

from app.extensions import db, bcrypt
import datetime as dt
from hashlib import md5

class User(db.Model, UserMixin):

    ''' A user who has an account on the website. '''

    __tablename__ = 'users'

    first_name = db.Column(db.String(30), nullable=True)
    last_name = db.Column(db.String(30), nullable=True)
    phone = db.Column(db.String(30), nullable=True)
    email = db.Column(db.String(80), primary_key=True, unique=True, nullable=False)
    confirmation = db.Column(db.Boolean(), nullable=False, default=False)
    created_at = db.Column(db.DateTime(), nullable=True, default=dt.datetime.utcnow)
    last_seen = db.Column(db.DateTime(), default=dt.datetime.utcnow)
    credits = db.Column(db.Integer(), nullable=True, default=0)
    customer_id = db.Column(db.String(40), nullable=True)
    _password = db.Column(db.Binary(60), nullable=False)

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    def check_password(self, plaintext):
        return bcrypt.check_password_hash(self.password, plaintext)

    def get_id(self):
        return self.email

    def get_credits(self):
        return self.credits
    
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)