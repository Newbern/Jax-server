from fastapi import APIRouter
from fastapi.responses import FileResponse
from app.schemas.alarm import *
from app.services.alarm import *
from app.security.session import *

# Setting up router
router = APIRouter(prefix="/alarm", tags=["Alarm"])

# API Endpoints for Alarm
@router.post("/create-alarm")
async def create_alarm(request: AlarmRequest, session_token: str = Depends(secure_session_token)):
    return await create_new_alarm(request, session_token)