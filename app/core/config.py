import os
from dotenv import load_dotenv

load_dotenv()

# Example configuration variable
EARTH_ENGINE_API_KEY = os.getenv("EARTH_ENGINE_API_KEY")
