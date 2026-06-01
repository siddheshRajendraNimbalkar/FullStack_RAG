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

from app.services.auth_service import (
    create_user,
    authenticate_user
)

from app.services.jwt_service import (
    create_access_token
)

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register")
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.username == request.username
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    user = create_user(
        db,
        request.username,
        request.password
    )

    token = create_access_token(
        str(user.id)
    )

    return {
        "access_token": token
    }


@router.post("/login")
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):

    user = authenticate_user(
        db,
        request.username,
        request.password
    )

    print(request.username)
    print(request.password)
    print(user)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        str(user.id)
    )

    return {
        "access_token": token
    }