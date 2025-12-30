from datetime import datetime
from app.celery_app import celery
from app.redis_client import redis_client


@celery.task(name="attendance.check_in")
def attendance_check_in(username: str):
    today = datetime.now().date().isoformat()
    key = f"attendance:{username}:{today}"

    redis_client.hset(
        key,
        mapping={
            "check_in": datetime.now().isoformat(),
            "check_out": "",
            "total_hours": 0
        }
    )

    return f"{username} checked in"


@celery.task(name="attendance.check_out")
def attendance_check_out(username: str):
    today = datetime.now().date().isoformat()
    key = f"attendance:{username}:{today}"

    data = redis_client.hgetall(key)
    if not data or not data.get("check_in"):
        return "No check-in found"

    check_in_time = datetime.fromisoformat(data["check_in"])
    check_out_time = datetime.now()

    total_hours = round(
        (check_out_time - check_in_time).seconds / 3600,
        2
    )

    redis_client.hset(
        key,
        mapping={
            "check_out": check_out_time.isoformat(),
            "total_hours": total_hours
        }
    )

    return f"{username} checked out"
