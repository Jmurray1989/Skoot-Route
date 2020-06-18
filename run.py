import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 


app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.getenv('MONGO_DBNAME', 'mongodb://localhost')
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')


mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    """Home page render"""
    return render_template('index.html')


@app.route('/about')
def about():
    """About page render"""
    return render_template('about.html')


@app.route('/skootroutes')
def skoot_routes():
    return render_template("skootroute.html", my_routes=mongo.db.my_routes.find())


@app.route('/mobile')
def mobile():
    """Mobile page render"""
    return render_template('mobile.html')


@app.route('/skootroutes')
def skoot_button():
    """Button re-direct on homepage"""
    return redirect(url_for('skootroutes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
