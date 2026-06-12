from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.user import UserCreate, UserResponse, UserLogin
from app.services.user_service import create_user, get_user_by_email, get_user_by_username, authenticate_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.get("/test")
def auth_test(db: Session = Depends(get_db)):
    return {"message": "auth router working"}

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    existing_email = get_user_by_email(
        db,
        user_data.email
    )

    if existing_email:
        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )

    existing_username = get_user_by_username(
        db,
        user_data.username
    )

    if existing_username:
        raise HTTPException(
            status_code=409,
            detail="Username already taken"
        )

    return create_user(
        db,
        user_data
    )

@router.post(
    "/login",
    response_model=UserResponse
)
def login(
    credentials: UserLogin,
    db: Session = Depends(get_db)
):
    user = authenticate_user(
        db,
        credentials.email,
        credentials.password
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return user