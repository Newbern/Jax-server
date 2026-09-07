from app.database.connection import *
from app.schemas.alarm import *


# Create a new alarm in the database
async def create_alarm(user_id, request: AlarmRequest):
    connection = await get_database_connection()

    async with connection.cursor() as cursor:
        await cursor.execute(
            "INSERT INTO alarms (user_id, time, day, message, turn_on) "
            "VALUES (%s, %s, %s, %s, %s)",
            (user_id, request.time, request.day, request.message, request.turn_on)
        )

        await connection.commit()

        data = cursor.lastrowid

    connection.close()

    return data if data else None


# Get all alarms for a user
async def get_alarms(user_id):
    connection = await get_database_connection()

    async with connection.cursor(aiomysql.DictCursor) as cursor:
        await cursor.execute(
            "SELECT * FROM alarms WHERE user_id = %s",
            (user_id,)
        )

        data = await cursor.fetchall()

    connection.close()

    return data if data else []

# Update an existing alarm in the database
async def update_alarm(request: AlarmUpdateRequest, user_id):
    connection = await get_database_connection()

    async with connection.cursor() as cursor:
        await cursor.execute(
            "UPDATE alarms SET time = %s, day = %s, message = %s, turn_on = %s "
            "WHERE id = %s AND user_id = %s",
            (request.time, request.day, request.message, request.turn_on, request.id, user_id)
        )

        await connection.commit()

    connection.close()

    return True

# Delete an existing alarm from the database
async def delete_alarm(request: AlarmDeleteRequest, user_id):
    connection = await get_database_connection()

    async with connection.cursor() as cursor:
        await cursor.execute(
            "DELETE FROM alarms WHERE id = %s AND user_id = %s",
            (request.id, user_id)
        )

        await connection.commit()

    connection.close()

    return True