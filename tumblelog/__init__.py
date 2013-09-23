# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "tumblelog"}
app.config["SECRET_KEY"] = "ak!U!&alak12amI&Naj"

db = MongoEngine(app)

def register_blueprints(app):
    from tumblelog.views import posts
    app.register_blueprint(posts)

register_blueprints(app)

if __name__ == '__main__':
    app.run()
