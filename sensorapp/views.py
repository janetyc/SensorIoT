from flask import Blueprint, Flask, Response, request, render_template, redirect, url_for, jsonify
from sensorapp import app, env

views = Blueprint('views', __name__, template_folder='templates')

@views.route('/')
def index():
    return render_template('index.html', output="hi")

@views.route('/404')
def page_not_found():
    return render_template('404.html'), 404

@views.route('/400')
def bad_request():
    return render_template('400.html'), 400
