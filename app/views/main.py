from flask import render_template, jsonify, Blueprint
from app import app
import random
import datetime as dt
from app.extensions import db
from app.decorators import *

mainbp = Blueprint('mainbp', __name__)

@mainbp.route('/')
@mainbp.route('/index')
def index():
    return render_template('index.html', title='Home')

@mainbp.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = dt.datetime.utcnow()
        db.session.commit()