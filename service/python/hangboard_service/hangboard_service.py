"""REST endpoints for Hangboard"""
from logging import Logger

from flask_rebar import errors, Rebar, SwaggerV3Generator


from .hangboard_models import TestResponse

logger = Logger("Hangboard.service")


rebar = Rebar()
# Registry object allows making API request handlers that auto-generate for Swagger
registry = rebar.create_handler_registry(
    prefix="api",  # All APIs under this prefix
    swagger_generator=SwaggerV3Generator(),
    spec_path="swagger.json",  # Open API specification at /api/swagger.json
    swagger_ui_path="swagger",  # Navigate to /api/swagger
)
swagger_gen = registry.swagger_generator
swagger_gen.title = "Hangboard"
swagger_gen.description = "Hangboard hard!!!!"


@registry.handles(
    rule="/hello",
    method="GET",
    response_body_schema={200: TestResponse()}
)
def get_hello():
    """Return the test response"""
    return {"message": "hello world!!"}