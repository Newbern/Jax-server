from app.database.connection import *


#----------------CREATE----------------
# Creating User
async def create_user(username, email, password):
    connection = await get_database_connection()

    async with connection.cursor() as cursor:
        await cursor.execute(
            """
            INSERT INTO users
            (username, email, password)
            VALUES (%s, %s, %s)
            """,
            (
                username,
                email,
                password
            )
        )

        data = cursor.lastrowid
        await connection.commit()

    connection.close()

    return data


#----------------GET----------------
# Get User
async def get_user(user_id):
    connection = await get_database_connection()

    async with connection.cursor(aiomysql.DictCursor) as cursor:
        await cursor.execute(
            "SELECT * FROM users WHERE id = %s",
            (user_id,)
        )

        data = await cursor.fetchone()

    connection.close()

    return data


# Get User By Email
async def get_email(email):
    connection = await get_database_connection()

    async with connection.cursor(aiomysql.DictCursor) as cursor:
        await cursor.execute(
            "SELECT * FROM users WHERE email = %s",
            (email,)
        )

        data = await cursor.fetchone()

    connection.close()

    return data


async def get_user_by_token(token):
    connection = await get_database_connection()

    async with connection.cursor(aiomysql.DictCursor) as cursor:
        await cursor.execute(
            "SELECT * FROM sessions WHERE session_token = %s",
            (token,)
        )

        # Getting Session Token data
        data = await cursor.fetchone()

    connection.close()

    if not data:
        return None

    # Getting User from the session token data
    return await get_user(data["user_id"])
