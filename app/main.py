from fastapi import FastAPI
# Web Static Files
from fastapi.staticfiles import StaticFiles
# Importing Routers
from app.api import auth, alarm
# Logs
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
#app.mount("/web", StaticFiles(directory="app/web/", html=True), name="web")
#app.mount("/alarm-web", StaticFiles(directory="app/web/alarm", html=True), name="alarm-web")


# Adding Routes
app.include_router(auth.router)
app.include_router(alarm.router)



# Home
@app.get('/')
def home():
    return {
        "name": "Jax",
        "version": "1.0.0",
        "status": "online"
    }