from flask import Flask, request, session, g, redirect, url_for, abort, render_template
import requests
from database import db_session
from models import Result, Product
from random import randrange
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
    allowed_types = ('secured', 'personal', 'bad credit', 'car', 'holiday', 'wedding', 'unsecured')
    if type not in allowed_types:
        abort(404, "Unknown loan type")

    showsponsored = randrange(1,10)

    if randrange(1,10) > 5:
        source='google'
        results = search_google(("%s loans" % (type)), page)
        save_results(results, type)
    else:
        source='db'
        results = get_results(type)
        if not results:
            results = search_google(("%s loans" % (type)), page)
            save_results(results, type)
            source='google'

    return render_template(
        'loan_results.html',
        data=results,
        source=source,
        type=type.replace('+', ' '),
        related=allowed_types,
        page=int(page),
        mids = MIDS,
        showsponsored=showsponsored
    )

@app.route('/goto/<mid>')
@app.route('/goto/<mid>/<clickref>')
def goto_merchant(mid=None, clickref=None):
    url = ("http://www.awin1.com/awclick.php?mid=%s&id=%s" % (mid, AWINID))
    return redirect(url, 302)

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
            result['title'].strip(),
            result['htmlTitle'].strip(),
            result['link'].strip(),
            result['displayLink'].strip(),
            result['snippet'].strip(),
            result['htmlSnippet'].strip(),
            result['formattedUrl'].strip(),
            result['htmlFormattedUrl'].strip(),
            type.strip()
        )
        db_session.add(r)
        db_session.commit()

def get_results(product_type):
    results = Result.query.filter_by(type=product_type).group_by('displaylink').all()[:10]
    if len(results) < 10:
        return None
    return results


if __name__ == '__main__':
    app.run()
