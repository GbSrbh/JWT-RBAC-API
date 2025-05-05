from fastapi import Request
from functools import wraps
from .token import JWTHandler
from ..exceptions import NoTokenFoundError, NotAdminUserError

jwt_handler = JWTHandler()

def auth_required(fn):
    @wraps(fn)
    async def wrapper(*args, **kwargs):
        request: Request = kwargs.get("request")

        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            raise NoTokenFoundError(message="Authentication failed, no token found in request")

        token = auth_header.split(" ")[1]

        payload = jwt_handler.decode_access_token(token)
        request.state.user = payload

        return await fn(*args, **kwargs)
    return wrapper


def admin_required(fn):
    @wraps(fn)
    async def wrapper(*args, **kwargs):
        request: Request = kwargs.get("request")

        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            raise NoTokenFoundError(message="Authentication failed, no token found in request")

        token = auth_header.split(" ")[1]
        payload = jwt_handler.decode_access_token(token)

        if payload.get("role") != "admin":
            raise NotAdminUserError(message="User is not admin, route restricted only for admins.")

        request.state.user = payload
        return await fn(*args, **kwargs)
    return wrapper
