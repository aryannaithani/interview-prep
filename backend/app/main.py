from fastapi import FastAPI
from app.schemas.user import UserCreate
from app.api.auth import router as auth_router

app = FastAPI(title="PrepForge API")

app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "PrepForge API is running"}

@app.post("/test")
def test_user(user: UserCreate):
    return user