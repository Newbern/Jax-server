from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api import auth
from app.logs.log import log
from contextlib import asynccontextmanager


# Logs
@asynccontextmanager
async def lifespan(app: FastAPI):
    log.info("JAX server Started")

    yield

    log.info("JAX server Shutting Down")


# Creating Connection
app = FastAPI(title="Jax Server", lifespan=lifespan)
# Mounting Static Files
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