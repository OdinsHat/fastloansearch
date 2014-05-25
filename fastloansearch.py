from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DEBUG=True,
    SECRET_KEY = 'uytjytfuytviti7f8tvwkuvfigy348u'
))

toolbar = DebugToolbarExtension(app)