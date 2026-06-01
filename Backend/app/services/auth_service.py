from jose import jwt
from datetime import datetime
from datetime import timedelta
import os

SECRET = os.getenv("JWT_SECRET")

ALGORITHM = "HS256"


def create_access_token(
    user_id: str
):
    payload = {
        "sub": user_id,
        "exp": datetime.utcnow()
        + timedelta(days=1)
    }

    return jwt.encode(
        payload,
        SECRET,
        algorithm=ALGORITHM
    )