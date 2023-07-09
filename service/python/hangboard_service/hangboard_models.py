"""Data models for Hangboard"""

from marshmallow import fields, Schema
from flask_rebar import RequestSchema


class TestResponse(Schema):
    """Test response"""

    message = fields.String()

####################
# Account Management
####################
class CreateAccountRequest(RequestSchema):
    """Request to create an account"""

    username = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)

class CreateAccountResponse(Schema):
    """Response to account creation"""

    success = fields.Boolean()
    message = fields.String()