from pydantic import BaseModel, Field
from typing import List

class TimelapseRequest(BaseModel):
    boundingBox: List[float] = Field(
        ..., 
        description="Bounding box coordinates as [min_lon, min_lat, max_lon, max_lat]",
        example=[-67.4989054621196, -18.396265626340664, -66.63761050858353, -19.231379922325146]
    )
    fps: int = Field(
        ..., 
        description="Frames per second for the timelapse video",
        ge=1,
        le=60,
        example=5
    )
    startYear: int = Field(
        ..., 
        description="Start year for the timelapse",
        ge=1984,
        le=2024,
        example=2000
    )
    endYear: int = Field(
        ..., 
        description="End year for the timelapse",
        ge=1984,
        le=2024,
        example=2024
    )
    startDate: str = Field(
        ..., 
        description="Start date for the timelapse in 'MM-DD' format",
        pattern="^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$",
        example="01-01"
    )
    endDate: str = Field(
        ..., 
        description="End date for the timelapse in 'MM-DD' format",
        pattern="^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$",
        example="12-31"
    )

    frequency: str = Field(
        ..., 
        description="Only use month, quarter, or year string.",
        pattern="^(month|quarter|year)$",
        example="month"
    )

    class Config:
        schema_extra = {
            "example": {
                "boundingBox": [-67.4989054621196, -18.396265626340664, -66.63761050858353, -19.231379922325146],
                "fps": 5,
                "startYear": 2000,
                "endYear": 2024,
                "startDate": "01-01",
                "endDate": "12-31",
                "frequency}": "month"
            }
        }
