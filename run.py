import os
from flask import Flask, render_template, redirect, request, url_for


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    """Home page render"""
    return render_template('index.html')


@app.route('/about')
def about():
    """About page render"""
    return render_template('about.html')


@app.route('/skoot')
def skoot():
    """Skoot Route page render"""
    return render_template('skootroute.html')


@app.route('/mobile')
def mobile():
    """Mobile page render"""
    return render_template('mobile.html')    


@app.route('/skoot')
def skoot_button():
    """Button re-direct on homepage"""
    return redirect(url_for('skoot'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
