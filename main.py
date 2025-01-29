from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import pytz

app = FastAPI()

# Enable CORS (Cross-Origin Resource Sharing)
# This allows your API to be accessed from different domains/browsers without restrictions.
origins = ["*"]  # You can restrict to specific domains if you like.
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
    utc_now = datetime.now(tz=pytz.UTC).isoformat()

    return {
        "email": "your-email@example.com",  # Replace with your real email
        "current_datetime": utc_now,
        "github_url": "https://github.com/yourusername/your-repo"
    }
