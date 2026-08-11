import os
import requests
from dotenv import load_dotenv

load_dotenv()

TMDB_KEY = os.getenv("TMDB_API_KEY")


def get_movie_poster(title, year=None):

    url = "https://api.themoviedb.org/3/search/movie"

    params = {
        "api_key": TMDB_KEY,
        "query": title
    }

    # Only include the year if we have one
    if year is not None:
        params["year"] = year

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None

    data = response.json()

    if not data.get("results"):
        return None

    poster = data["results"][0].get("poster_path")

    if not poster:
        return None

    return f"https://image.tmdb.org/t/p/w500{poster}"