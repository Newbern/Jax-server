from app.database.connection import get_database_connection
from app.database.users import get_user
from app.security.session import session_type, create_token
from datetime import datetime

#----------------CREATE----------------
# Creating a Session
def create_session(user_id, device_id, device_type):

    connection = get_database_connection()
    cursor = connection.cursor()

    expires = datetime.now() + session_type(device_type)

    cursor.execute(
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


    connection.commit()
    cursor.close()
    connection.close()

    return get_session(user_id, device_id)["session_token"]

#----------------GET----------------
def get_session(user_id, device_id):
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(
        """
        SELECT * 
        FROM sessions 
        WHERE user_id = %s 
        AND device_id = %s
        """,
        (user_id, device_id)
    )
    
    data = cursor.fetchone()
    cursor.close()
    connection.close()
    return data

def validate_session(token):
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(
        """
        SELECT * 
        FROM sessions 
        WHERE session_token = %s
        """,
        (token)
    )
    
    data = cursor.fetchone()
    data = get_user(data["user_id"])
    cursor.close()
    connection.close()
    return data

# Checking to see if Session Expires
def check_session(expiration):
    if expiration is None:
        return False
    if expiration < datetime.now():
        return False

    return True

#----------------DELETE----------------
# Delete Session
def delete_session(token):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        DELETE FROM sessions
        WHERE session_token = %s
        """,
        (token,)
    )
    connection.commit()
    cursor.close()
    connection.close()
