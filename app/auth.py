from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from app.redis_client import redis_client

security = HTTPBasic()


def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    user_key = f"user:{credentials.username}"
    user = redis_client.hgetall(user_key)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )

    if user["password"] != credentials.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid password"
        )

    return {
        "username": credentials.username,
        "role": user["role"]
    }
