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
    return render_template('about.html')


@app.route('/skoot')
def skoot():
    return render_template('skootroute.html')


@app.route('/skoot')
def skoot_button():
    return redirect(url_for('skoot'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
