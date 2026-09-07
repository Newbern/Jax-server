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
    user = await authenticate_token(session_token)
    
    if user is False:
        return authenticate_token_error(session_token)

    # Getting Alarms
    alarms = await get_alarms(user["id"])

    return alarms

async def update_alarm_data(request, session_token):
    # Authenticating User
    user = await authenticate_token(session_token)

    if user is False:
        return authenticate_token_error(session_token)

    # Updating Alarm
    updated_alarm = await update_alarm(request, user["id"])

    return {
        "success": True,
        "message": "Alarm updated successfully"
    }

async def delete_alarm_data(request, session_token):
    # Authenticating User
    user = await authenticate_token(session_token)

    if user is False:
        return authenticate_token_error(session_token)

    # Deleting Alarm
    deleted_alarm = await delete_alarm(request, user["id"])

    return {
        "success": True,
        "message": "Alarm deleted successfully"
    }