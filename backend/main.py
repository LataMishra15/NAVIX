from fastapi import FastAPI

app = FastAPI(title="NAVIX API")


@app.get("/")
def home():
    return {
        "message": "NAVIX Backend is running 🚀"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }