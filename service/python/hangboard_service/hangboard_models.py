"""Data models for Hangboard"""

from marshmallow import fields, Schema


class TestResponse(Schema):
    """Test response"""

    message = fields.String()