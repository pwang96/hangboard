"""REST endpoints for Hangboard"""
from logging import Logger, INFO

from flask_rebar import errors, Rebar, SwaggerV3Generator

from .account.account_manager import AccountManager
from .hangboard_models import (
    LoginRequest,
    LoginResponse,
    TestResponse,
    CreateAccountRequest,
    CreateAccountResponse,
    Users,
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
    rule="/hello", method="GET", response_body_schema={200: TestResponse()}
)
def get_hello():
    """Return the test response"""
    return {"message": "hello world!!"}


@registry.handles(
    rule="/join",
    method="POST",
    request_body_schema=CreateAccountRequest(),
    response_body_schema={200: CreateAccountResponse()},
)
def create_account():
    body = rebar.validated_body
    username = body["username"]
    email = body["email"]
    first_name = body["first_name"]
    last_name = body["last_name"]
    password = body["password"]

    try:
        account_manager.add_user(username, first_name, last_name, email, password)
        logger.info(f"Successfully created account for {username}")
        return {"success": True, "message": ""}
    except ValueError as e:
        logger.error(f"Error creating account: {e}")
        return {"success": False, "message": str(e)}


@registry.handles(
    rule="/login",
    method="POST",
    request_body_schema=LoginRequest(),
    response_body_schema={200: LoginResponse()},
)
def login():
    body = rebar.validated_body
    username = body["username"]
    password = body["password"]

    try:
        success = account_manager.login(username, password)
        if not success:
            logger.info(f"Incorrect password entered for {username}")
            raise errors.Forbidden(msg=f"Incorrect password for {username}")
        logger.info(f"Successfully logged in {username}")
        return {"success": True}
    except ValueError as e:
        logger.error(f"Error logging in {username}: {e}")
        raise errors.Forbidden(msg=f"{username} does not exist in the system")


@registry.handles(rule="/users", method="GET", response_body_schema={200: Users()})
def get_users():
    users = []
    print(account_manager.users)
    for user in account_manager.users.values():
        users.append(
            {
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
            }
        )

    return {"users": users}
