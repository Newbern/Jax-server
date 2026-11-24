
from app.logs.log import log
from app.utils.auth import *
import httpx

async def roku_command(request, session_token):
    try:
        # Authenticating User
        user = await authenticate_token(session_token)

        if user is False:
            return authenticate_token_error(session_token)

        # Roku Connection
        roku_ip = "10.0.0.20"
        base_url = f"http://{roku_ip}:8060"

        command = request.command
        action = request.action

        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{base_url}/{action}/{command}",
                timeout=5
            )

        response.raise_for_status()

        return {"status": "success"}

    except Exception as e:
        log.error(f"Roku Error: {str(e)}")
        raise