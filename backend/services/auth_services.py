from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models import User # Import your SQLAlchemy User model here
from schemas import UserCreate
from core.security import get_password_hash, verify_password, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta

class AuthService:
    
    @staticmethod
    def register_user(db: Session, user: UserCreate):
        # 1. Check if user already exists
        existing_user = db.query(User).filter(User.email == user.email).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        # 2. Hash the password
        hashed_password = get_password_hash(user.password)
        
        # 3. Create DB Object
        db_user = User(email=user.email, hashed_password=hashed_password)
        
        # 4. Save to DB
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        
        return db_user

    @staticmethod
    def login_user(db: Session, form_data):
        # 1. Find user by email (username field in OAuth2 form usually holds email)
        user = db.query(User).filter(User.email == form_data.username).first()
        
        # 2. Verify User and Password
        if not user or not verify_password(form_data.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # 3. Create JWT Token
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )
        
        return {"access_token": access_token, "token_type": "bearer"}