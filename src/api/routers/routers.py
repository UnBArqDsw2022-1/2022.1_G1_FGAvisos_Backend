from fastapi import APIRouter

from src.api.endpoints import professor
from src.api.endpoints import turma


api_router = APIRouter()
api_router.include_router(professor.router, 
                          prefix='/professor', 
                          tags=['professor'])
api_router.include_router(turma.router,
                          prefix='/turma',
                          tags=['turma'])