from jose import jwt
from jose import JWTError

from datetime import datetime
from datetime import timedelta

from app.core.config import (
    JWT_SECRET,
    JWT_EXPIRE_MINUTES
)

ALGORITHM = "HS256"


def create_access_token(
    user_id: str
):
    expire = datetime.utcnow() + timedelta(
        minutes=JWT_EXPIRE_MINUTES
    )

    payload = {
        "sub": user_id,
        "exp": expire
    }

    return jwt.encode(
        payload,
        JWT_SECRET,
        algorithm=ALGORITHM
    )


def verify_token(
    token: str
):
    try:
        payload = jwt.decode(
            token,
            JWT_SECRET,
            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:
        return None