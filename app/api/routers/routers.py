from fastapi import APIRouter

from app.api.endpoints import professor
from app.api.endpoints import turma
from app.api.endpoints import aviso
from app.api.endpoints import aluno


api_router = APIRouter()
api_router.include_router(professor.router, prefix='/professor', tags=['Professor'])
api_router.include_router(turma.router, prefix='/turma',tags=['Turma'])
api_router.include_router(aviso.router, prefix='/aviso',tags=['Aviso'])
api_router.include_router(aluno.router, prefix='/aluno',tags=['Aluno'])