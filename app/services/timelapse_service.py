import geemap
import ee
import os
from app.utils.ee_init import initialize_ee

async def generate_timelapse(request):
    initialize_ee()

    roi = ee.Geometry.BBox(
        request.boundingBox[0],
        request.boundingBox[1],
        request.boundingBox[2],
        request.boundingBox[3]
    )

    output_gif = 'static/landsat_timelapse.gif'
    
    timelapse = geemap.landsat_timelapse(
        roi,
        out_gif=output_gif,
        start_year=request.startYear,
        end_year=request.endYear,
        start_date=request.startDate,
        end_date=request.endDate,
        bands=['Blue', 'NIR', 'Red'],
        frames_per_second=request.fps,
        title='Landsat Timelapse',
        progress_bar_color='blue',
        mp4=False,
        frequency=request.frequency,
    )

    os.makedirs(os.path.dirname(output_gif), exist_ok=True)

    gif_url = f"http://127.0.0.1:8000/{output_gif}"
    return {"status": "Success", "message": "Timelapse generated", "gif_url": gif_url}
