from fastapi import FastAPI
from app.api import auth
from app.logs.log import log
from contextlib import asynccontextmanager


#----------MOVIE PLAYER SMALL BREAK----------
# from app.services.movie_scanner import scan_movies
# from app.services.movie_data_collector import get_movie_poster

# #scan_movies()
# print(get_movie_poster())




# Logs
@asynccontextmanager
async def lifespan(app: FastAPI):
    log.info("JAX server Started")

    yield

    log.info("JAX server Shutting Down")

# Creating Connection
app = FastAPI(title="Jax Server", lifespan=lifespan)




from fastapi.staticfiles import StaticFiles
app.mount("/web", StaticFiles(directory="app/web"), name="web")





# Adding Routes
app.include_router(auth.router)




# Home
@app.get('/')
def home():
    return {
        "name": "Jax",
        "version": "1.0.0",
        "status": "online"
    }