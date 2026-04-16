from fastapi import FastAPI

app = FastAPI()

FULL_NAME = "Boluwaji Dare"
EMAIL = "dbolup@gmail.com"
GITHUB_URL = "https://github.com/Dbolup"


@app.get("/")
def root():
    return {"message": "API is running"}


@app.get("/health")
def health_check():
    return {"message": "healthy"}


@app.get("/me")
def me():
    return {
        "name": FULL_NAME,
        "email": EMAIL,
        "github": GITHUB_URL,
    }
 