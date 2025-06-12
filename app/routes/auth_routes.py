from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserLogin, UserRegister, UserOut
from app.db.database import db
from app.utils.security import hash_password, verify_password
from app.core.jwt_handler import create_access_token
from bson import ObjectId

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserOut)
async def register(user: UserRegister):
    if await db.users.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    user_dict = user.model_dump()
    user_dict["password"] = hash_password(user.password)
    user_dict["role"] = "user"
    result = await db.users.insert_one(user_dict)
    
    return {"username": user.username, "email": user.email}

@router.post("/login")
async def login(user: UserLogin):
    user_db = await db.users.find_one({"email": user.email})
    if not user_db or not verify_password(user.password, user_db["password"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    token = create_access_token({"sub": user_db["email"], "role": user_db["role"]})
    return {"access_token": token, "token_type": "bearer"}