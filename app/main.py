from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.endpoints import timelapse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(timelapse.router, prefix="/api/v1/timelapse")
