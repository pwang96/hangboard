"""Hangboard app"""

from logging import Logger

from flask import Flask, url_for, redirect
from flask_cors import CORS, cross_origin

from .hangboard_service import rebar


app = Flask("Hangboard")
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
logger = Logger(app.logger.name)
# Sync rebar to the Flask app and set up Swagger UI
rebar.init_app(app)


@app.route("/swagger")
def redirect_to_swagger():
    """Redirect to Swagger UI"""
    return redirect(url_for("apiswagger_ui.show"))
