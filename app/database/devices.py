from app.database.connection import *
from app.database.users import get_user
from app.security.session import create_token
from datetime import datetime

#----------------CREATE----------------
# Creating Device
async def create_device(user_id, device_type):
    connection = await get_database_connection()

    async with connection.cursor(aiomysql.DictCursor) as cursor:
        user = await get_user(user_id)

        await cursor.execute(
            """
            INSERT INTO devices
            (api_key, user_id, device_name, device_type)
            VALUES (%s, %s, %s, %s)
            """,
            (
                create_token(),
                user_id,
                user["username"] + " devices",
                device_type
            )
        )

        data = cursor.lastrowid

        await connection.commit()

    connection.close()

    return data


# Get device by device_type and user_id
async def get_device_by_type(user_id, device_type):
    connection = await get_database_connection()

    async with connection.cursor(aiomysql.DictCursor) as cursor:
        await cursor.execute(
            """
            SELECT *
            FROM devices
            WHERE user_id = %s
            AND device_type = %s
            """,
            (user_id, device_type)
        )

        data = await cursor.fetchone()

    connection.close()

    return data if data else None


#----------------GET----------------
# Get Device
async def get_device(device_id):
    connection = await get_database_connection()

    async with connection.cursor(aiomysql.DictCursor) as cursor:
        await cursor.execute(
            "SELECT * FROM devices WHERE id = %s",
            (device_id,)
        )

        data = await cursor.fetchone()

    connection.close()

    return data


# Get Device Type
async def get_device_type(device_id, user_id):
    connection = await get_database_connection()

    async with connection.cursor(aiomysql.DictCursor) as cursor:
        await cursor.execute(
            """
            SELECT device_type
            FROM devices
            WHERE id = %s AND user_id = %s
            """,
            (device_id, user_id)
        )

        data = await cursor.fetchone()

    connection.close()

    return data["device_type"] if data else None


#----------------UPDATE----------------
# Updating Last Login Time
async def update_last_login(device_id):
    connection = await get_database_connection()

    last_seen = datetime.now()

    async with connection.cursor() as cursor:
        await cursor.execute(
            """
            UPDATE devices
            SET last_seen = %s
            WHERE id = %s
            """,
            (last_seen, device_id)
        )

        await connection.commit()

    connection.close()

    return last_seen
