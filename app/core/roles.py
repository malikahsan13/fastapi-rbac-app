from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.jwt_handler import decode_token

security = HTTPBearer()

def require_role(required_roles: list):
    def wrapper(credentials: HTTPAuthorizationCredentials = Depends(security)):
        token = credentials.credentials
        payload = decode_token(token)
        if not payload or payload.get("role") not in required_roles:
            raise HTTPException(403, detail="Insufficient role privileges")
        return payload
    return wrapper