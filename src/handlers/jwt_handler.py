import os
import jwt
import datetime

from FastAPI_PostgreSQL.src.exceptions import InvalidTokenError

class JWTHandler:
    def __init__(self) -> None:
        self.secret_key = os.environ.get("JWT_SECRET_KEY", "")
        if not self.secret_key:
            raise EnvironmentError("No secret key found for generating jwts in environment file.")
        self.algorithm = os.environ.get("JWT_ALGORITHM", "HS256")
        self.token_expiry_time = int(os.environ.get("TOKEN_EXPIRY_TIME_IN_MINUTES", "15"))

    def generate_access_token(self, token_data: dict) -> str:
        payload = token_data.copy()
        expire_time = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=self.token_expiry_time)
        payload.update({"exp": expire_time})
        encoded_jwt = jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt

    def decode_access_token(self, access_token: str) -> dict:
        try:
            payload = jwt.decode(access_token, self.secret_key, algorithms=[self.algorithm])
        except Exception as e:
            raise InvalidTokenError("Token validation failed: %s " % str(e))
        else:
            return payload
