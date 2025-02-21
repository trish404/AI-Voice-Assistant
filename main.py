from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to My AI Voice Assistant"}

@app.get("/ping")
def ping():
    return {"message": "Server is running"}

