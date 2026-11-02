
from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware

from fastapi.responses import JSONResponse

class AuthMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        path = request.url.path

        # Pages that don't require authentication
        public_paths = {
            "/auth/login",
            "/auth/signup",
            "/auth/login-page",
            "/auth/signup-page",
            "/auth/device-login"
        }

        # Allow login and signup pages
        if path in public_paths:
            return await call_next(request)

        # Allow login and signup assets
        if path.startswith("/auth-web/"):
            return await call_next(request)

        # Check for the session token
        #token = request.cookies.get("session_token")

        token = (request.cookies.get("session_token") or request.headers.get("X-Session-Token"))
        print("Auth | Path:", path)
        print("Auth | Cookie:", bool(request.cookies.get("session_token")))
        print("Auth | Header:", bool(request.headers.get("X-Session-Token")))
        print("Auth | Token found:", bool(token))
        if not token:
            if path.startswith("/alarm/") and request.headers.get("X-Session-Token") is None:
                return RedirectResponse("/auth/login", status_code=303)

            return JSONResponse(
                status_code=401,
                content={"success": False, "message": "Authentication required"}
            )




        ##if not token:
        ##    return RedirectResponse(
        ##        url="/auth/login",
        ##        status_code=303
        ##    )

        # TODO: Validate the token against your database here.
        # If invalid or expired, redirect to login.

        return await call_next(request)