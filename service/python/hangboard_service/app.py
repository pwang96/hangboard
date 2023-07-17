"""Hangboard app"""

from typing import Optional
from logging import Logger

import jwt
from flask import Flask, url_for, redirect, request, g
from flask_cors import CORS, cross_origin

from .hangboard_service import rebar, JWT_SECRET_KEY, JWT_ALGORITHM, account_manager


app = Flask("Hangboard")
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
logger = Logger(app.logger.name)
# Sync rebar to the Flask app and set up Swagger UI
rebar.init_app(app)


@app.before_request
def decode_jwt_if_exists() -> None:
    """Decode the JWT into the dictionary if it exists in the header"""
    auth_header = request.headers.get("Authorization", "").strip().strip(",")
    print(f"AUTH HEADER: {auth_header}")
    if len(auth_header) == 0:
        g.user = None
        return

    header_parts = auth_header.strip().split(" ")
    if header_parts[0].strip() != "Bearer":
        logger.warn("Authorization header has the wrong format.")
        g.user = None
        return

    decoded_jwt = jwt.decode(
        header_parts[1], JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM]
    )
    g.user = account_manager.get_user_by_username(decoded_jwt["username"])


@app.route("/swagger")
def redirect_to_swagger():
    """Redirect to Swagger UI"""
    return redirect(url_for("apiswagger_ui.show"))
