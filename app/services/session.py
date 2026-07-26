import secrets
from datetime import timedelta

def session_type(device_type):
    WATCH = "watch"
    WEB = "web"
    AUTH = "auth"

    SESSION_LENGTHS = {
        WATCH: timedelta(days=90),
        WEB: timedelta(days=3),
        AUTH: timedelta(hours=1)
    }

    return SESSION_LENGTHS.get(device_type)


def create_token():
    return secrets.token_hex(32)

