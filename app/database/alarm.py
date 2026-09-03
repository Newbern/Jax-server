from app.database.connection import *
from app.schemas.alarm import *


# Create a new alarm in the database
async def create_alarm(user_id, request: AlarmRequest):
    connection = await get_database_connection()

    async with connection.cursor() as cursor:
        await cursor.execute(
            "INSERT INTO alarms (user_id, time, day, message, is_repeat) "
            "VALUES (%s, %s, %s, %s, %s)",
            (user_id, request.time, request.day, request.message, request.is_repeat)
        )

        await connection.commit()

        data = cursor.lastrowid

    connection.close()

    return data if data else None


# Get all alarms for a user
async def get_all_alarms(user_id):
    connection = await get_database_connection()

    async with connection.cursor(aiomysql.DictCursor) as cursor:
        await cursor.execute(
            "SELECT * FROM alarms WHERE user_id = %s",
            (user_id,)
        )

        data = await cursor.fetchall()

    connection.close()

    return data if data else []