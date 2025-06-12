from fastapi import FastAPI
from app.routes import auth_routes, user_routes

app = FastAPI()

app.include_router(auth_routes.router)
app.include_router(user_routes.router)

# app.include_router(user_routes.router, prefix="/users", tags=["users"])
