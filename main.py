from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime,timezone
import pytz

app = FastAPI()


origins = ["*"]  
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get_basic_info():
    """
    Returns basic information in JSON format:
      - email (used in the HNG12 Slack workspace)
      - current_datetime in ISO 8601 format (UTC)
      - github_url to the project's codebase
    """
    # Generate current UTC datetime in ISO 8601 format
    utc_time = datetime.now(timezone.utc).replace(microsecond=0)

    return {
        "email": "ikwuhjcolejeff@gmail.com",  
        "current_datetime":  utc_time.isoformat().replace("+00:00", "Z"),
        "github_url": "https://github.com/Jcolejeff/BE-stage-1"
    }
