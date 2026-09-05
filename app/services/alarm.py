# Database
from app.database.alarm import *
from app.utils.auth import *

# Security
from app.logs.log import log


# Creating Alarm
async def create_new_alarm(request, session_token):
    # Authenticating User
    user = await authenticate_token(session_token)

    if user is False:
        return authenticate_token_error(session_token)

    # Creating Alarm
    alarm = await create_alarm(user["id"], request)

    return {
        "success": True,
        "message": "Alarm created successfully"
    }

async def get_all_alarms(session_token):
    # Authenticating User
    print("session_token:", session_token)
    user = await authenticate_token(session_token)

    if user is False:
        return authenticate_token_error(session_token)

    # Getting Alarms
    alarms = await get_all_alarms(user["id"])

    return alarms



    