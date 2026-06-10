from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.get("/test")
def auth_test(db: Session = Depends(get_db)):
    return {"message": "auth router working"}