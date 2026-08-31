from fastapi import APIRouter
from app.schemas.alarm import *
from app.services.alarm import *

# Setting up router
router = APIRouter(prefix="/alarm", tags=["Alarm"])

# API Endpoints for Alarm
@router.post("/create-alarm")
def create_alarm(request: AlarmRequest, session_token: str = None):
    return create_new_alarm(request, session_token)