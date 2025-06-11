from fastapi import FastAPI, APIRouter


router = APIRouter()

@router.get("/")
async def test():
    return "this is working fine"