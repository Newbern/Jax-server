from app.database.users import get_user_by_token

async def authenticate_token(token: str):
    # Getting User
    user = await get_user_by_token(token)

    # Checking to see if user exists
    if user is None:
        return {
            "success": False,
            "message": "User not found"
        }

    # Checking if the token is expired
    # HERE

    # Returning User
    return user