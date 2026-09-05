import secrets
from datetime import datetime, timedelta

# Security
from fastapi import Cookie, HTTPException, Depends
import json

def session_type(device_type):
    WATCH = "watch"
    WEB = "web"
    AUTH = "auth"

    SESSION_LENGTHS = {
        WATCH: timedelta(days=90),
        WEB: timedelta(days=3),
        AUTH: timedelta(hours=1)
    }
    length = SESSION_LENGTHS.get(device_type)

    if length is None:
        raise ValueError(f"Invalid device type: {device_type}")

    return length

def create_token():
    return secrets.token_hex(32)

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


# Security with FastAPI by browser cookies
def secure_session_token(session_token = Cookie(default=None)):
    if not session_token:
        raise HTTPException(
            status_code=401,
            detail="Session token is missing"
        )

    return session_token
