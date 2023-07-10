"""Data models for Hangboard"""

from marshmallow import fields, Schema
from flask_rebar import RequestSchema
from werkzeug import Request


class TestResponse(Schema):
    """Test response"""

    message = fields.String()


####################
# Account Management
####################
class CreateAccountRequest(RequestSchema):
    """Request to create an account"""

    username = fields.String(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)


class CreateAccountResponse(Schema):
    """Response to account creation"""

    success = fields.Boolean(required=True)
    message = fields.String()


class LoginRequest(RequestSchema):
    """Request to login"""

    username = fields.String(required=True)
    password = fields.String(required=True)


class LoginResponse(Schema):
    """Response to login"""

    success = fields.Boolean(required=True)


class User(Schema):
    """User"""

    username = fields.String(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.Email(required=True)


class Users(Schema):
    """List of users"""

    users = fields.List(fields.Nested(User), required=True)
