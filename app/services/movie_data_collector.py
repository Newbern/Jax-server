import os
import requests
from dotenv import load_dotenv

load_dotenv()

TMDB_KEY = os.getenv("TMDB_API_KEY")


def get_movie_poster(title, year):

    url = "https://api.themoviedb.org/3/search/movie"

    params = {
        "api_key": TMDB_KEY,
        "query": title,
        "year": year
    }

    response = requests.get(url, params=params)

    data = response.json()

    if not data["results"]:
        return None

    movie = data["results"][0]

    poster = movie.get("poster_path")

    if poster:
        return "https://image.tmdb.org/t/p/w500" + poster

    return None