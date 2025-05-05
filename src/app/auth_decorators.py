from fastapi import Request
from functools import wraps
from .token import JWTHandler
from ..exceptions import NoTokenFoundError, UserNotAdminError

jwt_handler = JWTHandler()

def extract_and_decode_token(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise NoTokenFoundError(message="Authentication failed, no token found in request")

    token = auth_header.split(" ")[1]
    payload = jwt_handler.decode_access_token(token)

    return payload

def auth_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        request: Request = kwargs.get("request")

        payload = extract_and_decode_token(request=request)
        request.state.user = payload

        return fn(*args, **kwargs)
    return wrapper


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        request: Request = kwargs.get("request")

        payload = extract_and_decode_token(request=request)

        if payload.get("role") != "ADMIN":
            raise UserNotAdminError(message="User is not admin, route restricted only for admins.")

        request.state.user = payload
        return fn(*args, **kwargs)
    return wrapper
