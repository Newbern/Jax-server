from app.database.connection import get_database_connection

# Create a new alarm in the database
def create_alarm(user_id, time, day, message, repeat):
    connection = get_database_connection()
    cursor = connection.cursor(Dictionary=True)

    # Insert the new alarm into the database
    cursor.execute(
        "INSERT INTO alarms (user_id, time, day, message, repeat) VALUES (%s, %s, %s, %s, %s)",
        (user_id, time, day, message, repeat)
    )
    connection.commit()

    data = cursor.lastrowid  # Get the ID of the newly created alarm
    cursor.close()
    connection.close()

    return data if data else None