# HNG Stage 1 DevOps API

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --host 127.0.0.1 --port 8000

Endpoints:


GET /
{
  "message": "API is running"
}

GET /health
{
  "message": "healthy"
}

GET /me
{
  "name": "Boluwaji Dare",
  "email": "dbolup@gmail.com",
  "github": "https://github.com/Dbolup"
}

Live URL
http://98.91.243.98
