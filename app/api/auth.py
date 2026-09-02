from fastapi import APIRouter
from fastapi import Response
from fastapi.responses import FileResponse
from app.schemas.auth import *
from app.services.auth import *

# Setting up router
router = APIRouter(prefix="/auth", tags=["Authorization"])

# Web Pages Login and Signup
@router.get("/login")
def login_page():
    return FileResponse("app/web/auth/login.html")

@router.get("/signup")
def signup_page():
    return FileResponse("app/web/auth/signup.html")

# Web Pages Login and Signup
@router.post("/login")
async def signin(request: LoginRequest, response: Response):
    return await web_login(request, response)

@router.post("/signup")
async def signup(request: RegisterRequest):
    return await register(request)

# API Endpoints for Device Login
@router.post("/device-login")
def login_device(request: DeviceLoginRequest):
    return device_login(request)