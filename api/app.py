
from flask import Flask
from core.external.authorization_modules.authorize_base import AuthorizationException
from core.services.exceptions import ResourceExistedException, ResourceNotFoundException

from apis import api
from apis.error_handlers import handle_exception
from apis.exceptions import IdentityNotMatchException,DataValidationException
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from flask_cors import CORS
from flask_restx._http import HTTPStatus

load_dotenv()

app = Flask(__name__)

api.init_app(app)
CORS(app)

app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)


@api.errorhandler(AuthorizationException)
def handle_root_exception(error):
    return handle_exception(error, HTTPStatus.FORBIDDEN)


@api.errorhandler(ResourceExistedException)
def handle_custom_exception(error):
    return handle_exception(error, HTTPStatus.BAD_REQUEST)


@api.errorhandler(ResourceNotFoundException)
def handle_another_exception(error):
    return handle_exception(error, HTTPStatus.NOT_FOUND)

@api.errorhandler(DataValidationException)
def handle_another_exception(error):
    return handle_exception(error, HTTPStatus.BAD_REQUEST)

@api.errorhandler(IdentityNotMatchException)
def handle_another_exception(error):
    return handle_exception(error, HTTPStatus.FORBIDDEN)



@jwt.token_verification_failed_loader
def token_verification_failed(jwt_header, jwt_payload):
    return handle_exception(AuthorizationException("Fail to verify token"), HTTPStatus.UNAUTHORIZED)

@jwt.expired_token_loader
def expired_token(jwt_header, jwt_payload):

    return handle_exception(AuthorizationException("Token has expired"), HTTPStatus.UNAUTHORIZED)

@jwt.unauthorized_loader
def unauthorized(explanation):
    return handle_exception(AuthorizationException(f"Missing Authorization header. {explanation}"), HTTPStatus.UNAUTHORIZED)


@jwt.invalid_token_loader
def unauthorized(reason):
    return handle_exception(AuthorizationException(f"Invalid token. {reason }"), HTTPStatus.UNAUTHORIZED)

app.config["ERROR_INCLUDE_MESSAGE"] = False
# print(api.as_postman())
if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
