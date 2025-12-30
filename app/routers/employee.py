from fastapi import APIRouter, Depends, HTTPException
from app.auth import get_current_user
from app.redis_client import redis_client
from app.models import UserCreate

router = APIRouter(prefix="/employee", tags=["Employee"])


@router.post("/register")
def register_employee(
    user: UserCreate,
    current_user=Depends(get_current_user)
):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admin only")

    key = f"user:{user.username}"

    if redis_client.exists(key):
        raise HTTPException(status_code=400, detail="User exists")

    redis_client.hset(
        key,
        mapping={
            "password": user.password,
            "role": user.role
        }
    )

    return {"message": "User registered successfully"}
