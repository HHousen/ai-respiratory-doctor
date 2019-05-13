from flask import render_template, jsonify, Blueprint
from app import app
import random
from app.decorators import *

mainbp = Blueprint('mainbp', __name__)

@mainbp.route('/')
@mainbp.route('/index')
def index():
    return render_template('index.html', title='Home')

@mainbp.route('/map')
def map():
    return render_template('map.html', title='Map')


@mainbp.route('/map/refresh', methods=['POST'])
def map_refresh():
    points = [(random.uniform(48.8434100, 48.8634100),
               random.uniform(2.3388000, 2.3588000))
              for _ in range(random.randint(2, 9))]
    return jsonify({'points': points})


@mainbp.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')
