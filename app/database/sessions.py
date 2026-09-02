from app.database.connection import *
from app.database.users import get_user
from app.security.session import session_type, create_token
from datetime import datetime


#----------------CREATE----------------
# Creating a Session
async def create_session(user_id, device_id, device_type):

    connection = await get_database_connection()

    expires = datetime.now() + session_type(device_type)

    async with connection.cursor() as cursor:
        await cursor.execute(
            """
            INSERT INTO sessions
            (user_id, device_id, session_token, expires_at)
            VALUES (%s, %s, %s, %s)
            """,
            (
                user_id,
                device_id,
                create_token(),
                expires
            )
        )

        await connection.commit()

    connection.close()

    session = await get_session(user_id, device_id)

    return session["session_token"]


#----------------GET----------------
async def get_session(user_id, device_id):
    connection = await get_database_connection()

    async with connection.cursor(aiomysql.DictCursor) as cursor:
        await cursor.execute(
            """
            SELECT *
            FROM sessions
            WHERE user_id = %s
            AND device_id = %s
            """,
            (user_id, device_id)
        )

        data = await cursor.fetchone()

    connection.close()

    return data


async def validate_session(token):
    connection = await get_database_connection()

    async with connection.cursor(aiomysql.DictCursor) as cursor:
        await cursor.execute(
            """
            SELECT *
            FROM sessions
            WHERE session_token = %s
            """,
            (token,)
        )

        data = await cursor.fetchone()

    connection.close()

    if not data:
        return None

    return await get_user(data["user_id"])


# Checking to see if Session Expires
def check_session(expiration):
    if expiration is None:
        return False

    if expiration < datetime.now():
        return False

    return True


#----------------DELETE----------------
# Delete Session
async def delete_session(token):
    connection = await get_database_connection()

    async with connection.cursor() as cursor:
        await cursor.execute(
            """
            DELETE FROM sessions
            WHERE session_token = %s
            """,
            (token,)
        )

        await connection.commit()

    connection.close()