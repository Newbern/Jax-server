
from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware


class AuthMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        path = request.url.path

        # Pages that don't require authentication
        public_paths = {
            "/auth/login",
            "/auth/signup",
            "/auth/login-page",
            "/auth/signup-page",
        }

        # Allow login and signup pages
        if path in public_paths:
            return await call_next(request)

        # Allow login and signup assets
        if path.startswith("/auth-web/"):
            return await call_next(request)

        # Check for the session token
        token = request.cookies.get("session_token")

        if not token:
            return RedirectResponse(
                url="/auth/login",
                status_code=303
            )

        # TODO: Validate the token against your database here.
        # If invalid or expired, redirect to login.

        return await call_next(request)