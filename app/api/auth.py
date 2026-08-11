from fastapi import APIRouter
from fastapi import Response
from fastapi.responses import FileResponse
from app.schemas.auth import LoginRequest, RegisterRequest
from app.services.auth import web_login, register

# Setting up router
router = APIRouter(prefix="/auth", tags=["Authorization"])

@router.get("/login")
def login_page():
    return FileResponse("app/web/login.html")

@router.get("/signup")
def signup_page():
    return FileResponse("app/web/signup.html")


@router.post("/login")
def signin(request: LoginRequest, response: Response):
    return web_login(request, response)

@router.post("/signup")
def signup(request: RegisterRequest):
    return register(request)