from pathlib import Path
from app.database.database import get_database_connection


MOVIE_DIR = Path("D:\Movie Collection")


def scan_movies():

    connection = get_database_connection()
    cursor = connection.cursor()

    for genre_folder in MOVIE_DIR.iterdir():

        if genre_folder.is_dir():

            genre = genre_folder.name

            for movie in genre_folder.iterdir():

                if movie.is_file():

                    filename = movie.name
                    filepath = str(movie)

                    print("Found:", filename)

                    cursor.execute(
                        """
                        INSERT INTO movies(
                            title,
                            genre,
                            filename,
                            filepath
                        )
                        VALUES(%s,%s,%s,%s)
                        """,
                        (
                            movie.stem,
                            genre,
                            filename,
                            filepath
                        )
                    )

    connection.commit()

    cursor.close()
    connection.close()