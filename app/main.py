from fastapi import FastAPI
from app.api import auth, media
from app.logs.log import log
from contextlib import asynccontextmanager



from app.services.movie_scanner import scan_movies

scan_movies()




# Logs
@asynccontextmanager
async def lifespan(app: FastAPI):
    log.info("JAX server Started")

    yield

    log.info("JAX server Shutting Down")

# Creating Connection
app = FastAPI(title="Jax Server", lifespan=lifespan)

# Adding Routes
app.include_router(auth.router)
app.include_router(media.router)




# Home
@app.get('/')
def home():
    return {
        "name": "Jax",
        "version": "1.0.0",
        "status": "online"
    }