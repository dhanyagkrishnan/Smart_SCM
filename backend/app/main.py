from fastapi import FastAPI
from app.database import Base, engine
from app.api.routes import router
from fastapi.middleware.cors import CORSMiddleware
import app.models.models  # register SQLAlchemy models before creating tables

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart SCM - Agentic AI Integrated Supply Chain Management",
    description="Demo supply-chain dashboard with inventory, supplier, procurement and risk analysis.",
    version="1.0.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)

@app.get("/")
def root():
    return {
        "message": "Welcome to Smart SCM Agentic AI API",
        "status": "Running",
        "docs": "http://127.0.0.1:8000/docs",
    }
