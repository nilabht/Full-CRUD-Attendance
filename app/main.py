from fastapi import FastAPI
from app.routers import auth, employee, attendance

app = FastAPI(title="Attendance App")

app.include_router(auth.router)
app.include_router(employee.router)
app.include_router(attendance.router)
