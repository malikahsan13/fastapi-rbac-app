from fastapi import APIRouter, Depends
from app.core.roles import require_role

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/admin-only", dependencies=[Depends(require_role(["admin"]))])
async def admin_area():
    return {"message": "Welcome, admin!"}