import os
import json

from flask import Flask, Response, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from pprint import pprint

import db.credentials as credentials

db = SQLAlchemy()

def create_app():
    from api.search_service import SearchService
    template_dir = os.path.abspath('../frontend/')
    app = Flask(__name__, template_folder=template_dir, static_folder='../frontend/public')
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://" + credentials.db['user'] + ":" + credentials.db['password'] + "@" + credentials.db['hostname'] + "/" + credentials.db['name']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    @app.route('/search')
    def search():
        search_service = SearchService(db)
        results = search_service.find_recipe(request.args.get('keywords'), 4)
        return json.dumps(results)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/searchbyingredient')
    def searchbyingredient():
        search_service = SearchService(db)
        results = search_service.find_recipe_by_ingredient(request.args.get('keywords'), 4)
        return json.dumps(results)

    @app.route('/<path:path>')
    def catch_all(path):
        return render_template('index.html')

    return app
