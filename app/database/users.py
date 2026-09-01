from app.database.connection import get_database_connection


#----------------CREATE----------------
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

#----------------GET----------------
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

def get_user_by_token(token):
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM sessions WHERE session_token = %s",
        (token,)
    )
    # Getting Session Token data
    data = cursor.fetchone()
    # Getting User from the session token data
    data = get_user(data["user_id"])
    
    cursor.close()
    connection.close()
    return data if data else None
