from typing import Set
from fastapi import FastAPI
from fastapi.openapi.utils import generate_operation_id
from fastapi.routing import APIRoute
from starlette.middleware.cors import CORSMiddleware

from app import settings
from app.routers.health import router as health_router


tags_metadata = [
    {"name": "document", "description": "document"},
]

title = 'Test'
description = 'Test'

app = FastAPI(debug=settings.DEBUG, openapi_tags=tags_metadata, title=title, description=description)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

app.include_router(health_router, tags=['health'])

