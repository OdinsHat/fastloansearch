from flask import Flask, request, session, g, redirect, url_for, abort, render_template
import requests
from database import db_session
from models import Result, Product
from key import GOOGLEKEY, CSE, AWINID, MIDS

app = Flask(__name__)
app.config.from_object(__name__)

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

    results = search_google(("%s loans" % (type)), page)
    save_results(results, type)
    
    return render_template(
        'loan_results.html',
        data=results,
        type=type,
        related=allowed_types,
        page=int(page),
        mids = MIDS
    )


@app.route('/cards/<type>')
@app.route('/cards/<type>/<page>')
def credit_cards(type='all', page=1):
    """Credit cards search"""
    allowed_types = ('cashback', 'bad_credit', '0 purchases', 'prepaid', 'all')
    if type not in allowed_types:
        abort(404, "Unknown credit card type")

    results = search_google("%s credit cards" % (type), page)
    if results.reason is 'OK':
        save_results(results, type)
    else:
        get_results('card', type)

    return render_template(
        'card_results.html',
        data=results,
        type=type,
        related=allowed_types,
        page=int(page)
    )

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html', error=error)


@app.route('/tools/loan_calculator')
def loan_calculator():
    return render_template('tools/loan_calculator.html')


@app.route('/privacy')
def page_privacy():
    return render_template('privacy.html')


@app.route('/copyright')
def page_copyright():
    return render_template('copyright.html')


@app.route('/about')
def page_about():
    return render_template('about.html')


def search_google(query, page):
    requesturl = "https://www.googleapis.com/customsearch/v1"
    cse = CSE
    apikey = GOOGLEKEY
    fullurl = "%s?cx=%s&key=%s&q=%s&filter=1" % (requesturl, cse, apikey, query)
    if page > 1:
        fullurl += "&start=%s&num=10" % ((int(page)-1) * 10)
    print fullurl
    return requests.get(fullurl).json()


def save_results(results, type):
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


def get_results(section, type):
    pass
    #results = Result.query.filter(Result.type == type).group_by('displaylink').all()[:10]


if __name__ == '__main__':
    app.run()
