from fastapi import APIRouter, Depends, HTTPException
from app.auth import get_current_user
from app.celery_app import celery
from app.redis_client import redis_client

router = APIRouter(prefix="/attendance", tags=["Attendance"])


@router.post("/check-in")
def check_in(current_user=Depends(get_current_user)):
    celery.send_task(
        "attendance.check_in",
        args=[current_user["username"]]
    )
    return {"message": "Check-in task queued"}


@router.post("/check-out")
def check_out(current_user=Depends(get_current_user)):
    celery.send_task(
        "attendance.check_out",
        args=[current_user["username"]]
    )
    return {"message": "Check-out task queued"}

@router.get("/admin/all")
def view_all_attendance(current_user=Depends(get_current_user)):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admin only")

    keys = redis_client.keys("attendance:*")
    return {key: redis_client.hgetall(key) for key in keys}
