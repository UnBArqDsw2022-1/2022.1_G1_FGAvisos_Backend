from fastapi import FastAPI, status, Depends, HTTPException

from app.models.aluno import AlunoModel
from app.schemas.aluno import AlunoSchema

from app.core.database import get_session
from app.api.routers.routers import api_router

from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.future import select

# Exemplos apenas para teste

app = FastAPI(title="FGAvisos API")
app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8001, reload=True)
