from fastapi import APIRouter
from app.redis_client import redis_client

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/bootstrap-admin")
def create_admin():
    """
    One-time admin creation
    """
    redis_client.hset(
        "user:admin",
        mapping={
            "password": "admin123",
            "role": "admin"
        }
    )
    return {"message": "Admin created"}
