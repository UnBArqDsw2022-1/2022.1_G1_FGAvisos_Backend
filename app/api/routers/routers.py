from fastapi import APIRouter

from app.api.endpoints import professor
from app.api.endpoints import turma


api_router = APIRouter()
api_router.include_router(professor.router, prefix='/professor', tags=['professor'])
api_router.include_router(turma.router, prefix='/turma',tags=['turma'])