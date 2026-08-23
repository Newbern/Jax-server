import bcrypt

def hash_password(password: str):
    password_bytes = password.encode("utf-8")

    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(
        password_bytes,
        salt
    )

    return hashed_password.decode("utf-8")

def verify_password(database_password, input_password):
    return bcrypt.checkpw(input_password.encode("utf-8"), database_password.encode("utf-8"))