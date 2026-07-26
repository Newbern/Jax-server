from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from pathlib import Path
from app.database.database import validate_session

# Setting up router
router = APIRouter(prefix="/auth", tags=["Media Player"])

MOVIE_DIR = Path("D:\Movie Collection")

@router.get("/movie_collection/")
def get_movies(request: Request):
    # Getting Token from Web
    token = request.cookies.get("session_token")

    # Checking if cookie exists
    if token is None:
        return {
            "success": False,
            "message": "Not logged in"
        }

    genres = []

    for genre in MOVIE_DIR.iterdir():
        if genre.is_dir():
            movies = []

            for movie in genre.iterdir():
                if movie.is_file():
                    movies.append(movie.name)

            genres.append({
                "name": genre.name,
                "movies": movies
            })

    return {
        "success": True,
        "genres": genres
    }

    





    