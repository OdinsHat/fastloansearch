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
@app.route('/loans/<type>/<page>')
def loans_search(type, page=1):
    """Loans search"""
    allowed_types = ('secured', 'unsecured', 'payday', 'car', 'holiday')
    if type not in allowed_types:
        abort(404, "Unknown loan type")

    cse = "008208809341786190865:lstx_fuuzog"
    query = "%s loans" % (type)
    apikey = "AIzaSyChRMCztfdN94uJWfHhaPUhQh102uMFV_k"
    requesturl = "https://www.googleapis.com/customsearch/v1"
    fullurl = "%s?cx=%s&key=%s&q=%s&filter=1" % (requesturl, cse, apikey, query)
    if page > 1:
        fullurl += "&start=11&num=10"

    data = requests.get(fullurl)

    results = data.json()

    for result in results['items']:
        r = Result(
            result['title'],
            result['htmlTitle'],
            result['link'],
            result['displayLink'],
            result['snippet'],
            result['htmlSnippet'],
            result['formattedUrl'],
            result['htmlFormattedUrl'],
            type
        )
        db_session.add(r)
        db_session.commit()
    
    return render_template(
        'loan_results.html',
        data=results,
        type=type,
        related=allowed_types,
        page=int(page)
    )

@app.route('/cards/<type>')
def credit_cards(type='all'):
    """Credit cards search"""
    allowed_types = ('cashback', 'bad_credit', '0 purchases', 'prepaid', 'all')
    if type not in allowed_types:
        abort(404, "Unknown credit card type")

    results = search_google("%s credit cards" % (type))

    return render_template('card_results.html', data=results, type=type, related=allowed_types)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html', error=error)

### Finance Tools ###

@app.route('/tools/loan_calculator')
def loan_calculator():
    return render_template('tools/loan_calculator.html')


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
