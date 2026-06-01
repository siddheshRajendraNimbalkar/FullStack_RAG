from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.user import User

from app.schemas.auth import (
    RegisterRequest,
    LoginRequest
)

from app.core.security import (
    hash_password,
    verify_password
)

from app.services.auth_service import (
    create_access_token
)

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register")
def register(
    data: RegisterRequest,
    db: Session = Depends(get_db)
):

    existing = db.query(User)\
        .filter(
            User.username == data.username
        )\
        .first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    user = User(
        username=data.username,
        password=hash_password(
            data.password
        )
    )

    db.add(user)
    db.commit()

    return {
        "message": "registered"
    }


@router.post("/login")
def login(
    data: LoginRequest,
    db: Session = Depends(get_db)
):

    user = db.query(User)\
        .filter(
            User.username == data.username
        )\
        .first()

    if not user:
        raise HTTPException(
            status_code=401
        )

    if not verify_password(
        data.password,
        user.password
    ):
        raise HTTPException(
            status_code=401
        )

    token = create_access_token(
        str(user.id)
    )

    return {
        "access_token": token
    }