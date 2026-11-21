from fastapi import APIRouter
from fastapi import Response
from app.services.roku import *
from app.security.session import *

# Setting up router
router = APIRouter(prefix="/roku", tags=["Roku"])


# Roku Commands
@router.post("/commands")
async def roku_commands(request, session_token = Depends(secure_session_token)):
    return await roku_command(request, session_token)