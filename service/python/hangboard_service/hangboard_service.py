"""REST endpoints for Hangboard"""
from logging import Logger, INFO

from flask_rebar import errors, Rebar, SwaggerV3Generator

from .account.account_manager import AccountManager
from .hangboard_models import (
    TestResponse,
    CreateAccountRequest,
    CreateAccountResponse
)

logger = Logger("Hangboard.service")
logger.setLevel(INFO)


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

# GLOBAL OBJECTS
account_manager = AccountManager()


@registry.handles(
    rule="/hello",
    method="GET",
    response_body_schema={200: TestResponse()}
)
def get_hello():
    """Return the test response"""
    return {"message": "hello world!!"}


@registry.handles(
    rule="/join",
    method="POST",
    request_body_schema=CreateAccountRequest(),
    response_body_schema={200: CreateAccountResponse()}
)
def create_account():
    body = rebar.validated_body
    username = body["username"]
    email = body["email"]
    password = body["password"]

    try:
        account_manager.add_user(username, email, password)
        logger.info(f"Successfully created account for {username}")
        return {"success": True, "message": ""}
    except ValueError as e:
        logger.error(f"Error creating account: {e}")
        return {"success": False, "message": str(e)}