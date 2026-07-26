from fastapi import APIRouter
from fastapi import Response
from app.schemas.auth import LoginRequest, RegisterRequest
from app.services.auth import login, register

# Setting up router
router = APIRouter(prefix="/auth", tags=["Authorization"])

@router.post("/login")
def signin(request: LoginRequest, response: Response):
    return login(request, response)

@router.post("/signup")
def signup(request: RegisterRequest):
    return register(request)