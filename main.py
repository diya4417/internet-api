from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "status": "API is running",
        "message": "Hello from the Internet API"
    }

@app.get("/api/test")
def test(name: str = "Guest"):
    return {
        "name": name,
        "result": "API endpoint works"
    }
