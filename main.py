from fastapi import FastAPI
from app.routes import project_routes

app = FastAPI()

app.include_router(project_routes.router)

@app.get("/")
def home():
    return {"message": "Value Added Logistics Project Management API"}
