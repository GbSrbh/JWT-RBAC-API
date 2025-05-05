from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from ..handlers.jwt_handler import JWTHandler
from ..db.db_connection import get_db
from ..dtos import (
    SignupRequest,
    SignupResponse,
    LoginRequest,
    Token,
)
from ..enums import Role
from ..handlers.password_handler import PasswordHandler
from ..db.models import User
from ..exceptions import UserAlreadyExistsError, InvalidRoleError, UserNotFoundError, InvalidCredentialsError

router = APIRouter()

USER_ROLE = {
    "user": Role.USER,
    "admin": Role.ADMIN
}

@router.post("/register", response_model=SignupResponse)
def register(user: SignupRequest, db: Session = Depends(get_db)):
    existing_user = db.exec(select(User).where(User.username == user.username)).first()
    if existing_user:
        raise UserAlreadyExistsError(message="User with this username already exists")

    password_handler = PasswordHandler()
    hashed_password = password_handler.hash_password(user.password)
    try:
        role = USER_ROLE[user.role]
    except KeyError:
        raise InvalidRoleError("Provided role is not supported")

    db_user = User(
        username=user.username,
        password=hashed_password,
        role=role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.post("/login", response_model=Token)
def login(form_data: LoginRequest, db: Session = Depends(get_db)):
    user = db.exec(select(User).where(User.username == form_data.username)).first()
    if not user:
        raise UserNotFoundError(message="No such user exists")

    password_handler = PasswordHandler()
    jwt_handler = JWTHandler()

    is_password_correct = password_handler.verify_password(password=form_data.password, hashed_password=user.password)
    if not is_password_correct:
        raise InvalidCredentialsError(message="Incorrect credentials")

    access_token = jwt_handler.generate_access_token(
        token_data={"sub": user.username, "role": user.role.value}
    )
    return {"access_token": access_token, "token_type": "bearer"}
