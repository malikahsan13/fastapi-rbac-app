from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.jwt_handler import decode_token

security = HTTPBearer()

def require_role(required_roles: list):
    