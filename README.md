# Attendance App (FastAPI + Redis + Celery)

A simple attendance management system built using FastAPI, Redis, Celery, Flower, and Docker.

---

## Prerequisites

Make sure you have the following installed:

- Docker
- Docker Compose (v2)

Verify:
```bash
docker --version
docker compose version
```
Project Structure
```
CRUD/
├── app/
│   ├── main.py
│   ├── celery_app.py
│   ├── tasks.py
│   ├── redis_client.py
│   ├── auth.py
│   └── routers/
│       ├── employee.py
│       └── attendance.py
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── .envRun the Application
```
From the directory where docker-compose.yml exists:

cd learn/CRUD
docker compose up --build

Service URLs
```
FastAPI Swagger UI: http://localhost:8000/docs

Flower (Celery Monitor): http://localhost:5555
```
How to Test (Using Swagger UI)
1. Create Admin (One Time)
```
POST /auth/bootstrap-admin
```

Admin credentials:
```
username: admin
password: admin123
```
2. Login as Admin

Swagger UI → Click Authorize

admin / admin123

3. Register an Employee
POST /employee/register


Example request body:
```
{
  "username": "Nilabh",
  "password": "Nilabh123",
  "role": "employee"
}
```

4. Login as Employee

Swagger UI → Click Authorize

Nilabh / Nilabh123

5. Employee Check-In
 ```
POST /attendance/check-in
```
6. Employee Check-Out
```   
POST /attendance/check-out
```
7. Admin View All Attendance

Login again as admin, then call:
```
GET /attendance/admin/all
```
Monitor Celery Tasks

Open Flower UI:
```
http://localhost:5555
```

Stop the Application

Stop containers:
```
docker compose down
```

Stop containers and remove Redis data:
```
docker compose down -v
```

