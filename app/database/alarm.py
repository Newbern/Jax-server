from app.database.connection import get_database_connection
from app.schemas.alarm import *

# Create a new alarm in the database
def create_alarm(user_id, request : AlarmRequest):
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)

    # Insert the new alarm into the database
    cursor.execute(
        "INSERT INTO alarms (user_id, time, day, message, is_repeat) VALUES (%s, %s, %s, %s, %s)",
        (user_id, request.time, request.day, request.message, request.is_repeat)
    )
    connection.commit()

    data = cursor.lastrowid  # Get the ID of the newly created alarm
    cursor.close()
    connection.close()

    return data if data else None

def get_all_alarms(user_id):
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)

    # Fetch all alarms for the given user_id
    cursor.execute(
        "SELECT * FROM alarms WHERE user_id = %s",
        (user_id,)
    )
    data = cursor.fetchall()  # Fetch all rows

    cursor.close()
    connection.close()

    return data if data else []