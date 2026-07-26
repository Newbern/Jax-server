from app.database.database import *
from app.security.hashing import *
from app.logs.log import log

def cookie(response, token, device_type):
    # Getting the Expiration date of the device based on its type
    expires = datetime.now() + session_type(device_type)

    # Converting to seconds
    seconds = int((expires - datetime.now()).total_seconds())

    print("SETTING COOKIE:", token)

    # Saving Cookie to Web
    response.set_cookie(
        key="session_token",
        value=token,
        httponly=True,
        secure=False,
        max_age=seconds
        )

def login(request, response):
    try:
        # Getting Device
        device_id = request.device_id
        device = get_device(device_id)

        # Checking to see if device exists
        if device is None:
            return {
                "success": False,
                "message": "Device not found"
            }

        # Checking API_KEY
        if device["api_key"] != request.api_key:
            log.warning(
                "Invalid API key",
                extra={
                    "device_id": device_id
                }
            )

            return {
                "success": False,
                "message": "Invalid API key"
            }

        # Getting The User of the Device
        user_id = device['user_id']

        # Getting Session for the Device Being Used
        session = get_session(user_id, device_id)

        if session is None:
            log.warning("Login attempted with unknown device", extra={"user_id": user_id, "device_id": device_id})
            return None

        # Checking to see if Session has Expired if so it will Create a new Session
        if not check_session(session["expires_at"]):
            delete_session(session["session_token"])
            session = create_session(user_id, device["device_id"], device["device_type"])

            # Saving cookie to web
            cookie(response, session, device["device_type"])

            # Creates a new session as well as returns the new token
            return {
                "success": True,
                "session": session
            }

        # Saving cookie to web
        cookie(response, session["session_token"], device["device_type"])

        # If the session is not expired return session_token
        return {
            "success": True,
            "session": session["session_token"]
        }
    
    except Exception as e:

        log.error(
            f"Login error: {e}",
            extra={
                "user_id": "UNKNOWN",
                "device_id": getattr(request, "device_id", "UNKNOWN")
            },
            exc_info=True
        )

        return {
            "success": False,
            "message": "Device not detected"
        }

def register(request):
    # Checking to see if email exists
    existing = get_email(request.email)

    if existing:
        return {
            "success": False,
            "message": "Email already exists"
        }

    # Creating Password & Making it secret
    password_hash = hash_password(request.password)


    # Creating User & return Id
    user_id = create_user(request.username, request.email, password_hash)

    # Creating Device & return Id
    device_id = create_device(user_id, request.device_type)

    # Creating Session & returning session_token
    session = create_session(
        user_id,
        device_id,
        request.device_type
    )

    # Returning Token
    return {
        "success": True,
        "session": session
    }

