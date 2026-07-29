from fastapi import FastAPI

app = FastAPI(title="BharatAgri AI API")

@app.get("/")
def home():
    return {
        "message": "Welcome to BharatAgri AI",
        "status": "Running"
    }
