from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine

from app.api import auth
from app.api import auth
from app.api import layout
from app.models import models

import os

DATABASE_URL = "postgresql://postgres:Zxcvbnm%400@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)

app = FastAPI(title="Consumer Attention Mapping System")

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(layout.router, prefix="/api", tags=["Store Layouts"])

@app.get("/")
def read_root():
    return {"status": "Backend is operational"}