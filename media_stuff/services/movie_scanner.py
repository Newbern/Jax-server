from pathlib import Path
import re
from app.database.database import get_database_connection

MOVIE_DIR = Path(r"D:\Movie Collection")


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

                    # Remove file extension
                    title = movie.stem

                    # Default year
                    year = None

                    # Look for "(1997)" at the end of the title
                    match = re.search(r"\((\d{4})\)$", title)

                    if match:
                        year = int(match.group(1))
                        title = re.sub(r"\s*\(\d{4}\)$", "", title)

                    print(f"Found: {title} ({year})")

                    cursor.execute(
                        """
                        INSERT INTO movies(
                            title,
                            year,
                            genre,
                            filename,
                            filepath
                        )
                        VALUES(%s,%s,%s,%s,%s)
                        """,
                        (
                            title,
                            year,
                            genre,
                            filename,
                            filepath
                        )
                    )

    connection.commit()

    cursor.close()
    connection.close()
