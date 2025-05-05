from fastapi import HTTPException

class InvalidCredentialsError(HTTPException):
    def __init__(self, message: str = "Invalid username or password"):
        super().__init__(status_code=401, detail=message)

class InvalidTokenError(HTTPException):
    def __init__(self, message: str = "Provided token is invalid."):
        super().__init__(status_code=401, detail=message)

class NoTokenFoundError(HTTPException):
    def __init__(self, message: str = "Authentication token not provided"):
        super().__init__(status_code=401, detail=message)

class NotAdminUserError(HTTPException):
    def __init__(self, message: str = "Forbidden, user not admin"):
        super().__init__(status_code=403, detail=message)

class UserAlreadyExistsError(HTTPException):
    def __init__(self, message: str = "User already exists"):
        super().__init__(status_code=400, detail=message)

class UserNotFoundError(HTTPException):
    def __init__(self, message: str = "User not found"):
        super().__init__(status_code=404, detail=message)
