from fastapi import APIRouter
# Web Static Files
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
# Roku Schemas and Services
from app.schemas.roku import *
from app.services.roku import *
# Security
from app.security.session import *

# Setting up router
router = APIRouter(prefix="/roku", tags=["Roku"])


# Roku Commands
@router.post("/commands")
async def roku_commands(request: CommandRequest, session_token = Depends(secure_session_token)):
    return await roku_command(request, session_token)