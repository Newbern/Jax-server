from app.database.connection import get_database_connection
from app.database.users import get_user
from app.security.session import create_token
from datetime import datetime

#----------------CREATE----------------
# Creating Device
def create_device(user_id, device_type):
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(
        """
        INSERT INTO devices
        (api_key, user_id, device_name, device_type)
        VALUES (%s, %s, %s, %s)
        """,
        (
            create_token(),
            user_id,
            get_user(user_id)["username"] + " devices",
            device_type
        )
    )

    data = cursor.lastrowid
    connection.commit()
    cursor.close()
    connection.close()

    return data

# Get device by device_type and user_id
def get_device_by_type(user_id, device_type):
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(
        """
        SELECT * 
        FROM devices 
        WHERE user_id = %s 
        AND device_type = %s
        """,
        (user_id, device_type)
    )
    
    data = cursor.fetchone()
    cursor.close()
    connection.close()
    return data if data else None

#----------------GET----------------
# Get Device
def get_device(device_id):
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM devices WHERE id = %s",
        (device_id,)
    )
    data = cursor.fetchone()
    cursor.close()
    connection.close()
    return data

# Get Device Type
def get_device_type(device_id, user_id):
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(
        """
        SELECT device_type
        FROM devices
        WHERE id = %s AND user_id = %s
        """,
        (device_id, user_id)
    )
    data = cursor.fetchone()
    cursor.close()
    connection.close()
    return data["device_type"] if data else None

#----------------UPDATE----------------
# Updating Last Login Time
def update_last_login(device_id):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        UPDATE devices
        SET last_seen = %s
        WHERE id = %s
        """,
        (datetime.now(), device_id)
    )
    data = cursor.fetchone()
    connection.commit()
    cursor.close()
    connection.close()
    return data["last_seen"] if data else None
