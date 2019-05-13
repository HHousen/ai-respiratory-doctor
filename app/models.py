from sqlalchemy.ext.hybrid import hybrid_property
from flask_login import UserMixin

from app.extensions import db, bcrypt
import datetime as dt

class User(db.Model, UserMixin):

    ''' A user who has an account on the website. '''

    __tablename__ = 'users'

    first_name = db.Column(db.String(30), nullable=True)
    last_name = db.Column(db.String(30), nullable=True)
    phone = db.Column(db.String(30), nullable=True)
    email = db.Column(db.String(80), primary_key=True, unique=True, nullable=False)
    confirmation = db.Column(db.Boolean(), nullable=False, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    paid = db.Column(db.Boolean(), nullable=False, default=False)
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

    def is_paid(self):
        return self.paid