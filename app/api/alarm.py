from fastapi import APIRouter
# Web Static Files
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
# Alarm Schemas and Services
from app.schemas.alarm import *
from app.services.alarm import *
# Security
from app.security.session import *

# Setting up router
router = APIRouter(prefix="/alarm", tags=["Alarm"])

# Mounting Static Files
router.mount("/alarm-web", StaticFiles(directory="app/web/alarm", html=True), name="alarm-web")

@router.get("/create-alarm")
async def create_alarm_page():
    return FileResponse("app/web/alarm/create_alarm/index.html")

@router.get("/get-alarms")
async def get_alarms_page():
    return FileResponse("app/web/alarm/get_alarms/index.html")

# API Endpoints for Alarm
@router.post("/create-alarm")
async def create_alarm(request: AlarmRequest, session_token = Depends(secure_session_token)):
    return await create_new_alarm(request, session_token)

@router.get("/get-alarm-data")
async def get_alarms(session_token = Depends(secure_session_token)):
    return await get_all_alarms(session_token)

@router.post("/updated-alarm-data")
async def update_alarm(request: AlarmUpdateRequest, session_token = Depends(secure_session_token)):
    return await update_alarm_data(request, session_token)

@router.post("/delete-alarm-data")
async def delete_alarm(request: AlarmDeleteRequest, session_token = Depends(secure_session_token)):
    return await delete_alarm_data(request, session_token)