# Database
from app.database.users import *
from app.database.sessions import *
from app.database.devices import *
# Security
from app.security.hashing import *
from app.security.session import *
from app.logs.log import log


def web_login(request, response):
    try:
        # Getting User
        user = "UNKNOWN"
        user = get_email(request.email)

        # Checking to see if user exists
        if user is None:
            return {
                "success": False,
                "message": "User not found"
            }

        # Checking Password
        if not verify_password(user['password'], request.password):
            log.warning(
                "Invalid password",
                extra={
                    "user_id": user["id"]
                }
            )

            return {
                "success": False,
                "message": "Invalid password"
            }

        # Getting Device_id
        device_id = get_device_by_type(user["id"], request.device_type)

        # Checking to see if session exists
        if device_id is None:
            log.error(
                f"Login error: No device_id found for user '{user['id']}' and device type '{request.device_type}'",
                extra={
                    "user_id": user["id"], 
                    "device_type ": request.device_type
                },
                exc_info=True
            )
            return {
                "success": False,
                "message": "Incorrect device type"
            }

        
        # Checking to see if session is not expired if so it will create a new session
        session = get_session(user["id"], device_id["id"])
        if not check_session(session['expires_at']):
            delete_session(session["session_token"])
            session = create_session(user["id"], device_id["id"], request.device_type)

        # Saving cookie to web
        device_type = request.device_type
        cookie(response, session, device_type)

        # Updating the last login time for the user
        last_seen = update_last_login(device_id["id"])
        log.info(
            "User last seen updated",
            extra={
                "user_id": user["id"]
            })

        return {
            "success": True,
            "session": session
        }

    except Exception as e:
        log.error(
            f"Login error: {e}",
            extra={
                "user_id": getattr(user, "id", "UNKNOWN")
            },
            exc_info=True
        )

        return {
            "success": False,
            "message": "Login failed"
        }
        
        


async def device_login(request):
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
            session = create_session(user_id, device_id, device["device_type"])

            # Creates a new session as well as returns the new token
            return {
                "success": True,
                "session": session
            }

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

async def register(request):
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

