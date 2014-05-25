from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify
import requests
from flask_debugtoolbar import DebugToolbarExtension
from database import db_session
from models import Result, Product

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DEBUG=True,
    SECRET_KEY = 'uytjytfuytviti7f8tvwkuvfigy348u'
))

toolbar = DebugToolbarExtension(app)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/')
def homepage():
    """Main (very basic) homepage"""
    return render_template('homepage.html')

@app.route('/loans/<type>')
def loans_search(type):
    pass

@app.route('/cards/<type>')
def loans_search(type):
    pass

### /Searches ###

### Pages ###

@app.route('/privacy')
def page_privacy():
    return render_template('privacy.html')

@app.route('/copyright')
def page_copyright():
    return render_template('copyright.html')

@app.route('/about')
def page_about():
    return render_template('about.html')

### /Pages ###
