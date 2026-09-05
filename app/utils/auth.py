from app.database.sessions import *
from app.database.devices import *
from app.logs.log import log

async def authenticate_token(token: str):
    # Getting User
    user = await get_user_by_token(token)

    # Getting Device
    device = await get_device_by_token(token)

    # Checking to see if user exists
    if user is None:
        return False

    # Getting Session Token Information
    user_id = user["id"]
    device_id = device["id"]
    device_type = device["device_type"]

    # Getting Session
    session = await get_session(user_id, device_id)
    token = session["session_token"]

    # Sessions Expiration date
    expiration = session["expires_at"]

    if expiration < datetime.now():
        await delete_session(token)
        await create_session(user_id, device_id, device_type)



    # Returning User
    return user


def authenticate_token_error(token):
    log.error(
        "User not authenticated",
        extra={
            "session_token": token
        },
        exc_info=True
    )
    return {
        "success": False,
        "message": "User not authenticated"
 }