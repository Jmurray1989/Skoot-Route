import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")


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


@app.route('/routes')
def routes():
    """Skoot Routes page render"""
    return render_template("routes.html")


@app.route('/addroute')
def addroute():
    """Add route page render"""
    return render_template('addroute.html')


@app.route('/publicroutes')
def publicroutes():
    """Public Routes page render"""
    return render_template('publicroutes.html', 
    routes=mongo.db.tasks.find())


@app.route('/mobile')
def mobile():
    """Mobile page render"""
    return render_template('mobile.html')


@app.route('/get_routes')
def get_routes():
    return render_template("routes.html")    


@app.route('/add_route')
def add_route():
    """Add Route"""
    return render_template('addroute.html',
    routes=mongo.db.routes.find())


@app.route('/insert_route', methods=['POST'])
def insert_route():
    routes = mongo.db.routes
    routes.insert_one(request.form.to_dict())
    return redirect(url_for('get_routes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
