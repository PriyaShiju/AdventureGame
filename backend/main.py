import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from routers import story,job
from db.database import create_tables
create_tables()
app = FastAPI(
    title = "Adventure API",
    docs_url = "/docs",
    redoc_url = "/redoc",
    # openapi_url = "/openapi.json",
    description="API to create cool stories",
    version="1.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"], # get,post, put(update)
    allow_headers=["*"]
)
app.include_router(story.router,prefix=settings.API_PREFIX)
app.include_router(job.router,prefix=settings.API_PREFIX)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)