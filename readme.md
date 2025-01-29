# HNG Stage 0 API

This is a simple REST API built with FastAPI that returns basic information including an email address, current datetime, and GitHub repository URL.

## Live API URL

[Your Render URL here]

## Features

- Returns JSON response with:
  - Email address
  - Current datetime in ISO 8601 format
  - GitHub repository URL
- CORS enabled
- Fast response time
- Deployed on Render

## Tech Stack

- Python 3.8+
- FastAPI
- Uvicorn
- pytz

## Local Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/your-repo
cd your-repo
```

2. Create and activate virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

### Endpoint: GET /

Returns basic information in JSON format.

#### Response Format

```json
{
	"email": "ikwuhjcolejeff@gmail.com",
	"current_datetime": "2025-01-30T09:30:00Z",
	"github_url": "https://github.com/Jcolejeff/BE-stage-1"
}
```

#### Sample cURL Request

```bash
curl http://localhost:8000
```

## Deployment

This API is deployed on Render. Visit [your-api-url] to access the live version.

## Related Links

- [HNG Python Developers](https://hng.tech/hire/python-developers)
- [HNG C# Developers](https://hng.tech/hire/csharp-developers)
- [HNG Golang Developers](https://hng.tech/hire/golang-developers)
- [HNG PHP Developers](https://hng.tech/hire/php-developers)
- [HNG Java Developers](https://hng.tech/hire/java-developers)
- [HNG NodeJS Developers](https://hng.tech/hire/nodejs-developers)
