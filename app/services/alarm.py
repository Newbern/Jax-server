# Database
from app.database.alarm import *
from app.utils.auth import authenticate_token

# Security
from app.logs.log import log


# Creating Alarm
async def create_new_alarm(request, session_token):

    # Authenticating User
    user = authenticate_token(session_token)

    # Creating Alarm
    alarm = await create_alarm(user["id"], request)

    return {
        "success": True,
        "message": "Alarm created successfully"
    }