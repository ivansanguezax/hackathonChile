from fastapi import APIRouter, HTTPException
from app.models.timelapse import TimelapseRequest
from app.services.timelapse_service import generate_timelapse

router = APIRouter()

@router.post("/")
async def create_timelapse(request: TimelapseRequest):
    try:
        return await generate_timelapse(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
