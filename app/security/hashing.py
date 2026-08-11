import bcrypt

def hash_password(password: str):
    password_bytes = password.encode("utf-8")

    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(
        password_bytes,
        salt
    )

    return hashed_password.decode("utf-8")

def verify_password(user_password, stored_password):
    password = user_password.encode("utf-8")
    stored_password = stored_password.encode("utf-8")

    return bcrypt.checkpw(stored_password, password)