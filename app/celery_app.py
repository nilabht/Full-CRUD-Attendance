from celery import Celery

celery = Celery(
    "attendance_app",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)
celery.autodiscover_tasks(["app"])
celery.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Asia/Kolkata",
    enable_utc=True
)

