from fastapi import APIRouter
# Web Static Files
from fastapi.staticfiles import StaticFiles
# Alarm Schemas and Services
from app.schemas.alarm import *
from app.services.alarm import *
# Security
from app.security.session import *

# Setting up router
router = APIRouter(prefix="/alarm", tags=["Alarm"])

# Mounting Static Files
router.mount("/get-alarms", StaticFiles(directory="app/web/alarm", html=True), name="get_alarms")
router.mount("/create-alarm", StaticFiles(directory="app/web/alarm", html=True), name="create_alarm")

# API Endpoints for Alarm
@router.post("/create-alarm")
async def create_alarm(request: AlarmRequest, session_token = Depends(secure_session_token)):
    return await create_new_alarm(request, session_token)

@router.get("/get-alarms")
async def get_alarms(session_token = Depends(secure_session_token)):
    return await get_all_alarms(session_token)