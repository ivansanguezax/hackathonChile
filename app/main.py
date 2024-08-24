from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.endpoints import timelapse

import os
import ee
import json

# Load credentials from environment variable
service_account_info = json.loads(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS_JSON'))
credentials = ee.ServiceAccountCredentials('', service_account_info)
ee.Initialize(credentials)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(timelapse.router, prefix="/api/v1/timelapse")
