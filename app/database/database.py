import mysql.connector
from datetime import datetime
from app.security.session import session_type, create_token

#----------------CREATE THINGS----------------
# Getting Database Connection
def get_database_connection():
    # Settings up connection to database
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="jax_server"
    )

# Creating Database
def setup_database():
    # Getting connection
    connection = get_database_connection()
    cursor = connection.cursor()

    with open("server/database/setup.sql", "r", encoding="utf-8") as file:
       sql_script = file.read()

    # Execute each SQL statement
    for statement in sql_script.split(";"):
       statement = statement.strip()
       if statement:
           cursor.execute(statement)

    # Commit the changes and close the connection
    connection.commit()
    cursor.close()
    connection.close()

    print("Database setup completed!")

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

# Creating User
def create_user(username, email, password):
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute(
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
    connection.commit()
    cursor.close()
    connection.close()

    return data

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

#------------------DELETE THINGS--------------------
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

#---------------GET THINGS-----------------
# Get User
def get_user(user_id):
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM users WHERE id = %s",
        (user_id,)
    )
    data = cursor.fetchone()
    cursor.close()
    connection.close()
    return data

# Get User By Email
def get_email(email):
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM users WHERE email = %s",
        (email,)
    )
    data = cursor.fetchone()
    cursor.close()
    connection.close()
    return data

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
# Get Session
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


    
#-----------------SECURITY===============

# Checking to see if Session Expires
def check_session(expiration):
    if expiration is None:
        return False
    if expiration < datetime.now():
        return False

    return True

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
#------------------MEDIA-----------------