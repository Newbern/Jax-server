import aiomysql

# Getting Database Connection
async def get_database_connection():
    # Settings up connection to database
    return await aiomysql.connect(
        host="localhost",
        user="root",
        password="",
        db="jax_server"
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