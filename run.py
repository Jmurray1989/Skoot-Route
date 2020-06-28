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

# Page renders


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
    return render_template('addroute.html', routes=mongo.db.routes.find())


@app.route('/publicroutes')
def publicroutes():
    """Public Routes page render"""
    return render_template('publicroutes.html', routes=mongo.db.routes.find())


@app.route('/mobile')
def mobile():
    """Mobile page render"""
    return render_template('mobile.html')

# Add, Edit & Delete Routes


@app.route('/insert_route', methods=['POST'])
def insert_route():
    """Adds Your Route To Public Route Page"""
    routes = mongo.db.routes
    routes.insert_one(request.form.to_dict())
    return redirect(url_for('publicroutes'))


@app.route('/edit_route/<route_id>')
def edit_route(route_id):
    """Edits Your Route on the Public Route Page"""
    the_route = mongo.db.routes.find_one({"_id": ObjectId(route_id)})
    return render_template('editroute.html', route=the_route)


@app.route('/update_route/<route_id>', methods=["POST"])
def update_route(route_id):
    """Updates Your Route on the Public Route Page"""
    route = mongo.db.routes
    route.replace_one({'_id': ObjectId(route_id)}, {
        'person_name': request.form.get('person_name'),
        'route_name': request.form.get('route_name'),
        'map_link': request.form.get('map_link'),
        'route_description': request.form.get('route_description')
    })
    return redirect(url_for('publicroutes'))


@app.route('/delete_route/<route_id>')
def delete_route(route_id):
    """Deletes Your Route from the Public Route Page"""
    mongo.db.routes.remove({'_id': ObjectId(route_id)})
    return redirect(url_for('publicroutes'))


# Error Handling of 404 & 500

@app.errorhandler(404)
def page_error(error):
    """Custom 404 error page displayed when captured"""
    return render_template("404.html"), 404


@app.errorhandler(500)
def error_500(error):
    """Custom 500 error page displayed when captured"""
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
