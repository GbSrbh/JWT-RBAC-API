print("User route loaded")

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from ..app.token import JWTHandler
from ..db.db_connection import get_db
from ..app.dtos import (
    SignupRequest,
    SignupResponse,
    LoginRequest,
    Token
)
from ..app.auth import PasswordHandler
from ..db.models import User

router = APIRouter()


@router.post("/register", response_model=SignupResponse)
def register(user: SignupRequest, db: Session = Depends(get_db)):
    existing_user = db.exec(select(User).where(User.username == user.username)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    password_handler = PasswordHandler()
    hashed_password = password_handler.hash_password(user.password)
    db_user = User(
        username=user.username,
        hashed_password=hashed_password,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.post("/login", response_model=Token)
def login(form_data: LoginRequest, db: Session = Depends(get_db)):
    user = db.exec(select(User).where(User.username == form_data.username)).first()

    password_handler = PasswordHandler()
    jwt_handler = JWTHandler()
    if not user or not password_handler.verify_password(password=form_data.password, hashed_password=user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect credentials")

    access_token = jwt_handler.generate_access_token(
        token_data={"sub": user.username, "role": user.role}
    )
    return {"access_token": access_token, "token_type": "bearer"}
