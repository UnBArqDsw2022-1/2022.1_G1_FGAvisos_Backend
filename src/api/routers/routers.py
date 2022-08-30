from fastapi import APIRouter

from src.api.endpoints import professor


api_router = APIRouter()
api_router.include_router(professor.router, 
                          prefix='/professor', 
                          tags=['professor'])