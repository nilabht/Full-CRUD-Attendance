from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    username: str
    password: str
    role: str  # admin or employee


class AttendanceResponse(BaseModel):
    check_in: Optional[str]
    check_out: Optional[str]
    total_hours: Optional[float]
