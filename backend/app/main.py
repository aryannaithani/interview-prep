from fastapi import FastAPI

app = FastAPI(title="PrepForge API")

@app.get("/")
def root():
    return {"message": "PrepForge API is running"}

