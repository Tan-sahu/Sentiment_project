from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from database import get_db

# --- IMPORT FIXES ---
# 1. 'schemas.user' matches your file 'schemas/user.py'
from schemas.user import UserCreate, UserOut, Token 
from services.auth_services import AuthService       
# --------------------

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/signup", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    return AuthService.register_user(db=db, user=user)

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return AuthService.login_user(db=db, form_data=form_data)